#! /usr/bin/env python
# -*- coding: utf-8 -*-
from exponenciacion_rapida import *
from euclides_ext import *

def sumar_puntos(a,b,curva):
    if(a[0]==b[0] and a[1]==b[1]):
        l = ((3*((a[0])**2))+curva[0])%curva[2]
        l = (l*(inverso(curva[2],2*a[1])))%curva[2]
    else:
        l = (b[1]-a[1])*(inverso(curva[2],b[0]-a[0]))
        if(b[0]-a[0]<0):
            l=-l%curva[2]
        else:
            l=l%curva[2]
        
    x3=((l**2)-a[0]-b[0])%curva[2]
    y3=(l*(a[0]-x3)-a[1])%curva[2]
    return (x3,y3)

def calcular_puntos(a,b,p):
    x_results=[]
    y_results=[]
    results=[]
    for i in range(p):
        x_results.append(((i**3)+(a*i)+b)%p)
        y_results.append((i**2)%p)

    index_x=0
    for i in x_results:
        index_y=0
        for j in y_results:
            if(i==j):
                results.append((index_x,index_y))
            index_y=index_y+1
        index_x=index_x+1
    return results

def calculo(db,p,curva):
    if(db==2):
        return sumar_puntos(p,p,curva)
    else:
        aux=sumar_puntos(p,p,curva)
        return calculo(db-2,aux,curva)

def codificar(mensaje,M,p,puntos):
    mensaje=int(mensaje,2)
    h=p//M #Parte entera de la división, cociente
    print "h="+ str(h)+"<"+str(p)+"/"+str(M)
    for j in (range(p)):
        x=h*mensaje+j
        for i in puntos:
            if(i[0]==x):
                y=i[1]
                print "Mensaje original codificado como punto Qm =("+str(mensaje)+"*"+str(h)+"+"+str(j)+","+str(y)+")="+str((x,y))
                return (x,y)

def gamal_eliptico():
    p=int(raw_input("Introduce el número primo p: "))
    a=int(raw_input("Introduce a: "))
    b=int(raw_input("Introduce b: "))
    P=input("Introduce el punto base P: ")

    db=int(raw_input("Introduce dB: "))
    aa=int(raw_input("Introduce aA: "))
    mensaje_original=raw_input("Introduce el mensaje original: ")
    M=int(raw_input("Introduce M: "))
    print "\n"

    puntos=calcular_puntos(a,b,p)
    punto=''
    print "Puntos  de  la  curva: " 
    for i in range(len(puntos)-1):
        punto =  punto + str(puntos[i]) + ", "
    punto = punto + str(puntos[len(puntos)-1])
    print punto
    
    curva=[a,b,p]
    dbP=[0,0]
    aaP=[0,0]
    aadbP=[0,0]

    dbP= calculo(db,P,curva)
    print "Clave pública de B: punto dBP= " + str(dbP)

    mensaje_codificado= codificar(mensaje_original,M,p, puntos)
    

    aaP= calculo(aa,P,curva)

    aadbP=calculo(aa,dbP,curva)
    resultado=sumar_puntos(mensaje_codificado,aadbP,curva)

    
    print "aA(dBP)= " + str(aadbP)
    print "Primer punto del Mensaje cifrado: Qm+aA(dBP)= " + str(resultado)
    print "Segundo punto del Mensaje cifrado: aAP=" + str(aaP)

def menu(): #Muestra el menú
    salir=False
    print "Carolina Álvarez Martín - alu0100944723"
    print "P12:Criptografía Elíptica"
    while not salir:
        print "\033[2J\033[1;1f"
        print "¿Qué quieres hacer?"
        print "1)Cifrar"
        print "2)Salir"
        opcion=raw_input("Introduce una opción:" )
        if opcion=="1":	
            gamal_eliptico()
        elif opcion=="2":
            salir=True	
        else: 
            print "Introduce 1 o 2 "


