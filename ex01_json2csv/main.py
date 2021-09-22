import os
import json

jsonPath = input("Entrez le nom du fichier avec comme extension .json: ")
nameOfCsvFile = input("Entrez le nom du nouveau fichier csv: ")
assert os.path.exists(jsonPath + '.json'), "Le fichier demandé n'a pas été trouvé"
jsonFile = open(jsonPath + '.json','r+')

csvList = json.loads(jsonFile.read())
csvTitles = ''
csvValues = ''
result = ''

for csvItem in csvList:
  csvKeysItem = csvItem.keys()
  csvValuesItem = csvItem.values()
  csvResultsItem = ''

  for title in csvKeysItem:
    if (csvTitles.find(title) == -1):
      csvTitles += title + ', '

  for value in csvValuesItem:
    csvResultsItem += '"' + str(value) + '"' + ', '

  csvValues += csvResultsItem + '\n'

result = csvTitles + '\n' + csvValues + '\n'

jsonFile.close()
csvFile = open(nameOfCsvFile + ".csv", "w")
csvFile.write(result)