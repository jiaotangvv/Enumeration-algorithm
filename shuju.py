# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 21:04:53 2018

@author: TP
"""

import numpy as np
import itertools

#计算模块
def jisuan(dis,unpoint,site):#unpoint还没走的节点矩阵(除终点以外)，明确当前节点的意义
    route=list(itertools.permutations(unpoint,len(unpoint)))#全排列
    route[:] = [list(c) for c in route]
    for c in route:
        c.append(7)
        c.insert(0,site)
    minroute=[]
    for r in route:
        k=0
        for i in range(len(unpoint)+1):
            p = r[i]
            j = r[i+1]
            k = k+dis[p,j]
        minroute.append(k)
#    print(route[minroute.index(min(minroute))])
#    print(min(minroute))
    return(route[minroute.index(min(minroute))],min(minroute))
    

#event
originmatrix=np.array([[0,300,360,210,590,475,500,690],\
                  [300,0,380,270,230,285,200,390],\
                  [360,380,0,510,230,765,580,770],\
                  [210,270,510,0,470,265,450,640],\
                  [590,230,230,470,0,515,260,450],\
                  [475,285,765,265,515,0,460,650],\
                  [500,200,580,450,260,460,0,190],\
                  [690,390,760,640,450,650,190,0]])
#第一问
Q1=jisuan(originmatrix,[1,2,3,4,5,6],0)

#第二问
originmatrix_2=originmatrix*1
originmatrix_2[0,3]=1000
originmatrix_2[3,0]=1000
Q2=jisuan(originmatrix_2,[1,2,3,4,5,6],0)
print(originmatrix)


#第三问
timematrix=originmatrix/2000
print(timematrix)
x1route=np.array([0,2,4,3,5,1,6,7])
y=np.array([[0,0],[1/6,1/2],[1/3,1],[1/2,1/2],[1/2,1],[1/3,1],[1/2,1],[1/2,5.5]])#景点停留时间
for i in x1route[1,7]:
    unit=1/60#单位变量
    x11=np.array([[0,0]])
    a=np.array([0,0])#初始化步行时间
    a[0,0]=x11[-1][2]+timematrix[x1route[np.argwhere(x1route==i)-1],i]#确定步行时间
    staytime=y[i,0]
    while y[i,0]<=staytime<y[i,1]:
        a[0,1]=a[0,0]+staytime
        x1=np.row_stack((x11,a))
        staytime=staytime+unit
    
        
    
    
x1=np.array([[0,0],[3.265,3.730],[0.18,1.02],[2,2.5],[1.135,1.765],[2.633,3.123],[3.830,4.33],[4.425,5.5]])#x1[i]为第i个点的时间窗
x2=np.array([[]])

def findroute(x1):
    site=0#初始当前位置
    t_state=0#初始当前时间
    dropobject=[]#初始化已经走过的景点
    site_id=[0,1,2,3,4,5,6]
    
    #主循环
    for step in range(1,8):
        #step=1to7
        #site=0当前位置
        #t_state当前时间
        #已走过的位置dropobject.append(site)
        #明确对接下来哪几个点进行概算
        site_id.remove(site)#去掉当前的点[1,2,3,4,5,6]
        #切片site_id=unpoint
        timematrix_state=timematrix*1
        newdistime=0
        for indexid in site_id:#检查未来去向是否被占用
            if x1[indexid,0]<=t_state+timematrix_state[site,indexid]<x1[indexid,1]:
                newdistime=x1[indexid,1]-t_state
                timematrix_state[site,indexid]=newdistime*1
    # =============================================================================
    #         elif x2[indexid,0]<=t_state+timematrix_state[site,indexid]<x1[indexid,1]:
    #             newsidtime=x2[indexid,1]-t_state
    # =============================================================================
            elif t_state+timematrix_state[site,indexid]+y[indexid,0]>x1[indexid,0]:
                timematrix_state[site,indexid]=10000#惩罚后来的队伍比前面的队伍先占用节点
    # =============================================================================
    #         elif t_state+timematrix_state[site,indexid]+y[indexid,0]>x2[indexid,0]:
    #             timematrix_state[site,indexid]=100
    # =============================================================================
            #得到了新的timematrix_state时间状态矩阵
        print(timematrix_state)
        #当前最短路径
        (p,q)=jisuan(timematrix_state,site_id,site)
        print(p)
        nextsite=p[1]*1
        t_state=t_state+timematrix_state[site,nextsite]+y[nextsite,0]
        print(t_state)
        dropobject.append(site)
        site=nextsite*1
            
    dropobject.append(7)
    print(dropobject)
    return(dropobject)
    
    #计算距离
    r=dropobject
    minroute=[]
    dis=originmatrix
    k=0
    for i in range(7):
        p = r[i]
        j = r[i+1]
        k = k+dis[p,j]
    minroute.append(k)
    print(minroute)
    
findroute(x1)