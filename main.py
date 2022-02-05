from art import logo , vs
from game_data import data
import random
from replit import clear

def format_data(account) :
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["description"]
  return f"{account_name}, a{account_descr}, from{account_country}"


def check_answer(guess, a_follower, b_follower) :
  if a_follower > b_follower  :
    if guess== "a" :
     return True
    else :
      return False 


account_b= random.choice(data)
is_guess= True
score= 0

while is_guess :
  print(logo)

  account_a= account_b
  account_b= random.choice(data)
 
  while account_a== account_b :
    account_b= random.choice(data)



  print(f"Compare A : {format_data(account_a)}")
  print(vs)
  print(f"Against B :{format_data(account_b)}")

  # Ask the user for a Guess 
  guess= input("Who has more followers ? 'A' or 'B' : ").lower()

  a_follower_count= account_a["follower_count"]
  b_follower_count= account_b["follower_count"]
  is_correct= check_answer(guess, a_follower_count,b_follower_count)

  clear()
  if is_correct :
    score +=1
    print(f"You're Right, Current Score : {score}")
  else :
    is_guess= False
    print(f"No, you're Wrong !, Your Score is : {score}")  


