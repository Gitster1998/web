x=int(input('1 for add\n2 for subtract\n,3 for multiply\n,4 for divide\n,5 for square root'))
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
