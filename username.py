import abc
Attempt=3
username=abc
password=123
while Attempt:
        user_name=input("Enter your user name")
        Pass_word=int(input("Enter your password"))
        if user_name==username and  Pass_word==password:
              print("login Successfully")
              break
        Attempt-=1
        print(f"you have {Attempt} Attempt left")
else:
       print("no more attempt")