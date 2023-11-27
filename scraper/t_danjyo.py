# ゴールは指定した日付の予約状況を取得すること
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup
from browser import Browser

def danjyo():
  browser = Browser()

  #URLにアクセス
  browser.open_page("https://sports932.net/facility/danjo/")

  #次へボタンをクリック
  browser.click_next_name("button")

  #タブを移動
  browser.switch_to_new_tab()

  #遷移先のURLを取得
  # url = browser.get_current_url()

  #予約状況からみるをクリック
  browser.click_specific_button_by_name("button")

  #予約状況を取得
  open_court = browser.get_html_by_class_name("table_base")
  return open_court
if __name__ == "__main__":
  danjyo()