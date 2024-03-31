# https://www.codingame.com/ide/puzzle/battle-of-heroes

import sys,math,copy


stack_1=['Minotaur', '20', '35', '10'];stack_2=['Unicorn', '16', '40', '14']


rest1,rest2=0,0
sieger=0
for i in range(1,10):
    print("Round {}".format(i))
    schaden1 = int(stack_1[1])*int(stack_1[3])
    kill1=int(schaden1//int(stack_2[2]))
    rest1+=schaden1 - int(stack_2[2])*kill1
    if rest1 >= int(stack_2[2]):
        kill1+=1
        rest1 = rest1 - int(stack_2[2])
    if kill1 > int(stack_2[1]):
        kill1 = int(stack_2[1])
    print("{} {}(s) attack(s) {} {}(s) dealing {} damage".format(stack_1[1],stack_1[0],stack_2[1],stack_2[0],schaden1))
    print("{} unit(s) perish".format(kill1))
    print("----------")
    stack_2[1] = str(int(stack_2[1])-kill1)
    if int(stack_2[1]) <= 0:
        sieger=1
        break

    schaden2 = int(stack_2[1])*int(stack_2[3])
    kill2=int(schaden2/int(stack_1[2]))
    rest2+=schaden2 - int(stack_1[2])*kill2
    if rest2 >= int(stack_1[2]):
        kill2+=1
        rest2 = rest2 - int(stack_1[2])
    if kill2 > int(stack_1[1]):
        kill2 = int(stack_1[1])
    print("{} {}(s) attack(s) {} {}(s) dealing {} damage".format(stack_2[1],stack_2[0],stack_1[1],stack_1[0],schaden2))
    print("{} unit(s) perish".format(kill2))
    print("##########")
    stack_1[1] = str(int(stack_1[1])-kill2)
    if int(stack_1[1]) <= 0:
        sieger=2
        break
if sieger == 1:
    print("{} won! {} unit(s) left".format(stack_1[0],stack_1[1]))
else:
    print("{} won! {} unit(s) left".format(stack_2[0],stack_2[1]))