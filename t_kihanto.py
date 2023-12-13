from browser import Browser

def kihanto():
  browser = Browser()
  
  #URLにアクセス
  browser.open_page("https://hikari-g.com/kihan/institution/tennis/")

  browser.click_button_by_class_name("ystdtb-banner-link__container")

  #タブを移動
  browser.switch_to_new_tab()

  #Browserを閉じる
  browser.close_browser()

if __name__ == "__main__":
  kihanto()