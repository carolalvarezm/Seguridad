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
    print "Carolina Álvarez Martín - alu0100944723"
    print "P13:Menú con todas las prácticas"

    while not salir:
        print "\033[2J\033[1;1f"
        print "¿Qué quieres hacer?"
        print "1)Cifrado Vernam"
        print "2)Cifrado Vigenere"
        print "3)Cifrado RC4"
        print "4)Cifrado A5/1"
        print "5)Generador E0 de Bluetooth"
        print "6)Multiplicación en SNOW3G y AES"
        print "7)Algoritmo Rijndael"
        print "8)Modo de cifrado en bloque"
        print "9)Algoritmo Diffie-Helmann"
        print "10)Algoritmo Fiat-Shamir"
        print "11)Cifrado RSA"
        print "12)Cifrado ElGamal Elíptico"
        print "13)Salir"
        opcion=raw_input("Introduce una opción:" )
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
