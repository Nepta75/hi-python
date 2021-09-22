import os
import json

iniPath = input("Entrez le nom du fichier avec comme extension .ini: ")
nameOfJsonFile = input("Entrez le nom du nouveau fichier json: ")
assert os.path.exists(iniPath + '.ini'), "Le fichier demandé n'a pas été trouvé"
iniFile = open(iniPath + '.ini','r+')

Lines = iniFile.readlines()

jsonContent = {}
currentSectionData = {}
currentSectionTitle = ''

for line in Lines:
  lineFormated = line.strip().replace('\n',"")

  if (lineFormated.startswith('[') and lineFormated.endswith(']')):
    currentSectionTitle = lineFormated.replace('[', '')
    currentSectionTitle = currentSectionTitle.replace(']', '').lower()
    currentSectionData = {}

  if (lineFormated.startswith('#') == False and lineFormated.startswith('[') == False):
      lineSplited = lineFormated.split('=')
      if (len(lineSplited) == 2):
        currentSectionData[lineSplited[0]] = lineSplited[1]

  if (currentSectionData and currentSectionTitle):
    jsonContent[currentSectionTitle] = currentSectionData

iniFile.close()
jsonFile = open(nameOfJsonFile + ".json", "w")
json.dump(jsonContent, jsonFile, sort_keys=True, indent='\t', separators=(',', ': '))