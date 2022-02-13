import os

def rename(filePath):
    f = open('toku.txt', 'r', encoding='UTF-8')


    datalist = f.readlines()


    for i in datalist:
        #数字.mp3があれば、datalist[i].mp3にリネーム
        if os.path.exists(filePath + i.split('【')[-1].split('】')[0] + '.mp3'):
            os.rename(filePath + i.split('【')[-1].split('】')[0] + '.mp3', filePath + i + '.mp3', )

    print("リネーム完了")
    f.close()
