import requests
from bs4 import BeautifulSoup
import time
#ページ数のカウントをする
def titleListUp():
    s = True #ループ変数
    urlnum = 0  #ページ数
    f = open('toku.txt', 'w') #各話タイトルを格納するファイル

    while s:
        load_url = "https://omocoro.jp/tag/%E5%8C%BF%E5%90%8D%E3%83%A9%E3%82%B8%E3%82%AA/page/" + str(urlnum) + "/"
        html = requests.get(load_url)
        soup = BeautifulSoup(html.content, "html.parser")
        for element in soup.select("span"):
           if element.text == "記事が見つかりませんでした" :
                s = False
        if s == False:
            break
        for element in soup.select("a"):    # すべてのliタグを検索して表示
            if element.text.startswith("【"):
                f.write(element.text.replace('ARuFa・恐山の匿名ラジオ','') + '\n')
        time.sleep(0.5)
        urlnum += 1
    return 0
