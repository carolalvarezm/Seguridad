#! /usr/bin/env python
# -*- coding: utf-8 -*-

def exponenciacion_rapida (base,potencia,modulo):
    y= int(base)
    b= int(potencia)
    x= 1
    while(b!=0):
        if((b%2)!=0):
            b=b-1
            x=(y*x)%int(modulo)
            
        else:
            b=b/2
            y=(y*y)%int(modulo)
            
    return x

