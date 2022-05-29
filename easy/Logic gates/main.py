import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
posL={'--':0,'__':1,'-_':2,'_-':3}
outL ={'AND':['-','_','_','_'],'OR':['-','_','-','-'],'XOR':['_','_','-','-'],'NAND':['_','-','-','-'],'NOR':['_','-','_','_'],'NXOR':['-','-','_','_']}

inputL={}
lenSignal=0
n = int(input())
m = int(input())
for i in range(n):
    input_name, input_signal = input().split()
    inputL[input_name] = input_signal
    lenSignal=len(input_signal)
print(inputL,file=sys.stderr)

for i in range(m):
    output_name, _type, input_name_1, input_name_2 = input().split()
    outputString=""
    line1 = inputL[input_name_1]
    line2 = inputL[input_name_2]
    out = outL[_type]
    for m in range(lenSignal):
        sig = line1[m]+line2[m]
        outputString = outputString + out[posL[sig]]
    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    print(output_name+" "+outputString )
