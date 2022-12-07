import sys,math

def getZeit(s,v):
    wert = s / v * 60
    #return round(wert,0)
    return wert

# v = strecke/zeit
# zeit = strecke/v

road_length=130   # 3
zoneList=['60 120']

road_length=150   # 6
zoneList=['30 120', '60 110', '90 120']

road_length=650  # 177
zoneList=['25 110', '26 60', '50 110', '80 60', '124 130', '125 110', '149 130', '150 90', '255 60', '358 130', '359 110', '387 90', '400 110', '425 130', '426 110', '478 90', '480 60', '514 90', '596 60', '605 130', '606 110', '620 90']


vorgabe=getZeit(road_length,130)
print(vorgabe,file=sys.stderr)
dauer,v0,s0,v1=0,130,0,0
for zone in zoneList:
    s1,v1 = [int(j) for j in zone.split()]
    dauer+=getZeit(s1-s0,v0)
    v0=v1;s0=s1
dauer+=getZeit(road_length-s0,v0)
print(dauer,file=sys.stderr)
print(int(dauer+0.5-vorgabe))
