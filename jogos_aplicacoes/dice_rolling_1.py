import random
from time import sleep

# Project - Dice Rolling 1.0

while True:

  print('.-.' * 15)
  print('Dice Rolling - The Simulator')
  print('.-.' * 15)
  
  # iniciando o jogo
  init_game = int(input('>> play game? [0] press\n --> '))
  
  print('Rolling......')
  sleep(0.2)

  # rolando o dado
  dice = random.randint(1,6)
  
  #mostrando resultado
  print(f'The result is {dice}')
  
  # parando o jogo
  stop_rolling = int(input('Quit game?\n [9] press\n --> '))
  if stop_rolling == 9:
    break
