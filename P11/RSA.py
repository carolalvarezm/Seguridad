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

    p=int(raw_input("\033[36m" +"Introduce el número primo p: "+'\033[0;m'))
    q=int(raw_input("\033[36m" +"Introduce el número primo q: "+'\033[0;m'))
    d=int(raw_input("\033[36m" +"Introduce d: "+'\033[0;m'))

    n=p*q
    r=(p-1)*(q-1)
    
    while(test==False):

        print "\033[35m" +"\nComprobamos si p(" + str(p) +") es un número primo"+'\033[0;m'
        if(test_lehman_peralta(p)!=True):
            p=int(raw_input("\033[36m" +"Introduce otro número primo p: "+'\033[0;m'))

        print "\033[35m" +"Comprobamos si q(" + str(q) +") es un número primo"+'\033[0;m'

        if(test_lehman_peralta(q)!=True):
            q=int(raw_input("\033[36m" +"Introduce otro número primo q: "+'\033[0;m'))

        print "\033[35m" +"Comprobamos si d(" + str(d) +") es primo con r("+str(r)+")"+'\033[0;m'
        if(comprobacion(r,d)!=True):
            d=int(raw_input("\033[36m" +"Introduce otro número d: "+'\033[0;m'))

        else:
            test=True
        n=p*q
        r=(p-1)*(q-1)

    if(opcion=='C'):
        mensaje_original=raw_input("\033[36m" +"Introduce el mensaje original: "+'\033[0;m')

    else:
        mensaje_original=raw_input("\033[36m" +"Introduce el mensaje cifrado: "+'\033[0;m')

    tam_bloque=size_bloque(26,n)
    
    if(opcion=='C'):
        mensaje_cod = codificar(mensaje_original,tam_bloque)
    else:
        mensaje_cod= codificar(mensaje_original,tam_bloque+1)
    

    print "\033[35m" +"e = inverso(" + str(d) + ") mod " + str(r) + "\n"+'\033[0;m'
    e = inverso(r,d)
    print "\033[35m" +"e = " + str(e) +'\033[0;m'

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
        

        print "\033[35m" +"Parámetros: p="+str(p)+", q="+str(q)+", d="+str(d)+", e="+str(e)+", n="+str(n)+", r="+str(r)+'\033[0;m'
        print "\033[35m" +"Bloques de tamaño " + str(tam_bloque)+'\033[0;m'
        print "\033[35m" +"Mensaje Original:" + mensaje_original+'\033[0;m'
        print "\033[35m" +"Mensaje codificado:" + mensaje_codificado+'\033[0;m'
        print "\033[35m" +"Mensaje cifrado:" + mensaje_cifrado+'\033[0;m'
        print "\033[35m" +"Mensaje Cifrado decodificado:" + mensaje_decodificado+'\033[0;m'
    else:
       
        for i in mensaje_cod:
            mensaje_codificado= mensaje_codificado + " " + str(i) 
            mensaje_cifrado= mensaje_cifrado +" " +str(exponenciacion_rapida(i,d,n)) 
            mensaje_cif.append(exponenciacion_rapida(i,d,n))
            
        mensaje_dec=decodificar(mensaje_cif,tam_bloque)
        mensaje_decodificado=''.join(mensaje_dec)

        print "\033[35m" +"Parámetros: p="+str(p)+", q="+str(q)+", d="+str(d)+", e="+str(e)+", n="+str(n)+", r="+str(r)+'\033[0;m'
        print "\033[35m" +"Bloques de tamaño " + str(tam_bloque)+'\033[0;m'
        print "\033[35m" +"Mensaje Cifrado:" + mensaje_original+'\033[0;m'
        print "\033[35m" +"Mensaje Cifrado codificado:" + mensaje_codificado+'\033[0;m'
        print "\033[35m" +"Mensaje Original Codificado:" + mensaje_cifrado+'\033[0;m'
        print "\033[35m" +"Mensaje Original decodificado:" + mensaje_decodificado+'\033[0;m'
        
def menu(): #Muestra el menú
    salir=False
    print "\033[2J\033[1;1f"
    print "\033[36m" +"Carolina Álvarez Martín - alu0100944723"+'\033[0;m'
    print "\033[36m" +"P11:Cifrado RSA"+'\033[0;m'
    while not salir:
        print "\033[36m" +"¿Qué quieres hacer?"+'\033[0;m'
        print "\033[36m" +"1)Cifrar"+'\033[0;m'
        print "\033[36m" +"2)Descifrar"+'\033[0;m'
        print "\033[36m" +"3)Salir"+'\033[0;m'
        opcion=raw_input("\033[36m" +"Introduce una opción:" +'\033[0;m')
        if opcion=="1":
            rsa('C')	
        elif opcion=="2":
            rsa('D')
        elif opcion=="3":
            salir=True
            
        else: 
            print "\033[36m" +"Introduce un número entre 1 y 3"+'\033[0;m'
