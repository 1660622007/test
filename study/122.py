from pymprog import *
import pandas as pd
x = pd.read_csv('C:/Users/16606/Desktop/x.csv', header=0).T  # 读取投入
y = pd.read_csv('C:/Users/16606/Desktop/y.csv', header=0).T  # 读取产出

N = len(x.T)  # DMU数量
def ccr(x, y, i):  # 投入，产出，带评测DMU序号

    begin('ccr')

   #定义变量
    L1 = len(x)  # x维度
    L2 = len(y)  # y维度
    Lambda = var("Lambda", N)  # 定义lambda
    v =var('v',L1)#定义x松弛
    u =var('u',L2)# 定义y松弛
    a =var('a')#x松弛
    b =var('b')#y松弛
   #约束条件 
    for k in range(L1):
        
        (sum(Lambda[j] * x[j][k] for j in range(N))+v[k] )==  x[i][k]
        print(v[k])
    for s in range(L2):
 
        (sum(Lambda[j] * y[j][s] for j in range(N))-u[s] )== y[i][s]
    
    #sum(Lambda[j] for j in range(N)) == 1#控制生产规模不变或可变假设

    #目标函数
    a=sum(v[k] for k in range(L1))
    b=1+sum(u[s] for s in range(L2))
    minimize(a)

    solve()
    return(Lambda)
   
for i in range(N):
    print(ccr(x, y, i))
