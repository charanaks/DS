from collections import defaultdict
n,e=map(int,input().split())
g=defaultdict(list)
while(e):
    e=e-1
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
st=int(input())
v=[]
v.append(st)
q=[]
q.append(st)
while(len(q)!=0):
    s=q.pop(0)
    print(s,end=" ")
    for i in g[s]:
        if i not in v:
            v.append(i)
            q.append(i)
