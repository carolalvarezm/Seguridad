#! /usr/bin/env python
# -*- coding: utf-8 -*-
from  exponenciacion_rapida import *

def diffiehellman ():

    p=raw_input("\033[36m" +"Introduce el número primo P: "+ '\033[0;m')
    alfa=raw_input("\033[36m" +"Introduce alfa (debe ser menor que p): "+ '\033[0;m')
    while(int(p)<int(alfa)):
        alfa=raw_input("\033[36m" +"Introduce alfa (debe ser menor que p): "+ '\033[0;m')

    xA=raw_input("\033[36m" +"Introduce el secreto xA: "+ '\033[0;m')
    xB=raw_input("\033[36m" +"Introduce el secreto xB: "+ '\033[0;m')
    yA=exponenciacion_rapida(alfa,xA,p)
    yB=exponenciacion_rapida(alfa,xB,p)
    ka=exponenciacion_rapida(yB,xA,p)
    kb=exponenciacion_rapida(yA,xB,p)
    if (ka==kb):
        print "\033[35m" +"yA="+str(yA)+ '\033[0;m'
        print "\033[35m" +"yB="+str(yB)+ '\033[0;m'
        print "\033[35m" +"La clave compartida k="+str(ka)+ '\033[0;m'
    else:
        print "\033[35m" +"Algo ha salido mal"+ '\033[0;m'

def menu(): #Muestra el menú
    salir=False
    print "\033[2J\033[1;1f"
    print "\033[36m" +"Carolina Álvarez Martín - alu0100944723"+ '\033[0;m'
    print "\033[36m" +"P9:Algoritmo de Diffie-Hellman"+ '\033[0;m'
    while not salir:
        print "\033[36m" +"¿Qué quieres hacer?"+ '\033[0;m'
        print "\033[36m" +"1)Cifrar"+ '\033[0;m'
        print "\033[36m" +"2)Salir"+ '\033[0;m'
        opcion=raw_input("\033[36m" +"Introduce una opción:"+ '\033[0;m' )
        if opcion=="1":	
            diffiehellman()
        elif opcion=="2":
            salir=True	
        else: 
            print "\033[36m" +"Introduce 1 o 2 "+ '\033[0;m'
