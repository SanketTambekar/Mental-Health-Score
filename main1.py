#Display art
from pyq.data_main import data
import random
#genarating a random account from the game data
score=0

##repeating the game till it is false
game_is_continue=True
account_b=random.choice(data)

while game_is_continue:
    def format_data(account):
         account_user=account['name']
         account_descr=account['description']
         account_country=account['country']
         return f"{account_user} {account_descr} {account_country}"

    def check_answer(user_guess,a_follower,b_follower):
        """"take a user guess and check for the follower counts and return the if it is correct or wrong"""
        if a_follower>b_follower:
            return user_guess=='a'
        else:
            return user_guess=='b'

    #generating the random account from the data
    account_a=account_b
    account_b=random.choice(data)

    ##check if the user account b as the same account as b
    if account_a==account_b:
        account_b=random.choice(data)

    print(f"Account A:{format_data(account_a)}")
    print("vs")
    print(f"Account B:{format_data(account_b)}")

    ##asking for the guess
    guess=input("Who has the more follower Type 'A' or 'B':").lower()

##cleaning the screen
    # print("\n"*10)


    a_follower_count=account_a['follower_count']
    b_follower_count=account_b['follower_count']

    is_correct=check_answer(guess,a_follower_count,b_follower_count)


    ##checking if the answer is correct

    if is_correct:
        score+=1
        print(f"you guessed the correct answer!!!and your score is {score}")
    else:
        print(f"you have guessed the wrong answer and your score is {score}")
        game_is_continue=False
# #format the ccount data into printable format
# print(f"{account_a}  vs {account_b}")
# if account_a['follower_count']>account_b['follower_count']:
#     print(f"A has has more follwer B")
# else:
#     print(f"B has  more follwer than A ")
# print(account_a['follower_count'])
# check user for a guess


