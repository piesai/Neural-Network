import random
w=[[random.uniform(-0.5,0.5),random.uniform(-0.5,0.5)]
   ,[random.uniform(-0.5,0.5),random.uniform(-0.5,0.5)]]
p=[[random.uniform(0,0.5)],[random.uniform(0,0.5)]]

def reluM(x):
    reluMx = [[0 for x in range(len(x[0]))] for y in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x[0])):
            reluMx[i][j] = relu(x[i][j])
    return reluMx
def relu(x):
    if x < 0:
        return 0
    if x > 0:
        return x
    if x == 0:
        return 0
def indi(x):
    if x < 0:
        return 0
    if x > 0:
        return 1
    if x==0:
        return 0
def indiM(x):
    indiMx = [[0 for x in range(len(x[0]))] for y in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x[0])):
            indiMx[i][j] = relu(x[i][j])
    return indiMx
def dp(x,y):
  res = [[0 for a in range(len(y[0]))] for b in range(len(x))]
  for i in range(len(x)):
     for j in range(len(y[0])):
         for k in range(len(y)):
          res[i][j]+=x[i][k]*y[k][j]
  return res
def transpose(x):
    trx=[[0 for x in range(len(x))] for y in range(len(x[0]))]
    for i in range(len(x[0])):
        for j in range(len(x)):
            trx[i][j]=x[j][i]
    return trx
def pd(x,y):
    pdx=[[0 for x in range(len(x[0]))] for y in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x[0])):
            pdx[i][j]=x[i][j]*y[i][j]
    return pdx
def yreel(x):
    yreel=0
    if (x[0][0]==1 and x[1][0]==0) or (x[1][0]==1 and x[0][0]==0):
        yreel=[[1]]
    else:
        yreel=[[0]]
    return yreel
def additionM(x,y):
    additionM=[[0 for x in range(len(x[0]))] for y in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x[0])):
            additionM[i][j]=x[i][j]+y[i][j]
    return additionM
def sM(x,y):
    sM=[[0 for x in range(len(x[0]))] for y in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x[0])):
            sM[i][j]=x[i][j]-y[i][j]
    return sM
def ps(x,y):
    psx=[[0 for x in range(len(x[0]))] for y in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x[0])):
            psx[i][j]=x[i][j]*y[0][0]
    return psx
for i in range(1,1000):
 x = [[random.randint(0,1)], [random.randint(0,1)]]
 a=dp(w,x)
 h = reluM(a)
 b=dp(transpose(h),p)
 def forward(x,w,p):
  y=reluM(b)
  return y
 y=forward(x,w,p)
 print(x)
 print(y)
 def cost(y):
    costy=(y[0][0]-yreel(x))**2
    return costy
 gradCp=ps(h,pd(indiM(b),pd([[2]],sM(y,yreel(x)))))
 gradCw=[[0,0],[0,0]]
 gradCw[0][0]=x[0][0]*indi(a[0][0])*p[0][0]*indi(b[0][0])*2*(y[0][0]-yreel(x)[0][0])
 gradCw[0][1]=x[1][0]*indi(a[0][0])*p[0][0]*indi(b[0][0])*2*(y[0][0]-yreel(x)[0][0])
 gradCw[1][0]=x[0][0]*indi(a[1][0])*p[1][0]*indi(b[0][0])*2*(y[0][0]-yreel(x)[0][0])
 gradCw[1][1]=x[1][0]*indi(a[1][0])*p[1][0]*indi(b[0][0])*2*(y[0][0]-yreel(x)[0][0])
 p=sM(p,ps(gradCp,[[0.1]]))
 w=sM(w,ps(gradCw,[[0.1]]))
