#  https://www.codingame.com/ide/puzzle/library-dependencies

import sys,math,copy


def setGraph(impList,dependList):
    graph={};bisher=[]
    for im in impList:
        wertL = im.split(" ")
        graph[wertL[1]] = []
    for depend in dependList:
        wertList = depend.split(" ")
        reqList=[]
        for i in range(2,len(wertList)):
            reqList.append(wertList[i].replace(",",""))
        for req in reqList:
            graph[wertList[0]].append(req)
    return graph

def setPruefung(graph,impList,dependList):
    bisherList=[]
    for imp in impList:
        wertL = imp.split(" ")
        reqList = graph[wertL[1]]
        for req in reqList:
            if not req in bisherList:
                return False,req,wertL[1]
        bisherList.append(wertL[1])
    return True,"",""

def setUmstellen(impList,dependList,graph):   
    ergList=[];iList=[]
    for imp in impList:
        wertL = imp.split(" ")
        iList.append(wertL[1])
    #print(sorted(iList),file=sys.stderr)
    print(graph['CC'],file=sys.stderr)
    print(graph['CR'],file=sys.stderr)

    restDict={}
    for imp in sorted(iList):
        if len(graph[imp]) > 0:
            reqList = graph[imp]
            rest=[]
            for req in reqList:
                if not req in ergList:
                    rest.append(req)
            if len(rest) > 0:
                restDict[imp] = rest[:]
            else:
                ergList.append(imp)
        else:
            ergList.append(imp)

        wiederholen=True
        while wiederholen:
            ersatzDict={};wiederholen=False;eList=[]
            for im in sorted(restDict):
                reqList = restDict[im]
                rest=[]
                for req in reqList:
                    if not req in ergList:
                        rest.append(req)
                if len(rest) > 0 or wiederholen:
                    ersatzDict[im] = rest[:]
                else:                
                    eList.append(im)
                    wiederholen=True
                    #break
            restDict = copy.deepcopy(ersatzDict)
            if "CR" in eList or "CC" in eList:
                a=0
            for e in sorted(eList):
                ergList.append(e)
    if len(restDict) > 0:
        return False,[]
    return True,ergList

