import sys
import math
from collections import namedtuple

def distance(x1,y1,x2,y2):
    return math.sqrt( ((x1-x2)**2)+((y1-y2)**2) )

x1=0;y1=0;x2=17630;y2=9000  # 1,9588
#gesamtlänge 19794
windrange=2200;baseRange=300
# 2200*3+300=6500   # windPos(0,0)=5750,2935   windPos(17630,9000) = 11800,6065
print(distance(x2,y2,11800,6065))


monsters = []
Entity = namedtuple('Entity', [
    'id', 'type','mZiel'
])
_entity = Entity(0,'test',"0")
monsters.append(_entity)
new = _entity._replace(mZiel="1")
print(new.mZiel)