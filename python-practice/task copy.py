import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the Rock Paper Scissors game")
#User input
User_input = input("Press 1 for rock, 2 for paper, or 3 for scissors ")
if User_input == "1":
    print(rock)
elif User_input == "2":
    print(paper)
elif User_input == "3":
    print(scissors)

#Computer

option = [rock, paper, scissors]
computer = (random.choice(option))
print(computer)

if User_input == "1" and computer == rock or User_input == "2" and computer == paper or User_input == "3" and computer == scissors:
     print("Draw")
elif User_input == "1" and computer == paper:
     print("Computer Won")
elif User_input == "1" and computer == scissors:
     print("You Won")
elif User_input == "2" and computer == rock:
     print("You Won")
elif User_input == "2" and computer == scissors:
     print("Computer Won")
elif User_input == "3" and computer == paper:
     print("You Won")
elif User_input == "3" and computer == rock:
     print("Computer Won")

