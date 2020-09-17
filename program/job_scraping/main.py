import requests
import json
from bs4 import BeautifulSoup

page = 1
url = f"https://www.rocketpunch.com/api/jobs/template?page={page}"

req = requests.get(url)

st_json = json.dumps(req.text)

dict = json.loads(st_json)
dict = json.loads(dict)
html = dict["data"]["template"]

soup = BeautifulSoup(html, "html.parser")

body = soup.find("div", {"id": "company-list"})

companies = body.find_all("div", {"class": "company"})
for company in companies:
    company_id = company["data-company_id"]
    company_name = company.find("div", {"class": "company-name"})
    company_name = company_name.find("h4", {"class": "header"})
    company_name = company_name.find("strong").string
    # print(job.find("h4", {"class", "header"}))

