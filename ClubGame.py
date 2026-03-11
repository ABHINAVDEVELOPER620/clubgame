import random
def age_checker():
    user_age = int(input("enter your age:"))
    if user_age >= 18 :
        print("welcome to the club!")
        return True
    else:
        print("you are not allowed!")
        print("remember kid gambling is bad!")
        return False


def game_of_clubs():
        user_bet = int(input("enter amount to bet $ : "))
        computer_guess =random.randint(1,11)
        for attempts in range(1,11):
            user_guess = int(input("enter a number to be guesse (1-11): "))
            if user_bet < 0 :
                print("enter a vaild amount")
            else:
                print(f"you have placed {user_bet}$ amount to bet" )

                if computer_guess == user_guess :
                    print(f"you have won the money you recived {user_bet}$")
                    break
                elif user_guess < computer_guess:
                    print("higher!")
                    print(f"you have {10- attempts} tries left.")
                elif user_guess > computer_guess:
                    print("lower")
        else:
            print(f"Game over! the number was{computer_guess}")


if age_checker():
     game_of_clubs()
