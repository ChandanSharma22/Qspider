def sum_of_natural_number(num):
    sum=0
    for i in range(1,num+1):
        sum+=i
    return f"Sum of {num} natural number is {sum}"
print(sum_of_natural_number(5))