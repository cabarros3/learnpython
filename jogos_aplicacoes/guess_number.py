# Project - Guess the number

import random

while True:

  print('.-.' * 15)
  print('Guess the number - The Game')
  print('.-.' * 15)

  user = int(input('Gues the number?\n --> '))
  computer = random.randint(1,10)

  if user == computer:
    print('Guess what?! You wan!!')
  else:
    print('So...You lose! Better luck next time, sis.')

  stop_guessing = str(input('>> Quit game?\n [s] press\n [n] press\n --> '))
  if 's' in stop_guessing:
    break
    
