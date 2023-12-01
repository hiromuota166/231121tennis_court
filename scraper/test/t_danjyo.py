# ゴールは指定した日付の予約状況を取得すること
import time
from test.browser import Browser
from test.shaping import replace_img_with_div

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
  # 火曜日が定休日なので、火曜日は違う表記
  if time.strftime("%a") != "Tue":
    #予約状況を取得
    open_court = browser.get_html_by_class_name("table_base")

    #不要な改行を取り除く
    formatted_open_court = open_court[0].replace("\n", "")

    #文章整形を適用
    final_output = replace_img_with_div(formatted_open_court)
    return final_output
  else:
    # h1タグで定休日の文言を取得
    closed_day = "定休日です"
    return closed_day

if __name__ == "__main__":
  danjyo()