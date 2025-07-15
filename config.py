COMPANIES_TO_SCRAPE = {
    'Nvidia': {
        'method': 'api_post_workday', 
        'url': 'https://nvidia.wd5.myworkdayjobs.com/wday/cxs/nvidia/NVIDIAExternalCareerSite/jobs'
    },
    'Amazon': {
        'method': 'api_get_facet',
        'url': 'https://www.amazon.jobs/en/search.json?base_query=&city=&country=&county=&facets%5B%5D=location&facets%5B%5D=business_category&facets%5B%5D=category&facets%5B%5D=schedule_type_id&facets%5B%5D=employee_class&facets%5B%5D=normalized_location&facets%5B%5D=job_type&latitude=&loc_group_id=&loc_query=&longitude=&offset=0&query_options=&radius=24km®ion=&result_per_page=1&sort=relevant'
    }
}