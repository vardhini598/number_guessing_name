import random
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    score=0
    rounds=0
    while True:
        print("\nyou can choose any level")
        print("1. Easy (1 to 10)")
        print("2. medium (1 to 50)")
        print("3. Hard (1 to 100)")
        print("4. Exit Game")
        choice=input("Enter your choice(1/2/3/4): ")
        if choice=='4':
            print(f"\nThanks for playing!you played {rounds} round(s) and scored {score} points(s).")
            break
        if choice=='1':
            max_num=10
        elif choice=='2':
            max_num=50
        elif choice=='3':
            max_num=100
        else:
            print("invalid choice.try again.")
            continue
        secret_number=random.randint(1,max_num)
        attempts=0
        max_attempts=5
        print("I have picked a number between 1 and {max_num).you have {max_attempts} attempts to guess it.")
        while attempts<max_attempts:
            try:
                guess=int(input(f"Attempt {attempts+1}:Enter your guess:"))
                attempts+=1
                if guess==secret_number:
                    print("Congratulations!You guessed it right.")
                    score+=1
                    break
                elif guess < secret_number:
                    print("Too low!")
                else:
                        print("Too high!")
            except valueError:
                print("please enter a valid number.")
        else:
                    print(f"sorry!The corect number was {secret_number}.")
                    rounds+=1
                    print(f"Current Score:{score} | Rounds played: {rounds}\n")
number_guessing_game()