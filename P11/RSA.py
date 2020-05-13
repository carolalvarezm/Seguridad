#! /usr/bin/env python
# -*- coding: utf-8 -*-
import math
from exponenciacion_rapida import *
from lehman_peralta import *
from euclides_ext import *

def size_bloque(base,n):
    tam_bloque=0
    while(not((base**tam_bloque)<n and n<(base**(tam_bloque+1)))):
        tam_bloque=tam_bloque+1
    
    return tam_bloque

def pasar_a_otra_base(mensaje,base,tam_bloque):
    alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    resultado=''
    aux=mensaje
    for i in range(1,tam_bloque):
        resultado=alfabeto[aux%base] + resultado
        aux=aux//base
    aux=aux%base
    resultado=alfabeto[aux]+resultado

    return resultado

def decodificar(mensaje,tam_bloque):
    result=[]
    for i in mensaje:
        result.append(pasar_a_otra_base(i,26,tam_bloque))
    return result


def codificar(mensaje,tam_bloque):
    alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    mensaje = mensaje.replace(' ','') #Para quitar los espacios
    mensaje = mensaje.upper() #Pasar a mayúsculas
    result=[]
    mensaje_cod=[]
    aux=0

    for i in range(1,(len(mensaje)/tam_bloque)+1):
        mensaje_cod.append(mensaje[(i-1)*tam_bloque:(i)*tam_bloque])


    if(len((mensaje[((len(mensaje)/tam_bloque))*tam_bloque:]))-1!=tam_bloque and len(mensaje[((len(mensaje)/tam_bloque))*tam_bloque:]) !=0 ):
        mensaje_cod.append(mensaje[((len(mensaje)/tam_bloque))*tam_bloque:])
        for i in range(tam_bloque-len(mensaje_cod[len(mensaje_cod)-1])):
            mensaje_cod[len(mensaje_cod)-1]=mensaje_cod[len(mensaje_cod)-1]+'!'

    for i in mensaje_cod:
        resultado=0
        tam=tam_bloque
        for j in i:
            if (j!='!'):
                resultado = resultado + (alfabeto.index(j))*(26**(tam-1)) 
                tam=tam - 1
 
        result.append(resultado)

    return result

def rsa(opcion):
    test=False

    p=int(raw_input("Introduce el número primo p: "))
    q=int(raw_input("Introduce el número primo q: "))
    d=int(raw_input("Introduce d: "))

    n=p*q
    r=(p-1)*(q-1)
    
    while(test==False):

        print "\nComprobamos si p(" + str(p) +") es un número primo"
        if(test_lehman_peralta(p)!=True):
            p=int(raw_input("Introduce otro número primo p: "))

        print "Comprobamos si q(" + str(q) +") es un número primo"

        if(test_lehman_peralta(q)!=True):
            q=int(raw_input("Introduce otro número primo q: "))

        print "Comprobamos si d(" + str(d) +") es primo con r("+str(r)+")"
        if(comprobacion(r,d)!=True):
            d=int(raw_input("Introduce otro número d: "))

        else:
            test=True
        n=p*q
        r=(p-1)*(q-1)

    if(opcion=='C'):
        mensaje_original=raw_input("Introduce el mensaje original: ")

    else:
        mensaje_original=raw_input("Introduce el mensaje cifrado: ")

    tam_bloque=size_bloque(26,n)
    
    if(opcion=='C'):
        mensaje_cod = codificar(mensaje_original,tam_bloque)
    else:
        mensaje_cod= codificar(mensaje_original,tam_bloque+1)
    

    print "e = inverso(" + str(d) + ") mod " + str(r) + "\n"
    e = inverso(r,d)
    print "e = " + str(e) 

    mensaje_cifrado=''
    mensaje_codificado=''
    mensaje_cif=[]
    
    if(opcion=='C'):
        for i in mensaje_cod:
            mensaje_codificado= mensaje_codificado + " " + str(i) 
            mensaje_cifrado= mensaje_cifrado +" " +str(exponenciacion_rapida(i,e,n)) 
            mensaje_cif.append(exponenciacion_rapida(i,e,n))

        mensaje_dec=decodificar(mensaje_cif,tam_bloque+1)
        mensaje_decodificado=''.join(mensaje_dec)
        

        print "Parámetros: p="+str(p)+", q="+str(q)+", d="+str(d)+", e="+str(e)+", n="+str(n)+", r="+str(r)
        print "Bloques de tamaño " + str(tam_bloque)
        print "Mensaje Original:" + mensaje_original
        print "Mensaje codificado:" + mensaje_codificado
        print "Mensaje cifrado:" + mensaje_cifrado
        print "Mensaje Cifrado decodificado:" + mensaje_decodificado
    else:
       
        for i in mensaje_cod:
            mensaje_codificado= mensaje_codificado + " " + str(i) 
            mensaje_cifrado= mensaje_cifrado +" " +str(exponenciacion_rapida(i,d,n)) 
            mensaje_cif.append(exponenciacion_rapida(i,d,n))
            
        mensaje_dec=decodificar(mensaje_cif,tam_bloque)
        mensaje_decodificado=''.join(mensaje_dec)

        print  "Parámetros: p="+str(p)+", q="+str(q)+", d="+str(d)+", e="+str(e)+", n="+str(n)+", r="+str(r)
        print "Bloques de tamaño " + str(tam_bloque)
        print "Mensaje Cifrado:" + mensaje_original
        print "Mensaje Cifrado codificado:" + mensaje_codificado
        print "Mensaje Original Codificado:" + mensaje_cifrado
        print "Mensaje Original decodificado:" + mensaje_decodificado
        
def menu(): #Muestra el menú
    salir=False
    print "Carolina Álvarez Martín - alu0100944723"
    print "P11:Cifrado RSA"
    while not salir:
        print "\033[2J\033[1;1f"
        print "¿Qué quieres hacer?"
        print "1)Cifrar"
        print "2)Descifrar"
        print "3)Salir"
        opcion=raw_input("Introduce una opción:" )
        if opcion=="1":
            rsa('C')	
        elif opcion=="2":
            rsa('D')
        elif opcion=="3":
            salir=True
            
        else: 
            print "Introduce un número entre 1 y 3"
