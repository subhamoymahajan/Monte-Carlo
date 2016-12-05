import numpy as np
import random
random.seed(1) #ONLY FOR DEGUBGGING TO GENERATE SAME RANDOM NUMBERS AND THIS LINE CAN BE OMITTED
n=10
iter=1000000
Tbar=10
cnt=0 # To check if no. of A = no. of B
system=np.zeros((n,n)) # System of A and B molecules
A=[] # list of all A molecules
B=[] # list of all B molecules
# Generating a random arrangement of A and B both equal in number. 0 representing A and 1 representing B
for i in range(n):
    for j in range(n):
        foo=random.random()
        if foo>0.5:
            if cnt==n*n/2: # Generate A istead of B when it has reached the desired amount
                A.append((i,j))
            else:
                system[i][j]=1
                cnt=cnt+1
                B.append((i,j))
        if foo<0.5:
    
            if n*n/2-cnt<=(n-j-1)+(n-i-1)*(n-1): 
                A.append((i,j))
            else: # Generate B if the number of remaining elements is equal to required number of B
                B.append((i,j))
                system[i][j]=1
                cnt=cnt+1

from matplotlib.pyplot import figure,show
fig=figure()
ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)
ax1.spy(system)
reject=0
for iter in range(iter):
    x1=int(random.random()*(n*n/2)) # Generate a random number between 0 and total number of possible B's or A's -1
    x2=int(random.random()*(n*n/2))
    i1,j1=A[x1] # Select one from each list of A and B
    i2,j2=B[x2]
    fourMinalpha=system[(i1-1+n)%n][j1]+system[(i1+1)%n][j1]+system[i1][(j1-1+n)%n]+system[i1][(j1+1)%n]# sum of neighbours is number of B's as neighbours=4-\alpha
    beta=system[(i2-1+n)%n][j2]+system[(i2+1)%n][j2]+system[i2][(j2-1+n)%n]+system[i2][(j2+1)%n]# sum of neighbours is number of B's as neighbours= \beta
    deltaNab=2*(beta-fourMinalpha)# N_{AB}= 2(\beta+\alpha-4)
    if deltaNab/Tbar<0: #exchange if \frac{\Delta N_{AB}}{\overline{T}}<0
        B[x2]=(i1,j1) #Update A, B list
        A[x1]=(i2,j2)
        system[i2][j2]=0 
        system[i1][j1]=1
        reject=0
    else:
        prob=np.exp(-deltaNab/Tbar)
        rand=random.random()
        if rand<prob: #probability of exchange is e^{-\frac{\Delta N_{AB}}{\overline{T}}}
            B[x2]=(i1,j1)
            A[x1]=(i2,j2)
            system[i2][j2]=0
            system[i1][j1]=1
            reject=0
        else: # reject the exchange
            reject=reject+1
    #if reject>1000:  #UNCOMMENT IF REJECTION CRITERION IS NEEDED
        #print(iter)
        #break   
ax2.spy(system)
show()
