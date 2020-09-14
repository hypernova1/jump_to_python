from page_extractor import extract_page, extract_jobs

last_page = extract_page()

jobs = extract_jobs(last_page)

print(jobs)
