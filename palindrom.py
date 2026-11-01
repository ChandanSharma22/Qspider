num=int(input("Enter any number"))
temp=num
reverse=0
while num>0:
    last_digit = num % 10
    reverse = reverse * 10 + last_digit
    num = num // 10
if reverse==temp:
    print("number is palindrom")
    
else:
    print("number is not palindrom")
    