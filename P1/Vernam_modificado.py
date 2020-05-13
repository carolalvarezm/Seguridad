#! /usr/bin/env python
# -*- coding: utf-8 -*-
import random
import binascii
cadena=''
from random import randint

def convertira_binario(cadena):
	return bin(int(binascii.hexlify(cadena), 16)) #Nos devuelve binario en notación hexadecimal


def convertira_ascii(cadena):
    n = int(cadena, 2)
    return binascii.unhexlify('%x' %n) #Nos devuelve el ascii

def cifrado_vernam():
	print "Introduce una opción"
	print "1) Clave introducida por teclado"
	print "2) Clave aleatoria"
	opcion=raw_input()
	if opcion=="1":
		cadena= raw_input("Introduce el mensaje a cifrar: " ) #Introducir desde teclado texto plano
		print "\n"
		print "Mensaje original:               " + cadena
		
		cadena_bin=convertira_binario(cadena) #Convirtiendo la cadena a binario
		cadena_bin="0"+cadena_bin[2:] #Formateando la cadena para que nos quede en la notación que queremos	
		print "Mensaje original(binario):      "+cadena_bin
		
		longitud=str(len(cadena_bin)) #Longitud del mensaje en binario
		print "Longitud del mensaje en binario:" + longitud
		print "\n"
		
		bucle=False
		while not bucle:
			clave= raw_input("Introduce la clave aleatoria: ")
		
			if(len(clave)==len(cadena_bin)):
				print "\n"
				print "Clave aleatoria:                "+clave 
				
				
				resultado=int(cadena_bin,2)^int(clave,2) #Pasar string a entero en base 2 y hacer la XOR
				
				resultado=bin(resultado) #Formatear el resultado
				print "Mensaje cifrado (binario):      "+'0'+resultado[2:]
				print "Mensaje cifrado          :      "+convertira_ascii(resultado)
				print "\n"
				bucle=True
			else:
				print "La longitud de la clave debe ser igual a la longitud de la cadena binaria"
	elif opcion=="2":
		cadena= raw_input("Introduce el mensaje a cifrar: " ) #Introducir desde teclado texto plano
		print "\n"
		print "Mensaje original:               " + cadena
		
		cadena_bin=convertira_binario(cadena) #Convirtiendo la cadena a binario
		cadena_bin="0"+cadena_bin[2:] #Formateando la cadena para que nos quede en la notación que queremos	
		print "Mensaje original(binario):      "+cadena_bin
		
		longitud=str(len(cadena_bin)) #Longitud del mensaje en binario
		print "Longitud del mensaje en binario:" + longitud
		print "\n"

		clave=''
		for i in cadena_bin:
			clave=clave+str(random.randint(0 , 1))
		print "\n"
		print "Clave aleatoria:                "+clave 
					
					
		resultado=int(cadena_bin,2)^int(clave,2) #Pasar string a entero en base 2 y hacer la XOR
					
		resultado=bin(resultado) #Formatear el resultado
		print "Mensaje cifrado (binario):      "+'0'+resultado[2:]
		print "Mensaje cifrado          :      "+convertira_ascii(resultado)
		print "\n"
		bucle=True
	else: 
		print "Introduce 1 o 2"


def descifrado_vernam():
	cadena= raw_input("Introduce el texto cifrado: ")
	print "\n"
	print "Mensaje cifrado:                "+cadena
	
	cadena_bin=convertira_binario(cadena) #Convirtiendo la cadena a binario
	cadena_bin="0"+cadena_bin[2:] #Formateando la cadena para que nos quede en la notación que queremos	
	print "Mensaje cifrado(binario):       "+cadena_bin
	
	longitud=str(len(cadena_bin)) #Longitud del mensaje en binario
	print "Longitud del mensaje en binario:" + longitud
	print "\n"
	
	bucle=False
	while not bucle:
		clave= raw_input("Introduce la clave aleatoria: ")
	
		if(len(clave)==len(cadena_bin)):
			print "\n"
			print "Clave aleatoria:                 "+clave 
			
			resultado=int(cadena_bin,2)^int(clave,2) #Pasar string a entero en base 2 y hacer la XOR
			
			resultado=bin(resultado)
			print "Mensaje original (binario):      "+'0'+resultado[2:]
			print "Mensaje original          :      "+convertira_ascii(resultado)
			print "\n"
			bucle=True
		else:
			print "La longitud de la clave debe ser igual a la longitud de la cadena binaria"

def menu(): #Muestra el menú
	salir=False
	print "Carolina Álvarez Martín - alu0100944723"
	print "P1:Cifrado de Vernam"
	while not salir:

		print "¿Qué quieres hacer?"
		print "1)Cifrar"
		print "2)Descifrar"
		print "3)Salir"
		opcion=raw_input("Introduce una opción:" )
		if opcion=="1":
			cifrado_vernam()	
		elif opcion=="2":
			descifrado_vernam()
		elif opcion=="3":
			salir=True
			
		else: 
			print "Introduce un número entre 1 y 3"
		

