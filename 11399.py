N = int(input())
p = list(map(int, input().split(" ")))

p.sort()

x =0
result =[]
for i in p:
    x += i
    result.append(x)

print(sum(result))