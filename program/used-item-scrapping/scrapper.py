from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

driver = webdriver.Chrome("/Users/melchor/dev/chromedriver")
driver.get('https://nid.naver.com/nidlogin.login')
time.sleep(1)

tag_id = driver.find_element_by_id('id')
tag_pw = driver.find_element_by_id('pw')
tag_id.clear()
time.sleep(1)

# id 입력
tag_id.click()
pyperclip.copy('아이디')
tag_id.send_keys(Keys.COMMAND, 'v')
time.sleep(1)

# pw 입력
tag_pw.click()
pyperclip.copy('비밀번호')
tag_pw.send_keys(Keys.COMMAND, 'v')
time.sleep(1)

# 로그인 버튼을 클릭합니다
login_btn = driver.find_element_by_id('log.login')
login_btn.click()

