#  https://www.codingame.com/ide/puzzle/panel-count

import sys,math

#attriDict={'Gender': 0}
#personList=[['Leo', 'Male'], ['Samuel', 'Male'], ['Maya', 'Female'], ['Diane', 'Female'], ['Mael', 'Male']]
#formulaList=['Gender=Female']

attriDict={'Gender': 0, 'Age': 1, 'Town': 2}
personList=[['Nina', 'Female', '27', 'Nantes'], ['Mehdi', 'Male', '61', 'Marseille'], ['Marius', 'Male', '6', 'Lyon'], ['Felix', 'Male', '20', 'Paris'], ['Leonard', 'Male', '57', 'Strasbourg'], ['Lila', 'Female', '74', 'Montpellier'], ['Victor', 'Male', '7', 'Toulouse'], ['Capucine', 'Female', '82', 'Nantes'], ['Faustine', 'Female', '27', 'Lyon'], ['Yanis', 'Male', '55', 'Lyon'], ['Clara', 'Female', '43', 'Toulouse'], ['Melissa', 'Female', '91', 'Lyon']]
formulaList=['Gender=Male AND Town=Lyon']

attriDict={'Gender': 0, 'Age': 1, 'Town': 2}
personList=[['Gabin', 'Male', '78', 'Lyon'], ['Nicolas', 'Male', '54', 'Strasbourg'], ['Chloe', 'Female', '56', 'Bordeaux'], ['Hadrien', 'Male', '66', 'Strasbourg'], ['Leon', 'Male', '58', 'Lille'], ['Eden', 'Female', '91', 'Nantes'], ['Zoe', 'Female', '76', 'Montpellier'], ['Nicolas', 'Male', '54', 'Strasbourg'], ['Iris', 'Female', '19', 'Lille'], ['Pierre', 'Male', '79', 'Lille'], ['Louise', 'Female', '89', 'Marseille'], ['Eloise', 'Female', '10', 'Nice']]
formulaList=['Gender=Male AND Car=Audi', 'EyeColor=Blue AND Town=Nantes']

for formula in formulaList:
    ergList=[]
    fList = formula.split(" ")
    wertDict={}
    for f in fList:
        if "=" in f:
            attrib,wert=f.split("=")
            wertDict[attrib] = wert
    fehler=False
    for personL in personList:
        treffer=True
        for att, wert in wertDict.items():
            if not att in attriDict:
               fehler=True
               break
            pos = attriDict[att]
            if not personL[pos+1] == wert:
                treffer=False
        if treffer:
            ergList.append(personL)   
    if fehler:
        print(0)         
    else:
        print(len(ergList))

