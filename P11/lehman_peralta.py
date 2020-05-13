#! /usr/bin/env python
# -*- coding: utf-8 -*-

from random import sample
from exponenciacion_rapida import *

def test_lehman_peralta(p):
    #comprobación de los primos pequeños:
    primos=[2,3,5,7,11]
    
    
    print "Test de Lehman-Peralta para " + str(p) + ": "
    print "1. Comprobamos que no sea divisible por los números primos pequeños: "

    if (p in primos):
        print str(p)+ " es un número primo pequeño\n"
        return True
    else:
        for i in primos: 
            if(p%i==0) :
                print str(p)+" es divisible por "+str(i)+" por tanto no es primo.\n"
                return False  
            else:
                print str(p)+" no es divisible por "+str(i)+"."

        print "\n"

        #aletorios 
        print "2.Elegimos enteros(a) al azar entre 2 y " + str(p-1) + " y calculamos a[i]^p-1/2"
        a =sample([x for x in range(2,p-1)],p/2)
        contador=0
        for i in a:

            print "Calculamos "+ str(i)+"^" + str((p-1)/2)+"= " + str(exponenciacion_rapida(i,(p-1)/2,p))+ " mod"+str(p)

            if(exponenciacion_rapida(i,(p-1)/2,p)==p-1 or exponenciacion_rapida(i,(p-1)/2,p)==1):
                if (exponenciacion_rapida(i,(p-1)/2,p)==p-1):
                    contador=contador+1
            else :
                print str(p) + " No es primo\n"
                return False

            
        if(contador>=1):
            print str(p) + " Puede ser primo\n"
            return True
        else:
            print str(p) + " No es primo\n"
            return False
