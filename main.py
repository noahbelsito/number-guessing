import random 
random_number = random.randint(1,10)
guess = 0

while guess == 0:
     try:
          guess = int(input('Guess a number from 1 to 10: '))
     except ValueError:
          print('That is not a number') 
          
          
while guess != random_number:
     if (11 > guess > random_number):
          print('Too High!') 	
     elif (0 < guess < random_number):
          print('Too Low!')
     else:
          print('Not in range?')
     try:
          guess = int(input('Guess again: '))
     except ValueError:
          print('That is not a number.')
          continue 
          
          
print('Correct. Nice Guess!') 
