#まずラジオのページ数を入力させる
import pagenum
import rename
import download


download.downloadFile('/Users/yk001/environment/tokumeiradio/')
pagenum.titleListUp()
rename.rename('/Users/yk001/environment/tokumeiradio/')
print("終了します")