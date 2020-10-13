from collections import defaultdict
def dfs(st,g,v):
    if st in v:
        print(st,end=" ")
    for i in g[st]:
        if i not in v:
            v.append(i)
            dfs(i,g,v)
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
dfs(st,g,v)
