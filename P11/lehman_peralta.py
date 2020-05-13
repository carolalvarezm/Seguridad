#! /usr/bin/env python
# -*- coding: utf-8 -*-

from random import sample
from exponenciacion_rapida import *

def test_lehman_peralta(p):
    #comprobación de los primos pequeños:
    primos=[2,3,5,7,11]
    
    
    print "\033[35m" +"Test de Lehman-Peralta para " + str(p) + ": "+'\033[0;m'
    print "\033[35m" +"1. Comprobamos que no sea divisible por los números primos pequeños: "+'\033[0;m'

    if (p in primos):
        print "\033[35m" +str(p)+ " es un número primo pequeño\n"+'\033[0;m'
        return True
    else:
        for i in primos: 
            if(p%i==0) :
                print "\033[35m" +str(p)+" es divisible por "+str(i)+" por tanto no es primo.\n"+'\033[0;m'
                return False  
            else:
                print "\033[35m" +str(p)+" no es divisible por "+str(i)+"."+'\033[0;m'

        print "\n"

        #aletorios 
        print "\033[35m" +"2.Elegimos enteros(a) al azar entre 2 y " + str(p-1) + " y calculamos a[i]^p-1/2"+'\033[0;m'
        a =sample([x for x in range(2,p-1)],p/2)
        contador=0
        for i in a:

            print "\033[35m" +"Calculamos "+ str(i)+"^" + str((p-1)/2)+"= " + str(exponenciacion_rapida(i,(p-1)/2,p))+ " mod"+str(p)+'\033[0;m'

            if(exponenciacion_rapida(i,(p-1)/2,p)==p-1 or exponenciacion_rapida(i,(p-1)/2,p)==1):
                if (exponenciacion_rapida(i,(p-1)/2,p)==p-1):
                    contador=contador+1
            else :
                print "\033[35m" +str(p) + " No es primo\n"+'\033[0;m'
                return False

            
        if(contador>=1):
            print "\033[35m" +str(p) + " Puede ser primo\n"+'\033[0;m'
            return True
        else:
            print "\033[35m" +str(p) + " No es primo\n"+'\033[0;m'
            return False
