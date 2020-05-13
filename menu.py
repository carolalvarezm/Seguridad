#! /usr/bin/env python
# -*- coding: utf-8 -*-
import  P1.Vernam_modificado as vernam
import  P2.Vigenere as vigenere
import  P3.RC4 as rc4 
import  P4.A5 as a5 
import  P5.e0 as e0
import  P6.multiplicacion as multiplicacion
import  P7.aes as aes
import  P8.cbc_cipherstealing as cbc 
import  P9.diffie_hellman as df
import  P10.fiat_shamir as fs
import  P11.RSA as rsa 
import  P12.gamal_eliptico as gamal


def menu(): #Muestra el menú
    salir=False
    print "\033[36m" +"Carolina Álvarez Martín - alu0100944723"+ '\033[0;m'
    print "\033[36m" +"P13:Menú con todas las prácticas"+ '\033[0;m'

    while not salir:
        print "\033[2J\033[1;1f"
        print "\033[36m" + "¿Qué quieres hacer?"+ '\033[0;m'
        print "\033[35m" + "1)Cifrado Vernam"+ '\033[0;m'
        print "\033[35m" + "2)Cifrado Vigenere"+ '\033[0;m'
        print "\033[35m" + "3)Cifrado RC4"+ '\033[0;m'
        print "\033[35m" + "4)Cifrado A5/1"+ '\033[0;m'
        print "\033[35m" + "5)Generador E0 de Bluetooth"+ '\033[0;m'
        print "\033[35m" + "6)Multiplicación en SNOW3G y AES"+ '\033[0;m'
        print "\033[35m" + "7)Algoritmo Rijndael"+ '\033[0;m'
        print "\033[35m" + "8)Modo de cifrado en bloque"+ '\033[0;m'
        print "\033[35m" + "9)Algoritmo Diffie-Helmann"+ '\033[0;m'
        print "\033[35m" + "10)Algoritmo Fiat-Shamir"+ '\033[0;m'
        print "\033[35m" + "11)Cifrado RSA"+ '\033[0;m'
        print "\033[35m" + "12)Cifrado ElGamal Elíptico"+ '\033[0;m'
        print "\033[35m" + "13)Salir"+ '\033[0;m'
        opcion=raw_input("\033[36m" +"Introduce una opción:" + '\033[0;m')
        if opcion=="1":	
            vernam.menu()
        elif opcion=="2":	
            vigenere.menu()
        elif opcion=="3":	
            rc4.menu()
        elif opcion=="4":	
            a5.menu()
        elif opcion=="5":	
            e0.menu()
        elif opcion=="6":	
            multiplicacion.menu()
        elif opcion=="7":	
            aes.menu()
        elif opcion=="8":	
            cbc.menu()
        elif opcion=="9":	
            df.menu()
        elif opcion=="10":	
            fs.menu()
        elif opcion=="11":	
            rsa.menu()
        elif opcion=="12":	
            gamal.menu()
        elif opcion=="13":
            salir=True	
        else: 
            print "Introduce un número entre 1 y 13"

menu()
