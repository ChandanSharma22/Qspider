
# WAPP to check whether a number is perfect or not

def is_perfect_number(a):
    sum = 0

    for i in range(1, a):
        if a % i == 0:
            sum += i

    if sum == a:
        return f"The number {a} is a perfect number"
    else:
        return f"The number {a} is not a perfect number"

print(is_perfect_number(13))


