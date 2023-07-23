#  https://www.codingame.com/ide/puzzle/the-alien-business-of-cows

import sys,math

def degToDec(deg):
    dec=0
    pos1=deg.find("°")
    pos2=deg.find("'")
    pos3=deg.find("\"")
    factor=-1
    if deg[pos3+1] == "N" or deg[pos3+1] == "E":
        factor=1
   # print(deg[pos2+1:pos3],file=sys.stderr)
    dec=factor*(float(deg[0:pos1])+float(deg[pos1+1:pos2])/60+float(deg[pos2+1:pos3])/3600)
    return dec



missionList=['Boadwine Farms Inc (South Dakota, USA) 43°44\'41.7"N 96°49\'37.4"W 496', 'George Farms (Wyoming, USA) 44°38\'39.1"N 108°58\'19.0"W 1467', 'Coronado Dairy (Arizona, USA) 32°01\'35.6"N 109°45\'44.3"W 1289', 'Peaceful Hills Farm (Missouri, USA) 39°04\'39.6"N 94°11\'49.5"W 282', 'Grotegut Dairy Farm Inc (Wisconsin, USA) 43°59\'33.9"N 87°45\'19.2"W 227', 'Crooked Creek Farm Dairy (Michigan, USA) 42°51\'18.8"N 82°59\'26.4"W 237', 'MVP Dairy, LLC (Ohio, USA) 40°37\'28.0"N 84°31\'41.0"W 253', 'The Family Cow (Pennsylvania, USA) 39°58\'02.7"N 77°34\'26.9"W 213', 'Kleinpeter Farms Dairy LLC (Louisiana, USA) 30°21\'47.1"N 91°01\'21.1"W 8', 'Working Cows Dairy (Alabama, USA) 31°11\'14.2"N 85°36\'06.3"W 83', 'Happy Cow Creamery (South Carolina, USA) 34°36\'51.1"N 82°21\'13.1"W 249']
missionList=['Boadwine Farms Inc (South Dakota, USA) 43°44\'41.7"N 96°49\'37.4"W 496']

shipList=[["VaCoWM Cleaner",44.7,0.8,3,0,0],["L4nd MoWer",22.38,1.2,10,5,0],["Cow Harvester",11.19,1.5,20,13,0]]
collectorAbAltitude=0.5
missileLat=degToDec("34°45'21.8\"N")
missileLon=degToDec("120°37'34.8\"W")
missileAlt=0.046
missileMaxalt=160
missileSpeed=6
g=9.81
PI=3.14159265359

moeglich=False
for mission in missionList:
    location=mission[0:mission.find(")")+1]    
    rest=mission[mission.find(")")+2:]
    p1=rest.find(" ")
    deg1=rest[0:p1]
    p2=rest[p1+1:].find(" ")
    deg2=rest[p1+1:p2+p1+1]
    collectorAltitude=float(rest[p2+p1+2:])/1000+collectorAbAltitude
    lat=degToDec(deg1)
    lon=degToDec(deg2)
   # print(dist,file=sys.stderr)
    dLat=(missileLat-lat)*111.11
    dLon=(missileLon-lon)*111.11*math.cos((lat+missileLat)/2*PI/180)
    distance=math.sqrt(dLat*dLat+dLon*dLon+(missileMaxalt-missileAlt)*(missileMaxalt-missileAlt))
    missileImpactTime=distance/missileSpeed
    name="";cows=0
    for ship in shipList:
        ship[5]=0
        abductionTime=collectorAbAltitude*1000/(g*ship[2])
        collectTime=missileImpactTime-(missileMaxalt-collectorAltitude)/ship[1]
        while collectTime-abductionTime>0:
            ship[5]=ship[5]+1
            collectTime=collectTime-abductionTime
        if ship[5] > ship[4]:
            moeglich=True
            name=ship[0]
            if ship[5] > ship[3]:
                cows=ship[3]
            else:
                cows=ship[5]

    if moeglich:
        print("{}: possible. Send a {} to bring back {} cows.".format(location,name,cows))
    else:
        print("{}: imposible.".format(location))