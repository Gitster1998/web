x=int(input('1 for add\n2 for subtract\n3 for multiply\n4 for divide\n5 for square root'))
if x==5:
  l=int(input('enter a number'))
  print(l**.5)
else:
        m,n=input().split()
        m=int(m)
        n=int(n)
        if x==1:
          print(m+n)
        elif x==2:
          print(m-n)
        elif x==3:
          print(m*n)
        elif x==4:
          print(m/n)
