with open("n.txt","+a") as f:
    f.write(input("enter your name,city,age:")+"\n")
with open("n.txt","r") as f:
    a = f.read()
    print(a)
