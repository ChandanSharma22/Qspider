def sum(num):
    sum=0
    while num>0:
        sum=sum+(num%10)
        num//=10
    return sum

def productofdigit(num):
    product=1
    while num>0:
        product=product*(num%10)
        num=num//10
    return product

def spy(num):
    if sum(num)==productofdigit(num):
        return True
    else:
        return False

print(spy(123))

    

    