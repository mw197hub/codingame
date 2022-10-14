import sys
import math

playList=[['31', 'PLAIN', '30'], ['18', 'PLAIN', '35'], ['14', 'PLAIN', '32'], ['25', 'ODD'], ['13', 'PLAIN', '9'], ['14', 'PLAIN', '34'], ['32', 'ODD'], ['26', 'PLAIN', '9'], ['29', 'EVEN'], ['7', 'PLAIN', '21'], ['32', 'PLAIN', '29'], ['0', 'PLAIN', '7'], ['7', 'PLAIN', '34'], ['13', 'PLAIN', '14'], ['22', 'PLAIN', '8'], ['25', 'PLAIN', '28'], ['11', 'PLAIN', '20'], ['14', 'ODD'], ['23', 'ODD'], ['13', 'PLAIN', '22'], ['2', 'ODD'], ['23', 'EVEN'], ['17', 'ODD'], ['30', 'EVEN'], ['28', 'PLAIN', '28'], ['5', 'PLAIN', '36'], ['13', 'EVEN'], ['22', 'PLAIN', '11'], ['5', 'EVEN'], ['32', 'PLAIN', '25'], ['13', 'ODD'], ['10', 'EVEN'], ['28', 'ODD'], ['15', 'PLAIN', '2'], ['33', 'EVEN'], ['29', 'ODD'], ['1', 'EVEN'], ['19', 'PLAIN', '12'], ['0', 'PLAIN', '34'], ['24', 'EVEN'], ['16', 'PLAIN', '36'], ['4', 'EVEN'], ['35', 'PLAIN', '13'], ['14', 'PLAIN', '34'], ['30', 'ODD'], ['13', 'EVEN'], ['29', 'ODD'], ['7', 'EVEN'], ['18', 'PLAIN', '20'], ['33', 'ODD'], ['24', 'PLAIN', '28'], ['34', 'PLAIN', '34'], ['33', 'EVEN'], ['32', 'EVEN'], ['10', 'EVEN'], ['13', 'ODD'], ['35', 'PLAIN', '26']]

rounds = 57
cash = 70545  #1 = 1153

playList=[['27', 'PLAIN', '30'], ['22', 'PLAIN', '36'], ['7', 'PLAIN', '23'], ['18', 'ODD'], ['18', 'PLAIN', '8'], ['17', 'PLAIN', '35'], ['36', 'ODD'], ['32', 'PLAIN', '9'], ['31', 'EVEN'], ['9', 'PLAIN', '14'], ['36', 'PLAIN', '33'], ['2', 'PLAIN', '11'], ['11', 'PLAIN', '11'], ['12', 'EVEN'], ['17', 'ODD'], ['7', 'PLAIN', '22'], ['28', 'PLAIN', '9'], ['12', 'PLAIN', '16'], ['5', 'EVEN'], ['15', 'PLAIN', '15'], ['7', 'EVEN'], ['3', 'EVEN'], ['30', 'EVEN'], ['3', 'EVEN'], ['27', 'ODD'], ['33', 'PLAIN', '4'], ['4', 'PLAIN', '15'], ['30', 'ODD'], ['11', 'ODD'], ['26', 'EVEN'], ['4', 'ODD'], ['5', 'PLAIN', '15'], ['0', 'EVEN'], ['24', 'PLAIN', '13'], ['31', 'PLAIN', '1'], ['28', 'EVEN'], ['4', 'PLAIN', '24'], ['23', 'PLAIN', '2'], ['29', 'EVEN'], ['0', 'EVEN'], ['32', 'PLAIN', '9'], ['26', 'PLAIN', '14'], ['29', 'ODD'], ['9', 'PLAIN', '9'], ['2', 'EVEN'], ['32', 'PLAIN', '30'], ['28', 'ODD'], ['2', 'ODD'], ['19', 'PLAIN', '12'], ['25', 'ODD'], ['19', 'PLAIN', '35'], ['31', 'ODD'], ['3', 'EVEN'], ['35', 'EVEN'], ['25', 'PLAIN', '31'], ['18', 'PLAIN', '18'], ['11', 'ODD'], ['27', 'PLAIN', '35'], ['14', 'PLAIN', '3'], ['32', 'PLAIN', '0'], ['6', 'EVEN'], ['24', 'PLAIN', '23'], ['7', 'PLAIN', '7'], ['22', 'PLAIN', '0'], ['13', 'PLAIN', '13'], ['12', 'PLAIN', '3'], ['6', 'PLAIN', '21'], ['9', 'PLAIN', '11'], ['14', 'ODD'], ['26', 'EVEN'], ['15', 'EVEN'], ['7', 'PLAIN', '20'], ['11', 'PLAIN', '10']]
rounds=73  #4 = 359412
cash=77041

for i in range(rounds):
    plays = playList[i]
    einsatz=int(cash/4+0.99)
    erg=0
    if plays[1] == "ODD":
        if int(plays[0])%2:
            erg = einsatz * 2
    elif plays[1] == "EVEN":
        if not int(plays[0])%2:
            if int(plays[0]) == 0:
                a = 0
            else:
                erg = einsatz * 2
    else:
        if plays[0] == plays[2]:
            erg = einsatz * 36
    cash = cash - einsatz + erg
#    print(cash,file=sys.stderr)
print(playList,file=sys.stderr)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(cash)