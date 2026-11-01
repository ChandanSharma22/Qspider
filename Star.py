"""for i in range(5):
    for j in range(5):
        if i<=j:
            print(" ","*",end="")
    print("")
    """
'''for i in range(5,0,-1):
    print(" "*(5-i)+"*"*i)

'''

#print * backslesh  line fly
'''for i in range(3):
    for j in range(3):
        if i==j:
            print("*",end="")
        else:
            print(" ",end=" ")
    print("")
'''

'''for i in range(5):
    for j in range(5):
        if i+j==4 and  i==j:
            print("*",end="")
        else:
            print(" ",end=" ")
    print("")
'''

'''for i in range(5):
    for j in range(5):
        if i+j==4 or  i==j:
            print("*",end="")
        else:
            print(" ",end=" ")
    print("")'''

'''for i in range(5):
    for j in range(5):
        if i==j:
            print("*",end="")
        else:
            print(" ",end=" ")
    print("")'''

#WAPP to vlidate a string if there is an spesh in a string the string is not valid 
"""str1=input("enter a str")
for i in str1:
    if i ==" ":
        print("invalid str")
        break 
else:
    print("valid string")
    """

#WAPP to find the repeted chr in string 
'''str1=input("enter any string")
for i  in str1:
    count=0
    for j in str1:
        if i==j:
            count+=1
    if count>=2:
        print(f"({i}) character is repeted")
        break
else:
    print("not found")
'''

#WAPP to check if a string contains any number by checking each character one by one 
str1=input("enter any string containg any number")
for i in str1:
    if i in "0123456789":
        print("string has number\n")
        break
else:
    print("string has no number")