hero=100
Monster=60

while Monster>0:
    action=int(input("Enter the action number\n 1-Attack the monster\n 2-Run away\n"))
    if action==1:
        Monster-=20
        print(f"hero{hero}hp")
        print(f"hero{Monster}hp")
        print(f"Attack the monster and his hp redused by 20 now the current {Monster}hp ")
    elif action==2:
        print(f"hero{hero}hp")
        print(f"hero{Monster}hp")
        print("you ascapped")
        break
    elif Monster<0:
        print(f"hero{hero}hp")
        print(f"hero{Monster}hp")
        print("you win")
    else:
        print("you enterd invalid input")