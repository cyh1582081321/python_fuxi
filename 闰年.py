'''
闰年的判断
'''
year = int(input('请输入要判断的年份：'))

if year%4 == 0:
    if  year%100 == 0:
        if year%400 == 0:
            print("您要查询的年份是闰年！！")
        else :
            print("您查询的年份是平年！！")
    else :
         print("您要查询的年份是闰年！！")
else :
            print("您查询的年份是平年！！")
