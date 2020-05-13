#! /usr/bin/env python
# -*- coding: utf-8 -*
from  aes import *

def modo_cbc():
    #clave=raw_input("Introduce la clave en hexadecimal: ")
    #iv=raw_input("Introduce el vector de inicialización en hexadecimal: ")
    #nbloques=raw_input("¿Cuántos bloques de texto original va a introducir?: ")
    #for i in range(nbloques):
        #mensaje.insert(i,raw_input("Introduce el bloque de texto original en hexadecimal: "))
    #Para grabar el vídeo
    resultado=[]
    nbloques=3
    iv='00000000000000000000000000000000'
    clave='000102030405060708090A0B0C0D0E0F'
    mensaje=['00112233445566778899AABBCCDDEEFF','00000000000000000000000000000000','000000000000000000000000000000']
    

    xorini='{0:032x}'.format(int(iv,16)^int(mensaje[0],16))
    tmp=aes(clave,xorini)
    resultado.insert(0,tmp)
    if(len(mensaje[len(mensaje)-1])<32):
        menor=True
    else:
        menor=False


    for i in (range(1,nbloques)):
        if(menor==True and i==nbloques-1):
            tmp=mensaje[i].zfill(32)
            xor='{0:032x}'.format(int(resultado[i-1],16)^int(tmp,16))
            tmp=aes(clave,xor)
            resultado.insert(i,resultado[i-1][0:len(mensaje[i])])
            resultado[i-1]=tmp
            
        else:    
            xor='{0:032x}'.format(int(resultado[i-1],16)^int(mensaje[i],16))
            tmp=aes(clave,xor)
            resultado.insert(i,tmp)

            
     #Para imprimir por pantalla

    if(menor):
        mensaje[len(mensaje)-1] = mensaje[len(mensaje)-1].ljust(32, '-')
        resultado[len(resultado)-1]=resultado[len(resultado)-1].ljust(32, '-')

    resultado_string=imprimir(resultado)     
    mensaje_string=imprimir(mensaje)

    print "Clave:                      " + imprimir([clave])[0]
    print "Vector de inicialización:   " + imprimir([iv])[0]
    for i in (range(len(mensaje_string))):
        print "Bloque de texto original " + str(i+1) + ": " + mensaje_string[i]
    print '\n'
    for i in (range(len(resultado_string))):
        print "Bloque de texto cifrado  " + str(i+1) + ": " + resultado_string[i]

def imprimir(resultado):
    string=''
    imprime=[]
    for i in range(len(resultado)):
        for j in range(0,len(resultado[i]),2):
            string=string+' '+resultado[i][j]+resultado[i][j+1]
        imprime.insert(i,string)
        string=''
    return imprime

def menu(): #Muestra el menú
    salir=False
    print "Carolina Álvarez Martín - alu0100944723"
    print "P8:Modos de cifrado en bloque"
    while not salir:
        print "¿Qué quieres hacer?"
        print "1)Cifrar"
        print "2)Salir"
        opcion = raw_input("Introduce una opción:" )

        if (opcion=="1"):
            modo_cbc()
        elif opcion=="2":
            salir=True	
        else:
            print "Introduce 1 o 2 "
