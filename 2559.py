#시간초과

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))


sum=0
a=0
for j in range(n):

    if j+m < n:
        for i in range(m):
            sum+=arr[j+i]
    if a<sum:
        a=sum
    sum =0

print(a)

---------------------

# 수정

n, k = map(int, input().split())  

temp = list(map(int, input().split())) 

temp_sum = []
temp_sum.append(sum(temp[:k]))

for i in range(n-k):
  temp_sum.append(temp_sum[i] - temp[i] + temp[k+i])

print(max(temp_sum))
