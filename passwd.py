print("guess the password")
for i in range(3):
    n = input("enter the password(5): ")
    if n == "12345":
        print("login successfully")
        exit()
    print("you have",2-i,"attempts")
print("the account is locked")
