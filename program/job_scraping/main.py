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