#4
impList=['import F', 'import A', 'import B', 'import C', 'import E', 'import D']
dependList=['B requires E', 'C requires A']
#2
impList=['import A', 'import B', 'import C']
dependList=['B requires A', 'C requires B', 'A requires C']
#1
#impList=['import A', 'import B', 'import C']
#dependList=['B requires A', 'C requires B']
#8
#impList=['import collections', 'import os', 'import random', 'import requests', 'import math', 'import builtins', 'import sys', 'import contextlib', 'import inspect', 'import functools', 'import itertools', 'import numpy', 'import time', 'import unittest', 'import pandas']
#dependList=['math requires requests', 'inspect requires contextlib, os', 'time requires collections, sys', 'contextlib requires sys, os', 'numpy requires os, requests, itertools', 'pandas requires unittest', 'itertools requires random, inspect, contextlib', 'functools requires inspect', 'builtins requires math', 'unittest requires contextlib']
#6
impList=['import requests', 'import itertools', 'import random', 'import functools', 'import inspect', 'import sys', 'import collections', 'import builtins', 'import pandas', 'import unittest', 'import contextlib', 'import os', 'import time', 'import math', 'import numpy']
dependList=['math requires requests', 'inspect requires contextlib, os', 'time requires collections, sys', 'contextlib requires sys, os', 'numpy requires os, requests, itertools', 'pandas requires unittest', 'itertools requires random, inspect, contextlib', 'functools requires inspect', 'builtins requires math', 'unittest requires contextlib']
#7
#impList=['import requests', 'import itertools', 'import random', 'import functools', 'import inspect', 'import sys', 'import collections', 'import builtins', 'import pandas', 'import unittest', 'import contextlib', 'import os', 'import time', 'import math', 'import numpy']
#dependList=['math requires requests', 'inspect requires contextlib, os', 'time requires collections, sys', 'contextlib requires sys, os', 'numpy requires os, requests, itertools', 'pandas requires unittest', 'itertools requires random, inspect, contextlib', 'functools requires inspect', 'builtins requires math', 'unittest requires contextlib']
#10
impList=['import BV', 'import BE', 'import Q', 'import X', 'import CW', 'import DF', 'import BJ', 'import H', 'import CS', 'import BS', 'import BG', 'import BW', 'import D', 'import CF', 'import U', 'import DD', 'import CC', 'import BO', 'import BR', 'import BY', 'import CJ', 'import F', 'import DH', 'import R', 'import CT', 'import BH', 'import CX', 'import CY', 'import BM', 'import DC', 'import DM', 'import BU', 'import CN', 'import DA', 'import M', 'import O', 'import BF', 'import CU', 'import CQ', 'import CE', 'import BK', 'import DK', 'import V', 'import CA', 'import BX', 'import CH', 'import W', 'import CI', 'import C', 'import CZ', 'import K', 'import CV', 'import CK', 'import S', 'import BI', 'import CR', 'import BA', 'import J', 'import DJ', 'import L', 'import DB', 'import BP', 'import N', 'import CD', 'import BT', 'import CM', 'import BQ', 'import I', 'import Z', 'import E', 'import DO', 'import B', 'import CL', 'import DL', 'import G', 'import P', 'import BB', 'import DI', 'import BN', 'import CG', 'import DE', 'import Y', 'import BD', 'import DG', 'import CP', 'import T', 'import DN', 'import CB', 'import BC', 'import BZ', 'import BL', 'import A', 'import CO']
dependList=['A requires BW, Z, CA', 'B requires BD', 'C requires DD, BM, CL', 'D requires CV, DJ, BD', 'G requires BO', 'H requires B', 'I requires DC, F, BH', 'J requires DI, A', 'K requires DB, E, CY', 'L requires CM', 'M requires DD, BT, DL', 'O requires DM, Q', 'P requires L, BD, BT', 'Q requires L, CU, CO', 'R requires BI, CW', 'S requires DK, BN', 'T requires BI, F, CC', 'U requires BH, T, BZ', 'V requires DI, Q', 'W requires BT, CT, DB', 'X requires CD, BO, BM', 'Z requires BY, CS', 'BA requires BB', 'BB requires CH, L', 'BC requires CO, BV', 'BG requires CI, CA', 'BH requires DG, BB', 'BI requires BJ', 'BJ requires CK, BH, CQ', 'BK requires BW, CI, DL', 'BL requires Y, DE', 'BN requires DF, CI, Y', 'BO requires CE', 'BP requires CI', 'BQ requires CA, CT', 'BS requires CU', 'BU requires BR, Z, CD', 'CA requires E, BZ', 'CB requires BD, E, Q', 'CC requires CM', 'CD requires BH, A', 'CF requires DO, BJ', 'CG requires O, BX, BO', 'CH requires J', 'CL requires BA, Z, D', 'CM requires DD, DE, CJ', 'CN requires BH', 'CO requires BR', 'CQ requires O', 'CR requires BV, DE, DA', 'CT requires Z', 'CU requires BV', 'CV requires DM', 'CW requires CA', 'CY requires DI, BX, Z', 'CZ requires DO, CU, F', 'DB requires BU, CZ, R', 'DD requires BZ', 'DE requires N, CW', 'DF requires M, BF', 'DG requires CU, DK, DM', 'DH requires DN, BK', 'DI requires Z', 'DJ requires CF, W', 'DK requires F, CE, BE', 'DO requires CQ']



###############
graph=setGraph(impList,dependList)
print(graph,file=sys.stderr)
pruefung,nach,vor = setPruefung(graph,impList,dependList)
if pruefung:
    print("Compiled successfully!")
else:
    print("Import error: tried to import {} but {} is required.".format(vor,nach))
    umstellen,ergList = setUmstellen(impList,dependList,graph)
    if umstellen:
        print("Suggest to change import order:")
        for erg in ergList:
            print("import "+erg)
    else:
        print("Fatal error: interdependencies.")
