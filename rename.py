import os

def rename(filePath):
    f = open('toku.txt', 'r', encoding='UTF-8')


    datalist = f.readlines()
    print (datalist[0])
    print (datalist[1])
    print (datalist[2])


    for i in datalist:
        if os.path.exists(filePath + i.split('【')[-1].split('】')[0] + '.mp3'):
            print("ある！" + i.split('【')[-1].split('】')[0] + '.mp3')
            #os.rename(filePath + i.split('【')[-1].split('】')[0] + '.mp3', filePath + i + '.mp3', )
        else:
            print("ないよ〜〜〜〜〜〜〜〜ーーーー" + i.split('【')[-1].split('】')[0] + '.mp3')


    f.close()
