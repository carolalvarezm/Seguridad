#! /usr/bin/env python
# -*- coding: utf-8 -*-

def inverso(a,b):
    return euclides_ext(a,b,'i')
def comprobacion(a,b):
    return euclides_ext(a,b,'c')

def euclides_ext(a,b,opcion):
    #incialización
    x=[-1,a,b]
    z=[0,1]
    

    i=2 #-1,0 y empezamos a actualizar el 1



    while(x[i]!=0):
        x.append(x[i-1]%x[i])
        z.append((-(x[i-1]//x[i])*z[i-1])+z[i-2])
    
        i=i+1
    if(opcion=='c'):
        if(x[i-1]==1):
            return True
        else:
            return False
    elif(opcion=='i'):
        return z[i-2]%a
