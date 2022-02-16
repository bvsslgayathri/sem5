def pour(jug1,jug2):
    max1,max2,fill=4,3,2
    print("%d\t%d"%(jug1,jug2))
    if jug1==fill:
        return
    elif jug1==max1:
        pour(0,jug2)
    elif jug1==0 and jug2!=0:
        pour(jug2,0)
    elif jug2==fill:
        pour(0,jug2)
    elif jug2<max2:
        pour(jug1,max2)
    elif jug2<(max1-jug1):
        pour((jug1+jug2),0)
    else:
        pour((max1-jug1)+jug1,jug2-(max1-jug1))

print('Jug1\tjug2')
pour(0,0)

