import math, random
from typing import List, Dict

def display_menu():
    print("--------------------------------")
    print (" Well come to High Low game")
    print("--------------------------------\n")

def generate_numbers() -> List[int]:
    user_number1 = random.randint(1, 100)
    computer_number2 = random.randint(1, 100)
    return [user_number1, computer_number2]

def is_Greater(number1 : int, number2 : int) -> bool:
    if (number1 > number2):
        return True
    else:
        return False
    
points = 0


def user_choice (choice : str, user_num : int, computer_num : int):
    global points
    if (choice == "lower"):
        answer = is_Greater(number1 = computer_num, number2 = user_num)
        if (answer):
            print ( "Yes you are right")
            points +=1
            print ("Score:", points)
        else:
            print ( " Sorry you are Wrong")
            print ( "Score:", points)
    elif (user_choice == "higher"):
        answer = is_Greater(number1 = user_num, number2 = computer_num)
        if (answer):
            print ( "Yes you are right")
            points +=1
            print ("Score:", points)
        else:
            print ( "Sorry you are Wrong")
            print ("Score:", points)
