while(True):
    n1, n2 = list(map(int, input().split()))
    if n1+n2 == 0:
        break
    if n2 % n1 == 0:
        print("factor")
    elif n1 % n2 == 0:
        print("multiple")
    else:
        print("neither")
