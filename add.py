s = 0
def add():    
        global s
        n = int(input("entere the no:"))
        if n>0:
            s = s+n
            return add()
        else:
            return s
print(add())
