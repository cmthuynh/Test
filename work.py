import numpy

x = numpy.random.randint(0,100,10)
y = numpy.random.randint(0,100,10)
value = 0
for i in range(9):
    j=i+1
    for j in range(10):
        b=y[j]-y[i]
        a=x[j]-x[i]
        if a**2 +b**2 == 0:
            continue
        count = 0
        for k in range(10):
            if(b*(x[k]-x[i])-a*(y[k]-x[i])==0):
                count=count + 1
        if value <= count:
            bf=b
            af=a
            xf=x[i]
            yf=y[i]
            value = count
print 'z=',bf,'*(x-',xf,')','-',af,'*(y-',yf,')'
print 'it go through',value,'points'
