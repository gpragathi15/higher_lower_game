from art import logo,vs
from game_data import data
import random
import os

# format account data into printable format
def format_data(account): 
  account_name=account["name"]
  account_descr=account["description"]
  account_country=account["country"]
  return f"{account_name} a {account_descr} from {account_country}"
def check_answer(guess,a_followers,b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
  #display art
print(logo)  
score=0
game_should_continue=True
# generate a random acc from the game data 
account_b=random.choice(data)
#make the game repeatable (use while loop)
while game_should_continue:

 #making B become the next A
  account_a=account_b
  account_b=random.choice(data)
  while account_a==account_b:
    account_b=random.choice(data)
  
  print(f"Compare A:{format_data(account_a)}.") 
  print(vs)
  print(f"Against B:{format_data(account_b)}.") 
    
  # ask user for a guess
  guess=input("Who has more followers? Type A or B:").lower()
  
  #check if the user is correct
  ##get follower count 
  a_follower_count=account_a["follower_count"]
  b_follower_count=account_b["follower_count"]
  is_correct=check_answer(guess, a_follower_count,b_follower_count)
  #clear screen after each round
  os.system('clear')
  print(logo)
  #feedback
  #score keeping
  if is_correct:
    score+=1
    print(f"You're right! Current score:{score}")
  else:
    game_should_continue=False
    print(f"Sorry, that's wrong Final score:{score}")


