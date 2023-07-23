#  https://www.codingame.com/ide/puzzle/crazy-list

import sys,math

testcases=[[1,4,7,10,13],[2,16,100,604,3628],[11,27,59,123,251,507,1019,2043,4091,8187],[129,2204,37479,637154],[5,-20,-70,-170],[2,-5,30,-145],[-1,2,-7,20],[5,5,5],[12,0,24,-24],[1,-1,1,-1],[7,8,8,8,8]]
validators=[[1,5,9,13,17],[3,24,171,1200,8403],[6,-7,84,-553]]

erg=0
for testcase in testcases:
    print(testcase,file=sys.stderr)
    if testcase[0] == testcase[1]:
        erg=testcase[0]
    else:
        x = testcase[-4]
        y = testcase[-3]
        z = testcase[-2]
        a = 0
        if not (y-x) == 0:
            a = (z - y) / (y - x)
        b = y - a * x
        erg = z * a + b

    print(int(erg))
    if int(erg) == testcase[-1]:
        print("richtig",file=sys.stderr)