import sys
input = sys.stdin.readline # 런타임 빨라서 씀

n=int(input())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort()
b.sort(key=lambda b:-b)

s=[]
for i in range(n):
    s.append(a[i]*b[i])

print(sum(s))

