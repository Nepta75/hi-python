import random
import os

words = ['bonjour', 'table', 'ecran']
steps = [
  {
    'step': 1,
    'string': '______',
  },
  {
    'step': 2,
    'string': ' |\n |   \n |\n_|____',
  },
  {
    'step': 3,
    'string': '_____\n |\n |   \n |\n_|____',
  },
  {
    'step': 4,
    'string': '_____\n |   |\n |   \n |\n_|____',
  },
  {
    'step': 5,
    'string': '_____\n |   |\n |   O\n |\n_|____',
  },
  {
    'step': 6,
    'string': '_____\n |   |\n |  _O\n |\n_|____',
  },
  {
    'step': 7,
    'string': '_____\n |   |\n |  _O_\n |\n_|____',
  },
  {
    'step': 8,
    'string': '_____\n |   |\n |  _O_\n |   |\n_|____',
  },
  {
    'step': 9,
    'string': '_____\n |   |\n |  _O_\n |  _|\n_|____',
  },
  {
    'step': 10,
    'string': '_____\n |   |\n |  _O_\t ****** PERDU ******\n |  _|_\n_|____',
  }
]

def game():
  currentStep = 1
  word = random.choice(words)
  lettersFound = []
  win = False

  while win == False and currentStep != 10:
    wordString = ''
    os.system('clear')

    print("#####################################")
    print("############### PENDU ###############")
    print("#####################################")

    for step in steps:
      if currentStep == step.get('step'):
           print('\n\n' + step.get('string'))

    for i in range(0, len(word)):
      if any(word[i] in s for s in lettersFound):
        wordString += word[i] + ','
        if wordString.replace(',', '') == word:
          win = True
      else:
        wordString += '_,'

    if win == False:
      letterInput = ''
      print('\n\t ' + wordString + '\n')
      while (len(letterInput) != 1):
        letterInput = input('Saisissez une lettre: ')
      print('word: ' + word)
      if word.find(letterInput) != -1:
        lettersFound.append(letterInput)
      else:
        currentStep += 1
  
  os.system('clear')
  if win:
    print('Bravo, Vous avez gagné !')
  else:
    print('Dommage, Vous avez perdu !')

  response = input("Voulez-vous rejouez ? (y/no): ")
  if response == 'y' or response == 'yes' or response == 'oui':
    return game()

game()