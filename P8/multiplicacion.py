#! /usr/bin/env python
# -*- coding: utf-8 -*
def multiplicar(primer,segundo):

    bytealgoritmo='00011011'

    primer='{0:08b}'.format(int(primer,16))#Lo pasamos a binario
    segundo='{0:08b}'.format(int(segundo,16))

    mult=[]
    mult.insert(0,primer)
    for i in range(7):
        if(mult[i][0]=='1'):
            desplazamiento=mult[i][1:]+'0'
            xor=int(desplazamiento,2)^int(bytealgoritmo,2)#Hacemos la xor 
            xor='{0:08b}'.format(xor)#La pasamos a binario
            mult.insert(i+1,xor)
        else:
            mult.insert(i+1,mult[i][1:]+'0')

    resultado=0
    for i in range(len(segundo)):
        if(segundo[7-i]=='1'):
            resultado=int(mult[i],2)^resultado

    return resultado





