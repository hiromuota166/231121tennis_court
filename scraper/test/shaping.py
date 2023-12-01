from bs4 import BeautifulSoup

def replace_img_with_div(html_data):
    soup = BeautifulSoup(html_data, 'html.parser')

    # すべての<img>タグを検索
    for img in soup.find_all('img'):
        if 'p_img/msg_icon01.gif' in img['src']:
            new_div = soup.new_tag('div')
            new_div.string = '×'
            new_div['width'] = img['width']
            new_div['height'] = img['height']
            img.replace_with(new_div)
        elif 'p_img/msg_icon05.gif' in img['src']:
            new_div = soup.new_tag('div')
            new_div.string = '⚪'
            new_div['width'] = img['width']
            new_div['height'] = img['height']
            img.replace_with(new_div)

    return str(soup)

if __name__ == "__main__":
    replace_img_with_div()
