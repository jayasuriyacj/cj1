inp1=input()
c=0
for i in range(len(inp1)):
  if inp1[i].isdigit() or inp1[i].isalpha():
    bb=0
  else:
    c+=1
print(c)
