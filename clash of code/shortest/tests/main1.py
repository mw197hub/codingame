
#input=6,4

#6import math;m=math.factorial;j=int;i=input;x=j(i());n=j(i());print(j(m(x)/m(x-n)))

#f=input
#x=int(f())
#a=1
#exec('a*=x;x-=1;'*int(f()))
#f(a)

import math

b=6
n=4

x=int(b)
a=1
#exec('a*=x;x-=1;'*int(n))
exec('a*=x;x-=1;'*n)
print(a)

print(int(math.factorial(b)/math.factorial(b-n)))
a=1;x=6
for _ in range(n):
    a*=x
    x-=1
print(a)

