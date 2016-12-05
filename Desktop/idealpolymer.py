import random
random.seed(1)
import numpy as np
d=3 #dimension
ravg=0
r2avg=0
rarr=[]
r2arr=[]
ravgarr=[]
r2avgarr=[]
avgpos=[0, 0, 0]
num=10000
for iter in range(0,num):
    pos=[0,0,0]
    for N in range(0,1000):
        a=random.random()
        b=int(a*2*d)
        pos[int(b/2)]=pos[int(b/2)] - (-1)**b
        
        
    rsqr=pos[0]**2 + pos[1]**2 + pos[2]**2
    r2avg=r2avg*iter + rsqr
    r2avg=r2avg/float(iter+1)
    r2arr.append(rsqr)
    r2avgarr.append(r2avg)
    ravg=ravg*iter+np.sqrt(rsqr)
    ravg=ravg/float(iter+1)
    rarr.append(np.sqrt(rsqr))
    ravgarr.append(ravg)
    avgpos=np.array(avgpos)+np.array(pos)
print("average pos")
print(avgpos/num)
from matplotlib.pyplot import legend,show,plot,xlabel,ylabel,hist,figure

iter=range(0,num)
print("ravg= "+str(ravg))
print("r^2avg= "+str(r2avg))

plot(iter,ravgarr,label="r average")
xlabel("iteration")
ylabel("Average")
legend()
show()

fig = figure()
ax = fig.add_subplot(111)
plot(iter,r2avgarr,label="r^2 average")
xlabel("iteration")
ylabel("Average")
legend()
show()

fig = figure()
ax = fig.add_subplot(111)
n, bins, rectangles = ax.hist(rarr,bins=50,normed=1,alpha=0.5)
fig.canvas.draw()
xlabel("No. of Polymers")
ylabel("Probability")
show()