import requests
import json
from bs4 import BeautifulSoup

URL = f"https://www.rocketpunch.com/api/jobs/template?location=서울특별시&specialty=Java&specialty=JSP&tag=웹서비스&tag=e-commerce"


def extract_total_page():
    response = requests.get(URL)
    json_dumps = json.dumps(response.text)
    json_data = json.loads(json_dumps)
    json_data = json.loads(json_data)
    body = json_data["data"]["template"]
    soup = BeautifulSoup(body, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})
    pagination = pagination.find("div", {"class", "widescreen"})
    return int(pagination.find_all("a", {"class": "item"})[-1].string)


def extract_rocket_jobs(total_page):
    company_infos = []
    for page in range(total_page):
        req = requests.get(f"{URL}&page={page + 1}")
        st_json = json.dumps(req.text)
        dict = json.loads(st_json)
        dict = json.loads(dict)
        html = dict["data"]["template"]
        soup = BeautifulSoup(html, "html.parser")
        body = soup.find("div", {"id": "company-list"})
        companies = body.find_all("div", {"class": "company"})
        for company in companies:
            company_info = extract_company_info(company)
            company_infos.append(company_info)
    return company_infos


def extract_company_info(company):
    company_id = company["data-company_id"]
    company_name = company.find("div", {"class": "company-name"})
    company_name = company_name.find("h4", {"class": "header"})
    company_name = company_name.find("strong").string
    service_types = company.find("div", {"class": "nowrap"}).get_text(strip=True)
    company_url = company.find("a")["href"]
    company_url = f"https://www.rocketpunch.com/{company_url}"
    return {'id': company_id, 'compnay_name': company_name, 'service_type': service_types, 'company_url': company_url}


def get_rocket_jobs():
    total_page = extract_total_page()
    return extract_rocket_jobs(total_page)
