'''
break 和 continue 用方法

'''
name = 'xiaoming'

for i in name:

    if i == 'm':
        break
    print(i,end='')
print()    
print(50*"*")
for t in name:
    if t == 'm':
        continue
    
    print(t,end='')
