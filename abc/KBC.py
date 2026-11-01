
def welcome(name):
    print(f"{name} kbc me apka swagat hai\n")

def rules():
    print("""1)you have 7 question
     2)you have 4 option
     3)if your choice is correct you get the price """ )

def question_bank():
    price=0
    q1="1)how mush golas has ronaldo scored till now\na)300\tb)983\nc)321\td)42"
    ans1="b"
    price=ask_question(q1,ans1,price)
    if price==-1:
        return print("you failed\n")
    print(f"your choice is correct you have won {price}")

    q2="2)how many days in a leap year\na)365\tb)364\nc)366\td)367"
    ans2="c"
    price=ask_question(q2,ans2,price)
    if price==-1:
        return print("you failed\n")
    print(f"your choice is correct you have won {price}")

    q3="3)which city is called the 'pink city'\na)kerala\tb)jaipur\nc)mumbai\td)c"
    ans3="b"
    price=ask_question(q3,ans3,price)
    if price==-1:
        return print("you failed\n")
    print(f"your choice is correct you have won {price}")

    q4="4)largest river in the world \na) amazon \tb)neil \nc)ganga \td)yamuna"
    ans4="a"
    price=ask_question(q4,ans4,price)
    if price==-1:
        return print("you failed\n")
    print(f"your choice is correct you have won {price}")

    q5="5)smallest country \na)india \tb) austrailia\nc)vatican\td) kerala"
    ans5="c"
    price=ask_question(q5,ans5,price)
    if price==-1:
        return print("you failed\n")
    print(f"your choice is correct you have won {price}\n")
    print(f"\nYou won the game{name}")
    

def ask_question(question,answer,current_price):
    print(question)
    ans=input("enter your answer\n")
    if ans==answer:
        current_price+=10000000
        return current_price
    else:
        return -1

print("-----Welcome---\n")
name=input("enter your name:")
welcome(name)
choice=input("Are you redy to start (y/n)")
if choice=="n":
    print("Thank you for plaing")
    
elif choice=="y":
    rules()
    question_bank()
