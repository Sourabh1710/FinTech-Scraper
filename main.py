import pandas as pd
from datetime import date
from config import COMPANIES_TO_SCRAPE
from scraper import SCRAPER_MAPPING

def run_scraper():
    """
    Main function to run the web scraper for all configured companies.
    """
    print("Starting the financial data scraper...")
    
    scraped_data = []
    today = date.today().strftime("%Y-%m-%d")
    
    for company, details in COMPANIES_TO_SCRAPE.items():
        print(f"Scraping job data for {company}...")
        
        method = details.get('method')
        url = details.get('url')
        
        if not method or not url:
            print(f"  - Skipping {company}: Configuration is incomplete.")
            continue
            
        scraper_function = SCRAPER_MAPPING.get(method)
        
        if not scraper_function:
            print(f"  - Skipping {company}: No valid scraper function found for method '{method}'.")
            continue
            
        # Call the appropriate scraper function
        job_count = scraper_function(url)
        
        if job_count > 0:
            print(f"  - Success! Found {job_count} jobs.")
            scraped_data.append({
                'Date': today,
                'Company': company,
                'Job_Count': job_count
            })
        else:
            print(f"  - Failed to retrieve a valid job count for {company}.")

    if not scraped_data:
        print("\nScraping complete. No data was successfully retrieved. Output file will not be created.")
        return

    # --- Save the data to a CSV file ---
    df = pd.DataFrame(scraped_data)
    
    # Create a unique filename with today's date
    output_filename = f"data/job_listings_{today}.csv"
    print(f"\nScraping complete. Saving data to {output_filename}")
    
    # To prevent overwriting, we can append or check for file existence
    try:
        # If the file already exists, load it and append new data
        existing_df = pd.read_csv(output_filename)
        combined_df = pd.concat([existing_df, df]).drop_duplicates(subset=['Date', 'Company'], keep='last')
        combined_df.to_csv(output_filename, index=False)
        print("Appended data to existing file.")
    except FileNotFoundError:
        # If the file doesn't exist, create it
        df.to_csv(output_filename, index=False)
        print("Created new data file.")

if __name__ == "__main__":
    run_scraper()