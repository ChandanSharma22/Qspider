#get input from the user and reverse that number
# Get input from the user and reverse that number
num = int(input("Enter the number: "))

reverse = 0

while num > 0:
    last_digit = num % 10
    reverse = reverse * 10 + last_digit
    num = num // 10

print("Reversed number:", reverse)