#! /usr/bin/env python
# -*- coding: utf-8 -*-
def fiat_shamir():
    #Inicialización
    p=int(raw_input("Introduce el número primo secreto P: "))
    q=int(raw_input("Introduce el número primo secreto Q: "))
    N=p*q
    print "N="+str(N) 
    #Identificación secreta de A
    s=int(raw_input("Introduce el número secreto s: "))
    v=(s**2)%N
    print "v="+str(v)

    iteraciones=int(raw_input("Introduce el número de iteraciones a realizar: "))

    for i in range(iteraciones):
        #Compromiso secreto de A
        x=int(raw_input("Introduce el número secreto x: "))

        #Testigo
        a=(x**2)%N
        #Reto
        e=int(raw_input("Introduce el bit e: "))

        #Respuesta
        if (e==0):
            y=x%N
        elif (e==1):
            y=(x*s)%N
        
        #Verificación
        if (e==0):
            print str(i+1)+"ª Iteracion: a="+str(a)+",y="+str(y)+ " comprobar que "+str(y)+"^2"+"(="+str(((y**2)%N)) + ") es igual a " +str(a)+"mod"+str(N)+"(="+ str((a%N))+")"
            if(((y**2)%N)==a%N):
                print "Comprobación Correcta!"
        elif (e==1): 
            print str(i+1)+"ª Iteracion: a="+str(a)+",y="+str(y)+" comprobar que "+str(y)+"^2"+"(="+str(((y**2)%N)) +") es igual a " +str(a)+"*"+str(v)+"mod"+str(N)+"(="+ str(((a*v)%N))+")"
            if(((y**2)%N)==((a*v)%N)):
                print "Comprobación Correcta!"
def menu(): #Muestra el menú
    salir=False
    print "Carolina Álvarez Martín - alu0100944723"
    print "P10:Algoritmo de Fiat-Shamir"
    while not salir:
        print "\033[2J\033[1;1f"
        print "¿Qué quieres hacer?"
        print "1)Cifrar"
        print "2)Salir"
        opcion=raw_input("Introduce una opción:" )
        if opcion=="1":	
            fiat_shamir()
        elif opcion=="2":
            salir=True	
        else: 
            print "Introduce 1 o 2 "
