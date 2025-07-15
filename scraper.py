import requests
from bs4 import BeautifulSoup

def scrape_api_post_workday(url):
    """Scraper for Workday POST request APIs (like Nvidia)."""
    try:
        payload = {"appliedFacets": {}, "limit": 1, "offset": 0, "searchText": ""}
        headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        response.raise_for_status()
        data = response.json()
        job_count = data.get('total')
        return int(job_count) if job_count is not None else 0
    except (requests.exceptions.RequestException, KeyError, ValueError) as e:
        print(f"  - Error during Workday API POST request: {e}")
        return 0

def scrape_api_get_facet(url):
    """Scraper for GET request APIs summing facets (like Amazon)."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()
        facets = data.get('facets', {}).get('employee_class_facet', [])
        if not facets: return 0
        total_jobs = sum(list(item.values())[0] for item in facets)
        return total_jobs
    except (requests.exceptions.RequestException, KeyError, ValueError, IndexError) as e:
        print(f"  - Error during Facet API GET request: {e}")
        return 0



SCRAPER_MAPPING = {
    'api_post_workday': scrape_api_post_workday,
    'api_get_facet': scrape_api_get_facet,
}