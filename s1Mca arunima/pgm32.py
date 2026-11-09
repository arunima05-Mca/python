lim=int(input("Enter limit:"))
for i in range(1,lim+1):
    for space in range(i,lim+1):
       print(" ",end=" ")
    for k in range(1,i+1):
       print(" * ",end=" ")
    print()
