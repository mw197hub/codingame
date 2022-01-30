i=int;u=input
e=u().split()
m=[i(e[4])]*9
for _ in [1]*i(e[7]):r,s=u().split();m[i(r)]=i(s)
while e:f,p,d=u().split();n=m[i(f)];print("BLOCK"if i(p)<n and d[0]=="L"or i(p)>n and d[0]=="R"else"WAIT")