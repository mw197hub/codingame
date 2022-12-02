import time

start = time.time()

'''
MAXN=1000
dp = [0]*(MAXN)

# base case
dp[0] = 1
for i in range(1,MAXN):
   dp[i] = dp[i-1] * i
print(dp[-1])
'''
'''
list1 = [0]*10
list2=list1
list1.append(2)
list2.extend([3,4])
print(list1)
print(list2)
'''
def area(length: int, width: int):
    print(length * width)

area_func = globals()["area"]
print(type(area_func))
area_func(5, 5)


print(time.time()-start)


