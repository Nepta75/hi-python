import random

rpsValues = {
  'pierre': 'papier',
  'papier': 'ciseau',
  'ciseau': 'pierre',
}

def isWin(rpsNamePlayer, rpsNameBot):
  win = 'perdu'
  
  if rpsNamePlayer == rpsNameBot:
    win = 'null'
    return win

  if rpsValues.get(rpsNamePlayer) != rpsNameBot:
    win = 'gagné'
  return win

def game():
  rpsNameBot = ''
  rpsNames = ''
  rpsNamePlayer = ''

  for rpsValue in list(rpsValues):
    rpsNames += (',' if len(rpsNames) > 0 else '') + rpsValue

  while (
    (rpsNamePlayer != list(rpsValues)[0]) and
    (rpsNamePlayer != list(rpsValues)[1]) and
    (rpsNamePlayer != list(rpsValues)[2])
  ): rpsNamePlayer = input("Taper une des trois options: " + rpsNames + ": ")

  rpsNameBot = random.choice(list(rpsValues))

  print("Ordinateur a joué: " + rpsNameBot)
  print("Vous avez joué: " + rpsNamePlayer)

  if (isWin(rpsNamePlayer, rpsNameBot) == 'gagné'):
    print("Success: Vous avez gagné contre l'ordinateur !")
  elif (isWin(rpsNamePlayer, rpsNameBot) == 'null'):
    print("Dommage: Vous avez fait match null avec l'ordinateur !")
  elif (isWin(rpsNamePlayer, rpsNameBot) == 'perdu'):
    print("Sorry: Vous avez perdu contre l'ordinateur !")

  response = input("Voulez-vous rejouez ? (y/no): ")
  if response == 'y' or response == 'yes' or response == 'oui':
    return game()
  return

game()