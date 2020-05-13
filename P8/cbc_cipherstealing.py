#! /usr/bin/env python
# -*- coding: utf-8 -*
from  aes import *

def modo_cbc():
    clave=raw_input("\033[36m" +"Introduce la clave en hexadecimal: "+ '\033[0;m')
    iv=raw_input("\033[36m" +"Introduce el vector de inicialización en hexadecimal: "+ '\033[0;m')
    nbloques=int(raw_input("\033[36m" +"¿Cuántos bloques de texto original va a introducir?: "+ '\033[0;m'))
    mensaje=[]
    for i in range(nbloques):
        mensaje.insert(i,raw_input("\033[36m" +"Introduce el bloque de texto original en hexadecimal: "+ '\033[0;m'))
    #Para grabar el vídeo
    resultado=[]
    #nbloques=3
    #iv='00000000000000000000000000000000'
    #clave='000102030405060708090A0B0C0D0E0F'
    #mensaje=['00112233445566778899AABBCCDDEEFF','00000000000000000000000000000000','000000000000000000000000000000']
    

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

    print "\033[35m" +"Clave:                      " + imprimir([clave])[0]+ '\033[0;m'
    print "\033[35m" +"Vector de inicialización:   " + imprimir([iv])[0]+ '\033[0;m'
    for i in (range(len(mensaje_string))):
        print "\033[35m" +"Bloque de texto original " + str(i+1) + ": " + mensaje_string[i]+ '\033[0;m'
    print '\n'
    for i in (range(len(resultado_string))):
        print "\033[35m" +"Bloque de texto cifrado  " + str(i+1) + ": " + resultado_string[i]+ '\033[0;m'

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
    print "\033[2J\033[1;1f"
    print "\033[36m" +"Carolina Álvarez Martín - alu0100944723"+ '\033[0;m'
    print "\033[36m" +"P8:Modos de cifrado en bloque"+ '\033[0;m'
    while not salir:
        print "\033[36m" +"¿Qué quieres hacer?"+ '\033[0;m'
        print "\033[36m" +"1)Cifrar"+ '\033[0;m'
        print "\033[36m" +"2)Salir"+ '\033[0;m'
        opcion = raw_input("\033[36m" +"Introduce una opción:" + '\033[0;m')
        if (opcion=="1"):
            modo_cbc()
        elif opcion=="2":
            salir=True	
        else:
            print "\033[36m" +"Introduce 1 o 2 "+ '\033[0;m'
