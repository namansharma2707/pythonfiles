#creating list
a = [10,20,30,40,50,60,70,80,90]
print(a)
#positive indexing
print(a[2])
#negative indexing
print(a[-3])
#start:end
print(a[2:6])
#start:end:step
print(a[1:8:2])
#reverse slicing
print(a[::-1])
#odd even
print(a[::2])
print(a[1::2])
#length
print(len(a))
#membership
if 40 in a:
    print("yes")
#concatenation
b = [100,200]
print(a + b)
#repetition
print(b * 3)
#nested list
x = [1,2,[10,20,[100,200]]]
print(x[2][2][1])
#mutable
a[0] = 999
print(a)
#loop
counter = 0
while counter < len(a):
    print(a[counter])
    counter += 1
