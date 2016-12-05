import random
random.seed(1)
import numpy as np
d=3 #dimension
ravg=0
r2avg=0
rarr=[]
r2arr=[]
avgcur_pos=[0, 0, 0]

length=1000
num=100*length
def step(cur_pos, dim, dir):
    cur_pos[dim]=cur_pos[dim]+dir
    return cur_pos
print("Length="+str(length))
iter = 0    

while iter<num and (d==2 or d==3):
    cur_pos=[0,0,0]
    old_pos=cur_pos[:]
    pos=[]
    pos.append(cur_pos[:])
    #print("first "+str(step(cur_pos,0,-1)))
    #print("first cur_pos "+str(cur_pos[:]))
    for N in range(0,length):
        if (step(cur_pos[:],0,-1) in pos) and (step(cur_pos[:],0,1) in pos) and (step(cur_pos[:],1,-1) in pos) and (step(cur_pos[:],1,1) in pos):
            if d==2:
                iter=iter-1
                skip_val=1
                break
            elif (step(cur_pos[:],2,-1) in pos) and (step(cur_pos[:],2,1) in pos):
                iter=iter-1
                skip_val=1
                break
        #    print("curpos "+str(cur_pos))
        #    print("pos "+str(pos))
            
        condition=True
        while condition==True:
            a=random.random()
            b=int(a*2*d)
            cur_pos=old_pos[:]
            cur_pos[int(b/2)]=cur_pos[int(b/2)] - (-1)**b
        #    print("1curpos "+str(cur_pos))
        #    print("1pos "+str(pos))
            
         #   print("here1")
            if cur_pos not in pos:
        #        print("here2") 
                old_pos=cur_pos[:]
                skip_val=0
                condition=False
                
        #print(cur_pos)
        pos.append(cur_pos[:]) 
        
    if skip_val <0.9:    
        rsqr=cur_pos[0]**2 + cur_pos[1]**2 + cur_pos[2]**2
        r2avg=r2avg*iter + rsqr
        r2avg=r2avg/float(iter+1)
        r2arr.append(rsqr)
        ravg=ravg*iter+np.sqrt(rsqr)
        ravg=ravg/float(iter+1)
        rarr.append(np.sqrt(rsqr))
        avgcur_pos=np.array(avgcur_pos)+np.array(cur_pos)    
        #print(len(pos))
        # from matplotlib.pyplot import legend,show,plot,xlabel,ylabel,figure
        # from mpl_toolkits.mplot3d import Axes3D
        # fig = figure()
        # ax = Axes3D(fig)
        # x=[]
        # y=[]
        # z=[]
        # for p in pos:
            # x.append(p[0])
            # y.append(p[1])
            # z.append(p[2])
        # ax.plot(x,y,z)
        # print(len(x))
        # show()
    #else:
    #    iter=iter-1
    iter=iter+1
    
print("average cur_pos")
print(np.array(avgcur_pos)/num)
from matplotlib.pyplot import legend,show,plot,xlabel,ylabel,hist,figure
iter=range(0,num)
print("ravg= "+str(ravg))
print("r^2avg= "+str(r2avg))
print(len(rarr))


