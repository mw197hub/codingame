import sys
import math

#  #=1, *=0
# test='#*######*#*'
# res = ''.join(format(ord(i), '08b') for i in test)  

time='#*######*#*'
addressList=['mayjul', 'sepsep', 'octapr', 'octsep', 'sepjun', 'octjan']

#time='##*#**#**'
#addressList=['maysep', 'mayfeb', 'marsep', 'junoct', 'octjan', 'marsep', 'jundec', 'sepsep', 'octapr', 'octjul', 'sepjul', 'sepfeb', 'marsep', 'junoct', 'octjan', 'marsep', 'augjan', 'octapr', 'sepaug', 'sepfeb', 'octjul', 'sepjun', 'novfeb', 'sepfeb', 'marsep', 'juldec', 'octsep', 'aprnov', 'marsep', 'julnov', 'sepfeb', 'octfeb', 'octjan', 'marsep', 'juldec', 'octsep', 'sepfeb', 'octsep', 'sepoct', 'octapr', 'octmar']


time = time.replace("#",'1')
time = time.replace("*",'0')
#print(time,file=sys.stderr)
zeit = "0000" + str(int(time,2))
print(zeit[-4:-2]+':'+zeit[-2:])


monDict={'jan':'0','feb':'1','mar':'2','apr':'3','may':'4','jun':'5','jul':'6','aug':'7','sep':'8','oct':'9','nov':'10','dec':'11'}

erg=""
for address in addressList:
    #wert = monDict[address[0:3]]+monDict[address[3:6]]
    #base = int(wert,12)

    base = int(monDict[address[0:3]]) * 12 + int(monDict[address[3:6]])
    erg += chr(base)
    print(address,file=sys.stderr,end="   # ")
    print(wert,file=sys.stderr,end="  # ")
    print(base,file=sys.stderr,end=" : ")
    print(erg,file=sys.stderr)
print(erg)

#print(chr(117))