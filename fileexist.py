import urllib.request
#--------------------------------------------------------
#そのURLがあるかどうかを調べる関数
def UrlChecker(urlname00):
    try:
        res = urllib.request.urlopen(urlname00)
        un=res.geturl()
        res.close()
        if un == urlname00:
            return 1
        else:
            return 0
        pass
    except:
        return 0
        pass
#----------------------
# URLを調べる
#----------------------