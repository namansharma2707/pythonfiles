def divi(n,d):
    if d ==1:
        return False
    if n%d == 0 :
        return True
if divi(n=int(input("enter no")),d=int(input("enter divisor:"))):
    print("yes it is divisible")
else:
    print("it is not")
