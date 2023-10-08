# https://ide.codingame.com/21609455?id=67159074dfed33eeaec99fa6e7420adaa0162c2

from json import dumps, loads
from typing import List
import sys,math,copy


file_contents=['Name=John;Age=15;Power=Telepathy\nName=Mary;Age=16;Power=Glows in the dark;Team=Basketball', 'Name=Adam;Age=17;Score=133;Power=Can turn anything into candy\nName=John;Score=283.5;City=NYC']
file_contents=['Name=BloodClaw;Age=14\nName=EchoBlade;Power=Geomorph\nName=FrostKinetic;Age=22;Test score=525.6\nName=ShadowShade;Power=Geomorph\nName=TempestSight;Age=17;Power=Biomimicry', 'Name=EchoBlade;Power=Geomorph;Test score=576.05\nName=EmberBreath;Age=18;Test score=310.78\nName=WhirlMaster;Age=21', 'Name=EclipseKinetic;Age=14;Power=Hydroblast;Test score=551.88\nName=EmberBreath;Test score=310.78\nName=TempestSight;Age=17;Power=Biomimicry;Test score=725.27']

#file_contents=["Test score=906.59;Name=ChronoThorn\nName=WarpHeart;Age=11;Power=Lightning Lash;Password=WWcYrqgory\nCity=New York;Name=AcidGlow;Test score=278.74;Power=Lightning Lash\nCity=Moscow;Password=zbfi@uO{Rf(kOYA;Power=Solar Flare;Name=VortexBolt;Age=16;Test score=623.27\nCity=Bangkok;Age=22;Name=RadiantFire;Test score=373.1;Power=Electroburst\nCity=Montevideo;Name=BloodSurge;Password=YR4pUq{RWU;Age=21;Power=Technopathy\nTest score=327.96;Name=TitanFire;City=Buenos Aires;Password=I|1e_kiUtjwxd6\nAge=22;Power=X-ray Vision;Name=BlazeBender\nTest score=560.51;Power=Shadowmeld;City=New Delhi;Name=BlazeBlade;Age=19","Password=I|1e_kiUtjwxd6;Age=18;Name=TitanFire\nPower=Shadowmeld;Name=BlazeBlade\nAge=22;Test score=373.1;Power=Electroburst;Name=RadiantFire\nName=BloodSurge;Test score=508.26\nPassword=-|yINm8EsGfr5j(#B;Name=SolarHeart\nName=VortexBolt;City=Moscow;Password=zbfi@uO{Rf(kOYA\nName=AcidGlow;Password=tV0wg:sTfdev","Test score=897.97;Password=WWcYrqgory;Name=WarpHeart","Name=WarpHeart;Power=Lightning Lash;City=Paris;Age=11;Password=WWcYrqgory\nName=TitanFire;Password=I|1e_kiUtjwxd6;Test score=327.96","Age=21;Name=BloodSurge;City=Montevideo;Test score=508.26;Password=YR4pUq{RWU\nAge=22;Password=MW5wN7)Y?P!/:M67L^_;Power=Thermokinesis;Name=ChronoThorn;Test score=906.59\nTest score=486.61;Name=BlazeBender;City=Sao Paulo;Age=22\nPower=Flight;Name=SolarHeart;Age=15;Password=-|yINm8EsGfr5j(#B\nName=WarpHeart;Test score=897.97;Power=Lightning Lash;City=Paris;Password=WWcYrqgory\nAge=19;Name=BlazeBlade;Test score=560.51;Power=Shadowmeld;City=New Delhi\nCity=Bangkok;Test score=373.1;Power=Electroburst;Name=RadiantFire\nAge=16;Password=zbfi@uO{Rf(kOYA;Power=Solar Flare;Test score=623.27;Name=VortexBolt;City=Moscow","Name=AcidGlow;Age=21;Password=tV0wg:sTfdev;Power=Lightning Lash;City=New York\nPower=Flight;Name=SolarHeart;City=Auckland;Password=-|yINm8EsGfr5j(#B;Test score=488.76\nAge=21;City=Montevideo;Password=YR4pUq{RWU;Name=BloodSurge;Test score=508.26\nCity=Sao Paulo;Test score=486.61;Power=X-ray Vision;Age=22;Password=xO9FD/_(/{0FA?:;Name=BlazeBender\nPassword=zbfi@uO{Rf(kOYA;Age=16;Name=VortexBolt;Power=Solar Flare;Test score=623.27;City=Moscow\nAge=22;Test score=906.59;Power=Thermokinesis;Name=ChronoThorn;City=Kuala Lumpur\nTest score=897.97;Power=Lightning Lash;Age=11;Password=WWcYrqgory;Name=WarpHeart;City=Paris","City=Moscow;Name=VortexBolt;Age=16;Password=zbfi@uO{Rf(kOYA;Power=Solar Flare;Test score=623.27\nCity=New Delhi;Name=BlazeBlade;Age=19;Test score=560.51;Password=rcHck::W:_v51\nPower=Energy Absorption;Name=TitanFire;City=Buenos Aires;Test score=327.96;Age=18;Password=I|1e_kiUtjwxd6\nPassword=-|yINm8EsGfr5j(#B;City=Auckland;Test score=488.76;Name=SolarHeart;Age=15;Power=Flight\nName=BloodSurge;Test score=508.26;Password=YR4pUq{RWU;Age=21;Power=Technopathy\nPower=Lightning Lash;City=New York;Password=tV0wg:sTfdev;Age=21;Name=AcidGlow;Test score=278.74","Name=TitanFire;Power=Energy Absorption\nName=WarpHeart;Test score=897.97;Password=WWcYrqgory;City=Paris\nCity=Montevideo;Name=BloodSurge;Test score=508.26","City=New Delhi;Test score=560.51;Name=BlazeBlade\nName=BloodSurge;Power=Technopathy;City=Montevideo;Age=21\nCity=New York;Power=Lightning Lash;Name=AcidGlow;Test score=278.74\nTest score=327.96;City=Buenos Aires;Password=I|1e_kiUtjwxd6;Name=TitanFire\nTest score=906.59;Name=ChronoThorn\nAge=22;Name=RadiantFire;Password=v(aV{yYmtaLg;Power=Electroburst","Name=BlazeBlade;City=New Delhi\nName=SolarHeart;Test score=488.76;City=Auckland;Age=15\nAge=16;Power=Solar Flare;Name=VortexBolt;Password=zbfi@uO{Rf(kOYA\nPower=Lightning Lash;Name=WarpHeart;City=Paris;Test score=897.97\nPower=Technopathy;Name=BloodSurge"]


nameDict={}
name=""

for fileC in file_contents:
    file = fileC.split("\n")    
    #print(file,file=sys.stderr)
   
    for f in file:
        wertDict = {}
        teil = f.split(";")        
        for t1 in teil:
            t2 = t1.split("=")
            if t2[0] == "Name":
                name = t2[1]
                if t2[1] in nameDict:
                    wertDict = nameDict[t2[1]]
        for t1 in teil:
            t2 = t1.split("=")
            if t2[0] == "Name":
                a=0
            else:
                wertDict[t2[0]] = t2[1]
        nameDict[name] = copy.deepcopy(wertDict)
erg=""
for name in sorted(nameDict):
    wertD = nameDict[name]
    erg=erg+"Name="+name+";"
    for w in sorted(wertD):
        wert=wertD[w]
        erg=erg+w+"="+wert+";"
    #print("{}   {}".format(name,wertD))    
    erg=erg[:-1]+"\n"
print(erg[:-1])