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
    
    mensaje = raw_input("Introduce el mensaje a cifrar: ")
    clave = raw_input("Introduce la clave: ")

    print "Texto original: "+mensaje
    print "Palabra clave: "+clave

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

    print "Traza:"
    print mensaje_traza
    print clave_traza
    print cifrado_traza
    print "\n"
    print "Texto original: " + mensaje
    print "Clave         : " + clave
    print "Texto cifrado : " + cifrado

def descifrado_vigenere():
    print "\n"
    cifrado=''
    mensaje_traza=''
    clave_traza=''
    cifrado_traza=''

    mensaje = raw_input("Introduce el mensaje cifrado: ")
    clave = raw_input("Introduce la clave: ")
    
    print "Texto cifrado: "+mensaje
    print "Palabra clave: "+clave

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

    print "Traza:"
    print mensaje_traza
    print clave_traza
    print cifrado_traza
    print "\n"
    print "Texto cifrado : " + mensaje
    print "Clave         : " + clave
    print "Texto original: " + cifrado


def menu(): #Muestra el menú
	salir=False
	print "Carolina Álvarez Martín - alu0100944723"
	print "P2:Cifrado de Vigenere"
	while not salir:
        print "\033[2J\033[1;1f"
		print "¿Qué quieres hacer?"
		print "1)Cifrar"
		print "2)Descifrar"
		print "3)Salir"
		opcion=raw_input("Introduce una opción:" )
		if opcion=="1":
			cifrado_vigenere()	
		elif opcion=="2":
			descifrado_vigenere()
		elif opcion=="3":
			salir=True
			
		else: 
			print "Introduce un número entre 1 y 3"
		
