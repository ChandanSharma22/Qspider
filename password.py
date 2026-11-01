password=input("enter  a password: \n")
is_upper=False
is_lower=False
is_digit=False
is_spch=False
for i in password:
    if "A"<=i>="Z":
        is_upper=True
    elif "a"<=i >="z":
        is_lower=True
        