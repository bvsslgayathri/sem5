def func():
  solutions=[]
  for t in range(9,-1,-1):
    for w in range(9,-1,-1):
      for o in range(9,-1,-1):
        for f in range(9,0,-1):
          for u in range(9,-1,-1):
            for r in range(9,-1,-1):
              l=[t,w,o,f,u,r]
              if len(set(l))==6:
                two=t*100+w*10+o*1
                four=f*1000+o*100+u*10+r*1
                if two+two==four:
                  solutions.append((two,two,four))
  return solutions
print(func())
