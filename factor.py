def fac(n):
    l = []
    for i in range(2,n//2):
        if n%i:
            continue
        else:
            l.append(i)
    l.append(n)
    return l
l = fac(n=int(input("enter the no:")))
print("the smallest factor is ",l[0])
