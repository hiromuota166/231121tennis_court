# urlがいつでも使えるならこれでいい

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup

options = Options()
options.headless = True # ヘッドレスモード True=非表示, False=表示
driver = webdriver.Chrome(options=options)

url_court = "https://www.reserve1.jp/yoyaku/member/member_job_select.php"