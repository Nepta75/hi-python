import random
startNumber = input("Entre le premier nombre: ")
endNumber = input("Entre le deuxième nombre: ")

def game():
  numberOfTry = 0
  randomNumber = random.randrange(int(startNumber), int(endNumber))
  oddOrEven = 'pair' if (randomNumber % 2) == 0 else 'impair'
  lenNumber = len(str(randomNumber))
  win = False
  responseNumber = ''
  print('randomNumber: ', randomNumber)

  while win == False:
    if (len(responseNumber) > 0):
      if int(responseNumber) > randomNumber:
        print('indice: le nombre secret est plus petit que ' + responseNumber)
      else:
        print('indice: le nombre secret est plus grand que ' + responseNumber)
    else:
      print('indice: le nombre secret est composé de: ' + str(lenNumber) + ' chiffre(s), et il est: ' + oddOrEven)

    responseNumber = input("Quel est le nombre secret ?: ")
    numberOfTry += 1
    if int(responseNumber) == randomNumber:
      win = True

  if win == True:
    print("Success: Vous avez trouvé le nombre secret au bout de " + str(numberOfTry) + " tentative(s) !! :)")
    response = input("Voulez-vous rejouez ? (y/no): ")
    if response == 'y' or response == 'yes' or response == 'oui':
      return game()
    return
  return

game()