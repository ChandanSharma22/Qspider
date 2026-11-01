num=int(input("Enter any number"))
count=0
while num>0:
    last_digit=num%10
    if last_digit==7:
        count+=1
        num=num//10
    else:
        print("no 7 found")
print(f"{count}")
