#! /usr/bin/env python
# -*- coding: utf-8 -*
def multiplicacion():
    primer=int(raw_input("\033[36m" +"Introduce el primer byte "+ '\033[0;m'),10)
    segundo=int(raw_input("\033[36m" +"Introduce el segundo byte "+ '\033[0;m'),10)
    algoritmo=raw_input("\033[36m" +"Introduce el algoritmo a utilizar(AES o SNOW3G): "+ '\033[0;m')

    bytealgoritmo=''

    while(bytealgoritmo==''):
        if(algoritmo=='AES' or algoritmo=='aes'):
            bytealgoritmo='00011011'
        elif(algoritmo=='SNOW3G' or algoritmo=='snow3g'):
            bytealgoritmo='10101001'
        else:
            algoritmo=raw_input("\033[36m" +"Introduce el algoritmo a utilizar(AES o SNOW3G): "+ '\033[0;m')
            bytealgoritmo=''

    primer='{0:08b}'.format(primer)#Lo pasamos a binario
    segundo='{0:08b}'.format(segundo)

    print "\033[35m" +"Traza: " + '\033[0;m'
    print "\033[35m" +"Paso 0" + '\033[0;m'
    mult=[]
    mult.insert(0,primer)
    print "\033[35m" +mult[0]+ '\033[0;m'
    for i in range(7):
        print "\033[35m" +"Paso " + str(i+1)+ '\033[0;m'
        if(mult[i][0]=='1'):
            desplazamiento=mult[i][1:]+'0'
            xor=int(desplazamiento,2)^int(bytealgoritmo,2)#Hacemos la xor 
            xor='{0:08b}'.format(xor)#La pasamos a binario
            mult.insert(i+1,xor)
            print "\033[35m" +mult[i]+'+'+bytealgoritmo+'='+mult[i+1]+ '\033[0;m'
        else:
            mult.insert(i+1,mult[i][1:]+'0')
            print "\033[35m" +str(mult[i+1])+ '\033[0;m'

    resultado=0
    for i in range(len(segundo)):
        if(segundo[7-i]=='1'):
            resultado=int(mult[i],2)^resultado

    print "\n"
    print "\033[35m" +"Primer byte:    "+primer+ '\033[0;m'
    print "\033[35m" +"Segundo byte:   "+segundo+ '\033[0;m'
    print "\033[35m" +"Byte Algoritmo: "+bytealgoritmo+ '\033[0;m'
    print "\033[35m" +"Multiplicación: "+'{0:08b}'.format(resultado)+ '\033[0;m'


def menu(): #Muestra el menú
    salir=False
    print "\033[2J\033[1;1f"
    print "\033[36m" +"Carolina Álvarez Martín - alu0100944723"+ '\033[0;m'
    print "\033[36m" +"P6:Multiplicación en SNOW 3G y AES"+ '\033[0;m'
    while not salir:
        print "\033[36m" +"¿Qué quieres hacer?"+ '\033[0;m'
        print "\033[36m" +"1)Multiplicar"+ '\033[0;m'
        print "\033[36m" +"2)Salir"+ '\033[0;m'
        opcion=raw_input("\033[36m" +"Introduce una opción:"+ '\033[0;m' )
        if opcion=="1":
            multiplicacion()	
        elif opcion=="2":
            salir=True	
        else: 
            print "\033[36m" +"Introduce 1 o 2 "+ '\033[0;m'



