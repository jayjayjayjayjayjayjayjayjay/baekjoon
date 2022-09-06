n = input().split('-')
answer =0

#맨처음 숫자는 무조건 더함
for i in n[0].split('+'):
    answer += int(i)

for i in n[1:]:
    for j in i.split('+'):
       answer -= int(j)

print(answer)
