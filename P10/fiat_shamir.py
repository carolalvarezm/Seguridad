#! /usr/bin/env python
# -*- coding: utf-8 -*-
def fiat_shamir():
    #Inicialización
    p=int(raw_input("\033[36m" +"Introduce el número primo secreto P: "+'\033[0;m'))
    q=int(raw_input("\033[36m" +"Introduce el número primo secreto Q: "+'\033[0;m'))
    N=p*q
    print "\033[35m" +"N="+str(N) +'\033[0;m'
    #Identificación secreta de A
    s=int(raw_input("\033[36m" +"Introduce el número secreto s: "+'\033[0;m'))
    v=(s**2)%N
    print "\033[35m" +"v="+str(v)+'\033[0;m'

    iteraciones=int(raw_input("\033[36m" +"Introduce el número de iteraciones a realizar: "+'\033[0;m'))

    for i in range(iteraciones):
        #Compromiso secreto de A
        x=int(raw_input("\033[36m" +"Introduce el número secreto x: "+'\033[0;m'))

        #Testigo
        a=(x**2)%N
        #Reto
        e=int(raw_input("\033[36m" +"Introduce el bit e: "+'\033[0;m'))

        #Respuesta
        if (e==0):
            y=x%N
        elif (e==1):
            y=(x*s)%N
        
        #Verificación
        if (e==0):
            print "\033[35m" +str(i+1)+"ª Iteracion: a="+str(a)+",y="+str(y)+ " comprobar que "+str(y)+"^2"+"(="+str(((y**2)%N)) + ") es igual a " +str(a)+"mod"+str(N)+"(="+ str((a%N))+")"+'\033[0;m'
            if(((y**2)%N)==a%N):
                print "\033[35m" +"Comprobación Correcta!"+'\033[0;m'
        elif (e==1): 
            print "\033[35m" +str(i+1)+"ª Iteracion: a="+str(a)+",y="+str(y)+" comprobar que "+str(y)+"^2"+"(="+str(((y**2)%N)) +") es igual a " +str(a)+"*"+str(v)+"mod"+str(N)+"(="+ str(((a*v)%N))+")"+'\033[0;m'
            if(((y**2)%N)==((a*v)%N)):
                print "\033[35m" +"Comprobación Correcta!"+'\033[0;m'
def menu(): #Muestra el menú
    salir=False
    print "\033[2J\033[1;1f"
    print "\033[36m" +"Carolina Álvarez Martín - alu0100944723"+'\033[0;m'
    print "\033[36m" +"P10:Algoritmo de Fiat-Shamir"+'\033[0;m'
    while not salir:
        print "\033[36m" +"¿Qué quieres hacer?"+'\033[0;m'
        print "\033[36m" +"1)Cifrar"+'\033[0;m'
        print "\033[36m" +"2)Salir"+'\033[0;m'
        opcion=raw_input("\033[36m" +"Introduce una opción:"+'\033[0;m' )
        if opcion=="1":	
            fiat_shamir()
        elif opcion=="2":
            salir=True	
        else: 
            print "\033[36m" +"Introduce 1 o 2 "'\033[0;m'
