i=int;u=input;t=print
e=u().split()
m=[i(e[4])]*9
for _ in range(i(e[7])):
 r,s=u().split();m[i(r)]=i(s)
while True:
 f,p,d=u().split()
 if i(p)<m[i(f)] and d[0]=="L" or i(p)>m[i(f)] and d[0]=="R":
  t("BLOCK")
 else:
  t("WAIT")