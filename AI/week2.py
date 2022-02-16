room1=input()
room2=input()
cost=0
statusA=int(input())
statusB=int(input())
location=input('A / B: ')
def cleaning(status1,status2,roomx,roomy):
  global cost
  if(status1==1):
    print('room ', roomx ,' is dirty ')
    print('Room', roomx ,' is  cleaned by vacuum cleaner ')
    status1=0
    cost+=100
    print('changing location of Vacuum cleaner to ',roomy)
    cost+=100
    if status2==1:
      print('room ',roomy,'is dirty')

      print('room ', roomy,'is cleaned')
      status2=0
      cost+=100
    else:
      print('room ',roomy,'is clean')

  else:
    print('room ',roomx, 'is clean..')
    print('changing location of Vacuum cleaner to ',roomy)
    cost+=100
    if status2==1:
      print('room ',roomy,'is dirty')
      
      print('room ', roomy,'is cleaned')
      status2=0
      cost+=100
    else:
      print('room ',roomy,'is clean')

if location=='A':
  cleaning(statusA,statusB,room1,room2)
  
elif location=='B':
  cleaning(statusB,statusA,room2,room1)
print(cost,'is total cost')
