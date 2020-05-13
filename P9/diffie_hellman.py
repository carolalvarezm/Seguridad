#! /usr/bin/env python
# -*- coding: utf-8 -*-
from  exponenciacion_rapida import *

def diffiehellman ():

    p=raw_input("Introduce el número primo P: ")
    alfa=raw_input("Introduce alfa (debe ser menor que p): ")
    while(int(p)<int(alfa)):
        alfa=raw_input("Introduce alfa (debe ser menor que p): ")

    xA=raw_input("Introduce el secreto xA: ")
    xB=raw_input("Introduce el secreto xB: ")
    yA=exponenciacion_rapida(alfa,xA,p)
    yB=exponenciacion_rapida(alfa,xB,p)
    ka=exponenciacion_rapida(yB,xA,p)
    kb=exponenciacion_rapida(yA,xB,p)
    if (ka==kb):
        print "yA="+str(yA)
        print "yB="+str(yB)
        print "La clave compartida k="+str(ka)
    else:
        print "Algo ha salido mal"

def menu(): #Muestra el menú
    salir=False
    print "Carolina Álvarez Martín - alu0100944723"
    print "P9:Algoritmo de Diffie-Hellman"
    while not salir:

        print "¿Qué quieres hacer?"
        print "1)Cifrar"
        print "2)Salir"
        opcion=raw_input("Introduce una opción:" )
        if opcion=="1":	
            diffiehellman()
        elif opcion=="2":
            salir=True	
        else: 
            print "Introduce 1 o 2 "
