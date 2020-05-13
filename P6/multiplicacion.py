#! /usr/bin/env python
# -*- coding: utf-8 -*
def multiplicacion():
    primer=int(raw_input("Introduce el primer byte "),10)
    segundo=int(raw_input("Introduce el segundo byte "),10)
    algoritmo=raw_input("Introduce el algoritmo a utilizar(AES o SNOW3G): ")

    bytealgoritmo=''

    while(bytealgoritmo==''):
        if(algoritmo=='AES' or algoritmo=='aes'):
            bytealgoritmo='00011011'
        elif(algoritmo=='SNOW3G' or algoritmo=='snow3g'):
            bytealgoritmo='10101001'
        else:
            algoritmo=raw_input("Introduce el algoritmo a utilizar(AES o SNOW3G): ")
            bytealgoritmo=''

    primer='{0:08b}'.format(primer)#Lo pasamos a binario
    segundo='{0:08b}'.format(segundo)

    print "Traza: "    
    print "Paso 0" 
    mult=[]
    mult.insert(0,primer)
    print mult[0]
    for i in range(7):
        print "Paso " + str(i+1)
        if(mult[i][0]=='1'):
            desplazamiento=mult[i][1:]+'0'
            xor=int(desplazamiento,2)^int(bytealgoritmo,2)#Hacemos la xor 
            xor='{0:08b}'.format(xor)#La pasamos a binario
            mult.insert(i+1,xor)
            print mult[i]+'+'+bytealgoritmo+'='+mult[i+1]
        else:
            mult.insert(i+1,mult[i][1:]+'0')
            print mult[i+1]

    resultado=0
    for i in range(len(segundo)):
        if(segundo[7-i]=='1'):
            resultado=int(mult[i],2)^resultado

    print "\n"
    print "Primer byte:    "+primer
    print "Segundo byte:   "+segundo
    print "Byte Algoritmo: "+bytealgoritmo
    print "Multiplicación: "+'{0:08b}'.format(resultado)


def menu(): #Muestra el menú
	salir=False
	print "Carolina Álvarez Martín - alu0100944723"
	print "P6:Multiplicación en SNOW 3G y AES"
	while not salir:

		print "¿Qué quieres hacer?"
		print "1)Multiplicar"
		print "2)Salir"
		opcion=raw_input("Introduce una opción:" )
		if opcion=="1":
			multiplicacion()	
		elif opcion=="2":
			salir=True	
		else: 
			print "Introduce 1 o 2 "



