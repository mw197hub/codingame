import sys
import math

gymnastsList=['Boris Shakhlin', 'Nadia Comaneci', 'Akinori Nakayama']
categoriesList=['beam', 'floor']
rowList=['Nikolai Andrianov,7.95,9.7,9', 'Nikolai Andrianov,8.94,8.3,9.29', 'Simone Biles,8.7,8.2,8.6', 'Boris Shakhlin,9.55,8.31,9.5', 'Boris Shakhlin,8.55,9.02,8.64', 'Aly Raisman,9.55,8.38,8.21', 'Aly Raisman,8.38,8.04,9.23', 'Takashi Ono,8.77,9.48,9.08', 'Takashi Ono,8.65,9.19,7.88', 'Nadia Comaneci,8.32,8.48,8.88', 'Nadia Comaneci,8.92,7.98,8.04', 'Sawao Kato,8.34,8.28,8.19', 'Sawao Kato,9.5,7.98,8.94', 'Laurie Hernandez,9.08,9.02,8.17', 'Viktor Chukarin,7.67,8.75,8.94', 'Laurie Hernandez,8.22,8.57,8.84', 'Alexei Nemov,9.27,9.38,7.98', 'Alexei Nemov,7.92,7.91,8.11', 'McKayla Maroney,9.32,8.48,8.97', 'McKayla Maroney,8.78,8.21,7.87', 'Viktor Chukarin,8.07,9.05,7.66', 'Katelyn Ohashi,8.03,7.63,9.15', 'Katelyn Ohashi,9.06,8.88,9.01', 'Akinori Nakayama,8.83,8.9,9.16', 'Akinori Nakayama,9.05,8.54,8.56', 'Shawn Johnson,8.95,8.11,8.07', 'Shawn Johnson,7.6,8.62,8.33', 'Simone Biles,8.62,9.56,8.72']


for g in gymnastsList:
    erg=[0,0,0];ergS=''
    for row in rowList:
        werte = row.split(",")
        if werte[0] == g:
            erg[0] = float(werte[1]) if float(werte[1]) > erg[0] else erg[0]
            erg[1] = float(werte[2]) if float(werte[2]) > erg[1] else erg[1]
            erg[2] = float(werte[3]) if float(werte[3]) > erg[2] else erg[2]
    for c in categoriesList:
        pos=0
        if c == "beam":
            pos =1
        if c == "floor":
            pos =2
        if erg[pos] == int(erg[pos]):
            ergS = ergS + str(int(erg[pos])) + ","
        else:
            ergS = ergS + str(erg[pos]) + ","
    print(ergS[:-1])