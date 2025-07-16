import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])
user_choice = input('What path do you want to take rock, paper, scissors?\n')

print('computers choice is:', computer_choice)

if computer_choice == user_choice:
     print('ITS A TIE!!')

elif user_choice == 'paper' and computer_choice == 'rock':
        print('YOU WIN!!')

elif user_choice == 'rock' and computer_choice == 'scissors':
        print('YOU WIN!!')

elif user_choice == 'scissors' and computer_choice == 'Paper':  
        print('YOU WIN!!')
else:
   print('YOU LOSE, COMPUTER WINS:)')