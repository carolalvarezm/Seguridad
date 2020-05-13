#! /usr/bin/env python
# -*- coding: utf-8 -*-
 
alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def buscar_letra(letra):
    return alfabeto.find(letra)

def cifrado_vigenere():
    print "\n"
    cifrado=''
    mensaje_traza=''
    clave_traza=''
    cifrado_traza=''
    
    mensaje = raw_input("\033[36m" +"Introduce el mensaje a cifrar: "+ '\033[0;m')
    clave = raw_input("\033[36m" +"Introduce la clave: "+ '\033[0;m')

    print "\033[35m" +"Texto original: "+mensaje+ '\033[0;m'
    print "\033[35m" +"Palabra clave: "+clave+ '\033[0;m'

    mensaje = mensaje.replace(' ','') #Para quitar los espacios
    mensaje = mensaje.upper() #Pasar a mayúsculas
    clave = clave.upper() #Pasar a mayúsculas

    for i in range(len(mensaje)):
        Mi=buscar_letra(mensaje[i])
        Ki=buscar_letra(clave[i%len(clave)])
        Ci=(Mi+Ki)%len(alfabeto)
        cifrado = cifrado + alfabeto[Ci]

        if(i%len(clave)==0): #Para la traza del algoritmo
            mensaje_traza =mensaje_traza+' '+mensaje[i:i+len(clave)]
            clave_traza =clave_traza+' '+clave[0:len(mensaje[i:i+len(clave)])]
    
    for i in range(len(cifrado)):
        if(i%len(clave)==0): #Para la traza del algoritmo
            cifrado_traza=cifrado_traza+' '+cifrado[i:i+len(clave)]

    print "\033[35m" +"Traza:"+ '\033[0;m'
    print "\033[35m" +mensaje_traza+ '\033[0;m'
    print "\033[35m" +clave_traza+ '\033[0;m'
    print "\033[35m" +cifrado_traza+ '\033[0;m'
    print "\n"
    print "\033[35m" +"Texto original: " + mensaje+ '\033[0;m'
    print "\033[35m" +"Clave         : " + clave+ '\033[0;m'
    print "\033[35m" +"Texto cifrado : " + cifrado+ '\033[0;m'

def descifrado_vigenere():
    print "\n"
    cifrado=''
    mensaje_traza=''
    clave_traza=''
    cifrado_traza=''

    mensaje = raw_input("\033[36m" +"Introduce el mensaje cifrado: "+ '\033[0;m')
    clave = raw_input("\033[36m" +"Introduce la clave: "+ '\033[0;m')
    
    print "\033[35m" +"Texto cifrado: "+mensaje+ '\033[0;m'
    print "\033[35m" +"Palabra clave: "+clave+ '\033[0;m'

    mensaje = mensaje.replace(' ','') #Para quitar los espacios
    mensaje = mensaje.upper() #Pasar a mayúsculas
    clave = clave.upper() #Pasar a mayúsculas

    mensaje = mensaje.replace(' ','') #Para quitar los espacios
    for i in range(len(mensaje)):
        Ci=buscar_letra(mensaje[i])
        Ki=buscar_letra(clave[i%len(clave)])
        Mi=(Ci-Ki)%len(alfabeto) #(Cifrado - clave mod len(clave))mod len(alfabeto)
        cifrado = cifrado + alfabeto[Mi] 

        if(i%len(clave)==0): #Para la traza del algoritmo
            mensaje_traza =mensaje_traza+' '+mensaje[i:i+len(clave)]
            clave_traza =clave_traza+' '+clave[0:len(mensaje[i:i+len(clave)])]
    
    for i in range(len(cifrado)):
        if(i%len(clave)==0): #Para la traza del algoritmo
            cifrado_traza=cifrado_traza+' '+cifrado[i:i+len(clave)]

    print "\033[35m" +"Traza:"+ '\033[0;m'
    print "\033[35m" +mensaje_traza+ '\033[0;m'
    print "\033[35m" +clave_traza+ '\033[0;m'
    print "\033[35m" +cifrado_traza+ '\033[0;m'
    print "\n"
    print "\033[35m" +"Texto cifrado : " + mensaje+ '\033[0;m'
    print "\033[35m" +"Clave         : " + clave+ '\033[0;m'
    print "\033[35m" + "Texto original: " + cifrado+ '\033[0;m'


def menu(): #Muestra el menú
    salir=False
    print "\033[2J\033[1;1f"
    print "\033[36m" +"Carolina Álvarez Martín - alu0100944723"+ '\033[0;m'
    print "\033[36m" +"P2:Cifrado de Vigenere"+ '\033[0;m'
    while not salir:
        print "\033[36m" +"¿Qué quieres hacer?"+ '\033[0;m'
        print "\033[36m" +"1)Cifrar"+ '\033[0;m'
        print "\033[36m" +"2)Descifrar"+ '\033[0;m'
        print "\033[36m" +"3)Salir"+ '\033[0;m'
        opcion=raw_input("\033[36m" +"Introduce una opción:"+ '\033[0;m' )
        if opcion=="1":
            cifrado_vigenere()	
        elif opcion=="2":
            descifrado_vigenere()
        elif opcion=="3":
            salir=True
            
        else: 
            print "\033[36m" +"Introduce un número entre 1 y 3"+ '\033[0;m'
        
