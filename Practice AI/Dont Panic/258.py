i=int;u=input;t=print
_,_,_,_,e,_,_,v=[i(j) for j in u().split()]
m=[e]*9
for _ in range(v):
 r,s=u().split();m[i(r)]=i(s)
while True:
 f,p,d=u().split()
 if i(p)<m[i(f)] and d[0]=="L" or i(p)>m[i(f)] and d[0]=="R":
  t("BLOCK")
 else:
  t("WAIT")