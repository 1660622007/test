# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:08:21 2020

@author: Administrator
"""

from pymprog import *
import pandas as pd
x = pd.read_csv("C:\\Users\\16606\\Desktop\\x.csv")#读取投入

y = pd.read_csv("C:\\Users\\16606\\Desktop\\y.csv")#读取产出

N = len(x)#DMU数量 

def ccr(x, y, i):#投入，产出，带评测DMU序号
    
    begin('ccr')

    
    L1 = len(x.T)#x维度
    L2 = len(y.T)#y维度
    Lambda = var('Lambda', N)#定义lambda
    e = var('e')#定义效率
#'''
    for k in range(L1):
        
        sum(Lambda[j] * x.iloc[j][k] for j in range(N)) <= e * x.iloc[i][k]
        
    for k in range(L2):
    

        sum(Lambda[j] * y.iloc[j][k] for j in range(N)) >= y.iloc[i][k]
#'''
    sum(Lambda[j] for j in range(N)) == 1 #控制生产规模不变或可变假设
    
    minimize(e)
    
    solve()
    
    E = e.primal
    
    return(E)
for i in range(N):
    a = ccr(x,y,i)
    print('DMU %f 的效率为: %f'%(i+1,a))
