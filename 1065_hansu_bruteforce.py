N = int(input())
count = 0
for i in range(1, N+1):
    if i < 100:
        count += 1
    elif i > 100:
        n1 = int((i % 100) % 10)
        n2 = int(((i-n1) % 100)/10)
        n3 = int((i-(n1+n2))/100)

        a = n2-n1
        b = n3-n2
        c = n3-n1
        if a == b:
            count += 1
print(count)
