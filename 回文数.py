'''
有二个条件 ：
   1 .倒数第一要相等
   2 .两头的数相加等于中间数
'''
num=int(input("请输入范围："))
while num>=10000:
    g=num%10
    s=num//10%10
    b=num//100%10
    q=num//1000%10
    w=num//10000%10
    if g==w and s==q and g+s+q+w==b:
        print("回文数是：%d"%num)
    num-=1
