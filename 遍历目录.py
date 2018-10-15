'''
目录的遍历获取

'''
import os


def getdir(path):
    #获取当前目录所有文件和目录的名字存储到列表中
    pathname =  os.listdir(path)
    for name in pathname:
        #拼接当前文件的绝对路径
        abspath = os.path.join(path,name)
        #判断当前所在的是文件还是目录
        if os.path.isfile(abspath):
            print("文件名",name)
        else:
            print("目录名",name)
            getdir(abspath)
path = input("请输入文件路径：")
getdir(path)
