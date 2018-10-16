arr = [1,2,2,2,2,[4,4,4,[4,4,4,[5,8],4]]]
sum = 0
def list1(arr):
    global sum
    sum += 1
    for i in arr:
        if isinstance(i, list):
            list1(i)
        else:
            print(i)
list1(arr)
print(20 * "*")
print(sum)
