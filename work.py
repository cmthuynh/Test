import numpy
from matplotlib import pyplot as plt

#overload warning if x,y over 100000. 
x = numpy.random.randint(0,10000,100)
y = numpy.random.randint(0,10000,100)

value = 0

for i in range(99):
    j=i+1
    for j in range(100):
        b=y[j]-y[i]
        a=x[j]-x[i]
        if a**2 +b**2 == 0:
            continue
        count = 0
        for k in range(100):
            if b*(x[k]-x[i])-a*(y[k]-y[i]) == 0:
                count=count + 1
        if value <= count:
            bf=b
            af=a
            xf=x[i]
            yf=y[i]
            xi=x[j]
            yi=y[j]
            value = count

print ('0 =',bf,'*(x -',xf,')','-',af,'*(y -',yf,')')
print ('it goes through',value,'points')

plt.plot(x,y,'ro')
plt.plot([xf,yf],[xi,yi],color='k',marker='o')
plt.axis([0,10000,0,10000])
plt.show()
