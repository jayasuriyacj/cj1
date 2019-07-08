inp1=int(input())
inp2=list(map(int,input().split()))[:inp1]
x=inp2.sort()
inp3 =int( (len(inp2))/2)
print(inp2[inp3])
