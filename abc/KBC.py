
def welcome(name):
    print(f"\nNamaste {name}! KBC mein aapka swagat hai.\n")


def rules():
    print("""
========== RULES OF THE GAME ==========

1. Game mein total 7 questions hain.
2. Har question mein 4 options hain (a, b, c, d).
3. Har correct answer par prize money milegi.
4. Wrong answer dene par game end ho jayega.
5. Answer dene ke liye a, b, c ya d enter karein.

=======================================
""")


def ask_question(question, options, correct_answer, prize):
    print("\n" + question)

    for option, answer in options.items():
        print(f"{option}) {answer}")

    while True:
        user_answer = input("Apna answer enter karein (a/b/c/d): ")
        user_answer = user_answer.strip().lower()

        if user_answer in options:
            break
        else:
            print("Invalid option! Please a, b, c ya d enter karein.")

    if user_answer == correct_answer:
        print(f"\nCorrect answer! Aapne Rs. {prize:,} jeete! 🎉")
        return True
    else:
        print(f"\nWrong answer! Sahi answer hai: {correct_answer}) "
              f"{options[correct_answer]}")
        return False


def question_bank():
    questions = [
        {
            "question": "1. Leap year mein kitne din hote hain?",
            "options": {
                "a": "365",
                "b": "364",
                "c": "366",
                "d": "367"
            },
            "answer": "c"
        },
        {
            "question": "2. Pink City kise kaha jata hai?",
            "options": {
                "a": "Mumbai",
                "b": "Jaipur",
                "c": "Delhi",
                "d": "Pune"
            },
            "answer": "b"
        },
        {
            "question": "3. Duniya ka sabse chhota desh kaun sa hai?",
            "options": {
                "a": "India",
                "b": "Nepal",
                "c": "Vatican City",
                "d": "Bhutan"
            },
            "answer": "c"
        },
        {
            "question": "4. Solar System mein kitne planets hain?",
            "options": {
                "a": "7",
                "b": "8",
                "c": "9",
                "d": "10"
            },
            "answer": "b"
        },
        {
            "question": "5. Python kya hai?",
            "options": {
                "a": "Programming language",
                "b": "Operating system",
                "c": "Web browser",
                "d": "Database"
            },
            "answer": "a"
        },
        {
            "question": "6. Ek week mein kitne din hote hain?",
            "options": {
                "a": "5",
                "b": "6",
                "c": "7",
                "d": "8"
            },
            "answer": "c"
        },
        {
            "question": "7. HTML ka full form kya hai?",
            "options": {
                "a": "HighText Machine Language",
                "b": "HyperText Markup Language",
                "c": "HyperTool Markup Language",
                "d": "HomeText Makeup Language"
            },
            "answer": "b"
        }
    ]

    total_prize = 0

    for index, question in enumerate(questions):
        prize = (index + 1) * 100000

        is_correct = ask_question(
            question["question"],
            question["options"],
            question["answer"],
            prize
        )

        if not is_correct:
            print("\nGame Over! Better luck next time.")
            break

        total_prize = prize
        print(f"Your total winning: Rs. {total_prize:,}")

    else:
        print("\nCongratulations! Aapne saare questions sahi answer kiye! 🏆")

    print(f"\n{name}, aapki final winning amount: Rs. {total_prize:,}")


# Main program
print("========== WELCOME TO KBC ==========")

name = input("Apna naam enter karein: ").strip()

if not name:
    name = "Player"

welcome(name)
rules()

while True:
    choice = input("Kya aap game start karna chahte hain? (y/n): ")
    choice = choice.strip().lower()

    if choice == "y":
        question_bank()
        break
    elif choice == "n":
        print("KBC khelne ke liye dhanyavaad!")
        break
    else:
        print("Please sirf y ya n enter karein.")
