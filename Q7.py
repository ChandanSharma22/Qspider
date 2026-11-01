#Ab tum Q7 khud try karo: User se 12345 input lo aur output 5 aana chahiye, yani number mein kitne digits hain.
num=int(input("Enter the number as 12345 :"))
i=0
while num>0:
    num=num//10
    i+=1
print(i)
    
