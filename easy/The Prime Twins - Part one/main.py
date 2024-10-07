# https://www.codingame.com/ide/puzzle/the-prime-twins---part-one

import sys,math



####

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False 
  return True

n=4

first=0;second=0
for i in range(n+1,110002):
  if is_prime(i):
    if first == 0:
      first = i
    else:
      
      if i - first == 2:
        second=i
        break
      else:
        first = i
print("{} {}".format(first,second))