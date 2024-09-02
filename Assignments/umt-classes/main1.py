import math, random

print("Welcome to the High & Low game!")
print("--------------------------------")

# Generate random numbers between 1 and 100
user_number1 = random.randint(1, 100)
computer_number2 = random.randint(1, 100)

print("Your number is:", user_number1)
print("Guess whether your number is Higher or Lower than the computer's number.")

# User input
user_choice = input("Enter your choice (Higher/Lower): ").strip().lower()

# Compare user input with computer number
if user_choice == "higher":
    if user_number1 > computer_number2:
        print("Yes, you are right!")
    else:
        print("Sorry, you are wrong. The computer's number was:", computer_number2)
elif user_choice == "lower":
    if user_number1 < computer_number2:
        print("Yes, you are right!")
    else:
        print("Sorry, you are wrong. The computer's number was:", computer_number2)
else:
    print("Invalid choice. Please enter 'Higher' or 'Lower'.")


# import math, random
# print("Well come to High & Low game !")
# print("--------------------------------")

# #Generate random number 1-100
# user_number1 = random.randint(1,100)
# computer_number2 = random.randint(1,100)

# print( "your number is:", user_number1)
# print("Gess your number Higher or Lower then computer ?")

# #user input
# user_choice = input("Enter your choice,Higher/Lower:")

# #how to compare user input with computer input
# if (user_choice == "lower"):
#     if(user_number1 < computer_number2):
#         print(" yes you are Right")
#     else:
#         print("Sorry you are Wrong","computer number was", computer_number2)
        