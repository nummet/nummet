x = float(input('Gi eit tal: '))

if x<0:
    print('Talet er negativt')
else:
    print('Talet er positivt eller null')
    
if round(x)!=x:
    print('Talet er ikkje eit heiltal')
else:
    if round(x/2)==x/2:
        print('Talet er eit partal')
    else:
        print('Talet er eit oddetal')