
a = int(input())

cnt = 0
tempo = a

if a ==0:
    print("NO")
elif a==1:
    print("YES")
else:
    while tempo > 0:
        if tempo//3 >0:
            cnt += 1
            tempo = tempo//3
        else:
            tempo =0
            for i in range(cnt):
                s = a
                if s - 3**(cnt-i) >0:
                    a -= 3**(cnt-i)
                    #print(3**(cnt-i))
            if a ==1 or a==0:
                print("YES")
            elif a>1:
                print("NO")




