import requests
from bs4 import BeautifulSoup
import time
# Webページを取得して解析する

urlnum = 14
load_url = "https://omocoro.jp/tag/%E5%8C%BF%E5%90%8D%E3%83%A9%E3%82%B8%E3%82%AA/page/"
f = open('toku.txt', 'w')

# HTML全体を表示する
for p in range(14):
    load_url = "https://omocoro.jp/tag/%E5%8C%BF%E5%90%8D%E3%83%A9%E3%82%B8%E3%82%AA/page/" + str(urlnum) + "/"
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")
    for element in soup.select("a"):    # すべてのliタグを検索して表示
        if element.text.startswith("【"):
            f.write(element.text.replace('ARuFa・恐山の匿名ラジオ','') + '\n')
    urlnum -= 1
    time.sleep(0.5)

print("完了")
