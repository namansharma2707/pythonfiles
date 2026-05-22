s = int(input("starting no(smaller):"))
e = int(input("ending no(larger):"))
if e-s<0:
    print("starting chota hota h and ending bada")
    exit(1)
su=0
m=1
for i in range(s,e+1):
    su += i
    m *= i
    print(f"the sum si {su}\nthe product is {m}")
