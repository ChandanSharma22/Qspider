age=int(input("Enter your age year"))
ragistred=input("Enter the value have you ragisterd YES or NOT")
if age>=18:
    print("elagibale",":",age)
    if ragistred=="YES":
        print("no need to ragistration")
    else:
        print("get ragister your self")
else:
    print("login")