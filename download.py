import time
import urllib.request
import fileexist

def downloadFile(filePath):
    s = ""
    print("何話までDLした？:")
    nanwa = int(input()) + 1
    print("何話までDLする？:")
    made = int(input())

    for i in range(made - nanwa + 1):
        s = str(i+nanwa).zfill(3)
        print("#"+s+"をダウンロード中")
        if fileexist.UrlChecker("https://omocoro.heteml.net/radio/tokumei/"+s+".mp3") > 0:
            urllib.request.urlretrieve("https://omocoro.heteml.net/radio/tokumei/"+s+".mp3",filePath+s+".mp3")
            print("30秒待機中…")
            time.sleep(30)
        else:
            print("https://omocoro.heteml.net/radio/tokumei/"+s+".mp3が存在しません")
        
        

#pushテスト