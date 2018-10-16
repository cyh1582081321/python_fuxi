'''
栈：没有真正的栈，只能用list去模拟栈的存储
特点：先进后出

'''
stack = []

stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)
stack.append(60)
stack.append(70)

print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())

#collection__收集 、deque__队列
from collections import deque
duilie = deque()

duilie.append(10)
duilie.append(20)
duilie.append(30)
duilie.append(40)
duilie.append(50)
duilie.append(60)
duilie.append(70)
duilie.append(80)
duilie.append(90)
print(duilie)
# 直接看体现不出来
print(duilie.popleft())
print(duilie)
print(duilie.popleft())
print(duilie)
print(duilie.popleft())
print(duilie)
print(duilie.popleft())
print(duilie)
print(duilie.popleft())
print(duilie)

