r=input
p=print;t=int
a,b,c,d,e,f,g,h=[int(i) for i in r().split()]
l={d:e}
for i in range(h):
 m,n=r().split();l[t(m)]=t(n)
while True:
 q = r().split();x=int(q[0]);y=int(q[1]);z=q[2];a=0
 if x in l:
  w = l.pop(x)
  if (y < w and z=="LEFT") or (y > w and z=="RIGHT"):
   p("BLOCK");a=100
 if a < 99:
  p("WAIT")