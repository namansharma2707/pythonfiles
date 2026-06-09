total = 21
while True:
    n = int(input("enter no:"))
    match n:
        case 0:
            print("total is",total)
            print("computer choose 0")
            print("total is",total)
        case 1:
            print("total is",total)
            print("computer choose 4")
            total-=5
            print("total is",total)
        case 2:
            print("total is",total)
            print("computer choose 3")
            total-=5
            print("total is",total)
        case 3:
            print("total is",total)
            print("computer choose 2")
            total-=5
            print("total is",total)
        case 4:
            print("total is",total)
            print("computer choose 1")
            total-=5
            print("total is",total)
        case _:
            print("0-4 me ek no choos karo")
    if total == 1:
        print("u lost")
        exit(0)
print("you lose")