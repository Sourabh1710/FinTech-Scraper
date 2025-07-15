# Alternative Financial Data Scraper

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/release/python-3100/)                                                                                                
**Author:** **Sourabh Sonker (Aspiring Data Scientist)**

---

## Project Overview

This project is a modular Python application designed to collect **alternative financial data** by scraping the number of open job listings from major tech companies. In the world of quantitative finance, traditional data like quarterly earnings reports is widely available. This scraper creates a proprietary, high-frequency dataset that can serve as a leading indicator of a company's growth and future financial performance, providing a potential information edge for investment analysis.

The core of the project is a robust, configurable script that automates the data collection process and saves the results in a clean, analysis-ready CSV format.


---

## Key Features

*   **Modular Architecture:** The code is logically separated into a configuration file (`config.py`), a scraper module (`scraper.py`), and a main execution script (`main.py`).
*   **Multi-API Handling:** Successfully scrapes data from diverse and complex API architectures, demonstrating adaptability to different web technologies.
*   **Robust Error Handling:** Implements `try-except` blocks to gracefully handle network issues, API changes, or unexpected responses without crashing.
*   **Automated Data Structuring:** Parses raw web data and structures it into a time-stamped pandas DataFrame.
*   **Persistent Data Storage:** Appends new data to a daily CSV file, creating a valuable longitudinal dataset for time-series analysis.

---

## Technical Accomplishments & Challenges

A primary challenge of this project was adapting to the unique API architectures of each target company. I successfully **reverse-engineered and developed custom scrapers for two distinct systems**:

1.  **Nvidia (Workday API):** I developed a scraper that interacts with their Workday API. This required crafting a specific JSON payload and sending it via a `POST` request to retrieve the total job count, a common but often undocumented corporate API structure.
2.  **Amazon (Custom JSON Endpoint):** For Amazon, I reverse-engineered a complex `GET` request endpoint. This involved analyzing the URL parameters and decoding a JSON response where the total job count was not a direct value, but had to be calculated by summing values across multiple data "facets" within the JSON object.

The project also included a **thorough investigation into advanced anti-scraping technologies**. For other targets like Microsoft and Apple, my analysis determined that they employ dynamic, JavaScript-heavy rendering and sophisticated anti-bot measures. I successfully diagnosed this and confirmed that a full browser automation tool like Selenium would be the required approach, demonstrating a deep understanding of modern web technologies and the ability to make strategic project decisions.

---

## Technologies Used

*   **Language:** Python 3
*   **Libraries:**
    *   `requests`: For making robust HTTP requests to web servers and APIs.
    *   `pandas`: For data manipulation and structuring the final output.
    *   `BeautifulSoup`: (Used during the investigative phase) For parsing HTML and XML documents.
*   **Environment:**
    *   `venv`: For managing project dependencies in an isolated virtual environment.

---

## Project Structure

   ```bash
         fintech_scraper/
       ├── config.py # Configuration file for target companies and URLs
       ├── main.py # Main script to execute the scraper
       ├── scraper.py # Contains all the scraper functions
       ├── data/
       │ └── job_listings_YYYY-MM-DD.csv # Example output file
       └── README.md
   ```
---

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/fintech-scraper.git
    cd fintech-scraper
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You will need to generate this file. See next section.)*

4.  **Run the scraper:**
    ```bash
    python main.py
    ```
    The script will print its progress to the console and save/append the results to a CSV file in the `data/` directory.

