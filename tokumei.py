import time
import urllib.request

s = ""
print("何話までDLした？:")
nanwa = int(input()) + 1
print("何話までDLする？:")
made = int(input())

for i in range(made - nanwa):
    s = str(i+nanwa).zfill(3)
    print("#"+s+"をダウンロード中")
    urllib.request.urlretrieve("https://omocoro.heteml.net/radio/tokumei/"+s+".mp3","/Users/yk001/environment/tokumeiradio/"+s+".mp3")
    print("30秒待機中…")
    time.sleep(30)

print("おわり")

#なんやねん！！！ああああああああああああ