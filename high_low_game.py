import random as rd
def high_low_game():
    user_score= 0
    com_score= 0
    while True:
        try:
            NUM_ROUNDS= int(input ("Enter number of rounds you want to play?"))
            break
        except ValueError:
            print("only integer is allowed.")
    for x in range (1, NUM_ROUNDS+1):
        print("\nwelcome to high-low number game.\n............................")
        print(f"Rounds left {NUM_ROUNDS}")
        user_num = rd.randint (1,100)
        com_num= rd.randint (1,100)
        print(f"user number is {user_num}")
        # print(f"computer number is {com_num}")
        while True:
            try:
                user_choice = input("guess whether user number is higher or lower than the computer's number. (higher/lower):").strip().lower()
                if user_choice not in ("higher", "lower"):
                    raise ValueError ("invalid input, only higher or lower is allowed.")
                else:
                    break
            except ValueError as err:
                print(err)
        if (user_choice =="higher" and user_num > com_num) or (user_choice =="lower" and user_num < com_num):
            print(f"congrats you have won this round. computer's number was {com_num}\n")
            user_score+=1
        elif user_num==com_num:
            print(f"you lost this round. computer's number was {com_num}\n")
            com_score+=1
        else:
            print(f"you lost this round. computer's number was {com_num}\n")
            com_score+=1
        NUM_ROUNDS-=1
    if user_score > com_score:
        print(f"Congratulations you have won this game.\nyour score= {user_score} and computer score= {com_score}")
    elif user_score==com_score:
        print(f"score tied")
    else:
        print(f"you have lost this game.\nyour score= {user_score} and computer score= {com_score}")
    print(f"Game over.......................")

high_low_game()