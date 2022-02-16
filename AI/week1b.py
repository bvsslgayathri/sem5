def addition(m,n):
  return m+n
def subtraction(m,n):
  return m-n
def multiply(m,n):
  return m*n
def division(m,n):
  return m/n
def modulo(m,n):
  return m%n
n=int(input('enter 1st number : '))
m=int(input('enter 2nd number : '))
if n>m:
  m,n=n,m
ch=int(input('Enter choice : 1-addition 2-subtraction 3-multiplication 4-division : '))
if ch==1:
  print(addition(m,n))
elif ch==2:
  print(subtraction(m,n))
elif ch==3:
  print(multiply(m,n))
elif ch==4:
  print(division(m,n))
elif ch==5:
  print(modulo(m,n))
else:
  print("select proper operator")
