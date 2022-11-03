#  https://www.codingame.com/ide/puzzle/parse-sql-queries

import sys,math,string,copy

def is_number(s):
    """ Returns True is string is a number. """
    try:
        float(s)
        return True
    except ValueError:
        return False


sql='SELECT * FROM cats' # test 1
table='Name Breed'
rowList=['McFur Peterbald', 'Squeeky Bambino', 'Greta Laperm']

sql='SELECT Suburb, Regionname FROM Housing WHERE Rooms = 4 ORDER BY CouncilArea DESC' # test4
table='Suburb Rooms CouncilArea Regionname'
rowList=['Bulleen 3 Manningham EasternMetropolitan', 'Hawthorn 1 Boroondara SouthernMetropolitan', 'Hawthorn 3 Boroondara SouthernMetropolitan', 'Hawthorn 2 Boroondara SouthernMetropolitan', 'Hawthorn 4 Boroondara SouthernMetropolitan', 'Hawthorn 2 Boroondara SouthernMetropolitan', 'Healesville 3 YarraRanges NorthernVictoria', 'HeidelbergHeights 3 Banyule EasternMetropolitan', 'HeidelbergHeights 2 Banyule EasternMetropolitan', 'HeidelbergWest 3 Banyule EasternMetropolitan']

#sql='SELECT * FROM Fishmonger WHERE Environment = FreshWater ORDER BY Weight DESC'  #test3
#table='Name Environment Type Weight'
#rowList=['Prawns FreshWater ShellFish 0.25', 'Beluga SaltWater Caviar 1', 'Salmon FreshWater Fish 15', 'SeaBream SaltWater Fish 0.5', 'BlueFinTuna SaltWater Fish 600', 'Salmon SaltWater Fish 5', 'Trout FreshWater Fish 2', 'Lobster SaltWater ShellFish 6']


sqlList = sql.split(" ")
tableList= table.split(" ")
ergList=[]
bis = 0;order=0
whereList=[]
for i in range(len(sqlList)):
    if sqlList[i] == "FROM":
        bis = i
    if sqlList[i] == "ORDER":
        for j in range(len(tableList)):
            if tableList[j] == sqlList[i+2]:
                order = j
    if sqlList[i] == "WHERE":
        whereList.append(sqlList[i+1])
        whereList.append(sqlList[i+3])
print(whereList,file=sys.stderr)

rList=[]
for row in rowList:
    rList.append(row.split(" "))

if "ORDER" in sql:
    num=True
    for r in rList:
        if not is_number(r[order]):
            num = False

    if not num:
        if "DESC" in sql:
            rList = sorted(rList,key=lambda x: x[order] ,reverse=True)
        else:
            rList = sorted(rList,key=lambda x: x[order] ,reverse=False)
    else:
        if "DESC" in sql:
            rList = sorted(rList,key=lambda x: float(x[order]) ,reverse=True)
        else:
            rList = sorted(rList,key=lambda x: float(x[order]) ,reverse=False)
#print(rList,file=sys.stderr)


ueber=''
for row in rList:
    if sqlList[1] == "*":        
        ueber=table+" "
        where=False if len(whereList) > 0 else True
        if len(whereList) > 0:     
            for j in range(len(tableList)):               
                if tableList[j] == whereList[0]:
                    if whereList[1] == row[j]:
                        where = True
            if where:
                ergList.append(row)
        else:
            ergList.append(row)

    else:        
        ueber=''
        where=False if len(whereList) > 0 else True
        eList =[]
        for i in range(1,bis):            
            spalte = sqlList[i]
            spalte = spalte.replace(',','')
            ueber+=spalte+' '
            for j in range(len(tableList)):
                if tableList[j] == spalte:
                    eList.append(row[j])
                if len(whereList) > 0:                    
                    if tableList[j] == whereList[0]:
                        if whereList[1] == row[j]:
                            where = True
        if where:
            ergList.append(copy.deepcopy(eList))
print(ergList,file=sys.stderr)

print(ueber[:-1])
for erg in ergList:
    out = ""
    for e in erg:
        out+=e+" "
    print(out[:-1])
        