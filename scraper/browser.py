from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class Browser:
    def __init__(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)

    #urlを開く
    def open_page(self, url):
        self.driver.get(url)
        time.sleep(2)

    #タブ移動
    def switch_to_new_tab(self):
        # 現在のタブのリストを取得
        window_handles = self.driver.window_handles

        # 新しいタブ（最後に開いたタブ）に切り替える
        self.driver.switch_to.window(window_handles[-1])

    #name属性の次へボタンをクリック
    def click_next_name(self,button_name):
        next_btn = self.driver.find_element_by_name(button_name)
        next_btn.click()
        time.sleep(2)

    #x-path属性の次へボタンをクリック
    def click_next_xpath(self, xpath):
        next_btn = self.driver.find_element_by_xpath(xpath)
        next_btn.click()
        time.sleep(2)

    #指定したボタンをクリック
    def click_specific_button_by_name(self, button_name, index=0):
        buttons = self.driver.find_elements_by_name(button_name)
        if len(buttons) > index:
            buttons[index].click()
            time.sleep(2)
        else:
            print(f"指定されたインデックス({index})のボタンは存在しません。")

    #現在のURLを取得
    def get_current_url(self):
        return self.driver.current_url

    #class名を指定して、テキストを取得
    def get_text_by_class_name(self, class_name):
        return self.driver.find_element_by_class_name(class_name).text
    
    #javascriptをクリック
    def click_javascript(self, javascript):
        self.driver.execute_script(javascript)
        time.sleep(2)

    #value属性を指定して、ボタンをクリック
    def click_button_by_value(self, value):
        self.driver.find_element_by_css_selector(f"input[value='{value}']").click()
        time.sleep(2)