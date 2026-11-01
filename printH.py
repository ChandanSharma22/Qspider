'''
#print H
for i in range(5):
    for j in range(5):
        if j==0 or j==4 or i==2:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print("")
'''
"""
#print I
for i in range(5):
    for j in range(5):
        if i==0 or j==2 or i==4:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print("")
"""
"""
#print Swasthik
for i in range(5):
    for j in range(5):
        if (j==2 or i==2 )or (i==0 and j>=2)or(j==0 and i<=2)or(j==4 and i>=2) or (i==4 and j<=2):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print("")
"""
"""
for i in range(5):
    for j in range(5):
        if (j==2 or i==2 )or(i==0 and j>=2)or(j==4 and i<=2)or(j==0 and i>=2)or(i==4 and j<=2):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print("")
"""
"""
#print hart
for i in range(6):
    for j in range(7):
        if (i==0 and j%3!=0)or(i==1 and j%3==0)or(i-j==2)or(i+j==8):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print("")
"""
"""
def abc(num1,num2):
    print(num1*num2)
abc(2,3)
"""
#find max number
def max_two(a,b):
    if a>b:
        return a 
    else:
        return b
num1=int(input("Enter any number"))
num2=int(input("Enter any number"))
print(max_two(num1,num2))