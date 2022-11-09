
#  https://www.codingame.com/training/easy/hello-world

import sys,math

def umwandeln(wert):
    vorz = 1 if wert[0] in ['N','E'] else -1
    p = 3 if len(wert) == 8 else 2
    erg = float(wert[1:1+p])
    erg = erg + float(float(wert[p+1:p+3])/60)
    erg = erg + float(float(wert[p+3:p+5])/3600)
    erg = erg * vorz
    return erg

def entfernung(lat1,lon1,lat2,lon2):
    print("lat1,lon1: ",lat1,lon1)
   # dist = 6371 * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon2 - lon1))
   # return round(dist,0)
    R = 6371.0
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = round(R * c +.5,0)
    print("Result:", distance,file=sys.stderr)
    return distance


capList=[['Wien', 'N481200', 'E0162100'], ['Budapest', 'N472933', 'E0190305']]
mesList=['Servus, Welt!', 'Szia, Vilag!']
travList=[['N472059', 'E0183005'], ['N481330', 'E0172100']]

capList=[['Epidaurus', 'N373800', 'E0230800'], ['The_Globe_Theatre', 'N513025', 'W0000542'], ['Broadway', 'N404532', 'W0735906']]
mesList=['Chairete!', 'Haile to thee, Noble Master!', 'Hello, Dolly!']
travList=[['N373800', 'E0230800'], ['N513025', 'W0000542'], ['N404532', 'W0735906'], ['N450915', 'E0125549'], ['N505540', 'W0235856'], ['N522335', 'W0411458'], ['N450815', 'E0125649'], ['N451015', 'E0125449'], ['N512335', 'W0511458']]
travList=[['N450915', 'E0125549']]

capList=[['Joe_s_Place', 'S000000', 'E1790000'], ['Jack_s_Place', 'S000000', 'W1700000'], ['Laplace', 'N000000', 'E1790000']]
mesList=['Hello, I am Joe!', 'Hello, I am Jack!', 'Hello, I am Sorry!']
travList=[['N000000', 'W1753000'], ['N900000', 'E1790000'], ['N900000', 'W1700000'], ['S900000', 'W0123456'], ['N000000', 'E0043000'], ['N123456', 'E0043000'], ['S123456', 'E0123456']]
travList=[['N000000', 'W1753000']]

from geopy import distance
coords_1 = (52.2296756, 21.0122287)
coords_2 = (52.406374, 16.9251681)
print(distance.geodesic(coords_1, coords_2))



for trav in travList:
    ergS=9999999
    ergList=[]
    lat1=umwandeln(trav[0])
    lon1=umwandeln(trav[1])
    for i in range(len(capList)):
        cap = capList[i]
        lat2=umwandeln(cap[1])
        lon2=umwandeln(cap[2])
        dist = entfernung(lat1,lon1,lat2,lon2)
        if dist <= ergS:
            if dist < ergS:
                ergS=dist
                ergList.clear();ergList.append(i)
            else:
                ergList.append(i)

    out=""
    for erg in ergList:
        out = out + mesList[erg] + " "
    print(out[:-1])