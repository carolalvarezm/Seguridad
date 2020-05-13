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
	print "\033[35m" +"Introduce una opción"+ '\033[0;m'
	print "\033[35m" +"1) Clave introducida por teclado"+ '\033[0;m'
	print "\033[35m" +"2) Clave aleatoria"+ '\033[0;m'
	opcion=raw_input()
	if opcion=="1":
		cadena= raw_input("\033[36m" +"Introduce el mensaje a cifrar: " + '\033[0;m') #Introducir desde teclado texto plano
		print "\n"
		print "\033[35m" +"Mensaje original:               " + cadena +  '\033[0;m'
		
		cadena_bin=convertira_binario(cadena) #Convirtiendo la cadena a binario
		cadena_bin="0"+cadena_bin[2:] #Formateando la cadena para que nos quede en la notación que queremos	
		print "\033[35m" +"Mensaje original(binario):      "+cadena_bin + '\033[0;m'
		
		longitud=str(len(cadena_bin)) #Longitud del mensaje en binario
		print "\033[35m" +"Longitud del mensaje en binario:" + longitud + '\033[0;m'
		print "\n"
		
		bucle=False
		while not bucle:
			clave= raw_input("\033[36m" +"Introduce la clave aleatoria: "+ '\033[0;m')
		
			if(len(clave)==len(cadena_bin)):
				print "\n"
				print "\033[35m" +"Clave aleatoria:                "+clave  + '\033[0;m'
				
				
				resultado=int(cadena_bin,2)^int(clave,2) #Pasar string a entero en base 2 y hacer la XOR
				
				resultado=bin(resultado) #Formatear el resultado
				print "\033[35m" +"Mensaje cifrado (binario):      "+'0'+resultado[2:] + '\033[0;m'
				print "\033[35m" +"Mensaje cifrado          :      "+convertira_ascii(resultado) + '\033[0;m'
				print "\n"
				bucle=True
			else:
				print "\033[35m" +"La longitud de la clave debe ser igual a la longitud de la cadena binaria"+ '\033[0;m'
	elif opcion=="2":
		cadena= raw_input("\033[36m" +"Introduce el mensaje a cifrar: " + '\033[0;m') #Introducir desde teclado texto plano
		print "\n"
		print "\033[35m" +"Mensaje original:               " + cadena + '\033[0;m'
		
		cadena_bin=convertira_binario(cadena) #Convirtiendo la cadena a binario
		cadena_bin="0"+cadena_bin[2:] #Formateando la cadena para que nos quede en la notación que queremos	
		print "\033[35m" +"Mensaje original(binario):      "+cadena_bin + '\033[0;m'
		
		longitud=str(len(cadena_bin)) #Longitud del mensaje en binario
		print "\033[35m" +"Longitud del mensaje en binario:" + longitud+ '\033[0;m'
		print "\n"

		clave=''
		for i in cadena_bin:
			clave=clave+str(random.randint(0 , 1))
		print "\n"
		print "\033[35m" +"Clave aleatoria:                "+clave + '\033[0;m'
					
					
		resultado=int(cadena_bin,2)^int(clave,2) #Pasar string a entero en base 2 y hacer la XOR
					
		resultado=bin(resultado) #Formatear el resultado
		print "\033[35m" +"Mensaje cifrado (binario):      "+'0'+resultado[2:]+ '\033[0;m'
		print "\033[35m" +"Mensaje cifrado          :      "+convertira_ascii(resultado)+ '\033[0;m'
		print "\n"
		bucle=True
	else: 
		print "\033[35m" +"Introduce 1 o 2"+ '\033[0;m'


def descifrado_vernam():
	cadena= raw_input("\033[36m" +"Introduce el texto cifrado: "+ '\033[0;m')
	print "\n"
	print "\033[35m" +"Mensaje cifrado:                "+cadena+ '\033[0;m'
	
	cadena_bin=convertira_binario(cadena) #Convirtiendo la cadena a binario
	cadena_bin="0"+cadena_bin[2:] #Formateando la cadena para que nos quede en la notación que queremos	
	print "\033[35m" +"Mensaje cifrado(binario):       "+cadena_bin+ '\033[0;m'
	
	longitud=str(len(cadena_bin)) #Longitud del mensaje en binario
	print "\033[35m" +"Longitud del mensaje en binario:" + longitud+ '\033[0;m'
	print "\n"
	
	bucle=False
	while not bucle:
		clave= raw_input("\033[36m" +"Introduce la clave aleatoria: "+ '\033[0;m')
	
		if(len(clave)==len(cadena_bin)):
			print "\n"
			print "\033[35m" +"Clave aleatoria:                 "+clave + '\033[0;m'
			
			resultado=int(cadena_bin,2)^int(clave,2) #Pasar string a entero en base 2 y hacer la XOR
			
			resultado=bin(resultado)
			print "\033[35m" +"Mensaje original (binario):      "+'0'+resultado[2:]+ '\033[0;m'
			print "\033[35m" +"Mensaje original          :      "+convertira_ascii(resultado)+ '\033[0;m'
			print "\n"
			bucle=True
		else:
			print "\033[35m" +"La longitud de la clave debe ser igual a la longitud de la cadena binaria"+ '\033[0;m'

def menu(): #Muestra el menú
	salir=False
	print "\033[2J\033[1;1f"
	print "\033[36m" +"Carolina Álvarez Martín - alu0100944723" + '\033[0;m'
	print "\033[36m" +"P1:Cifrado de Vernam"+ '\033[0;m'
	while not salir:
		print "\033[36m" +"¿Qué quieres hacer?"+ '\033[0;m'
		print "\033[36m" +"1)Cifrar"+ '\033[0;m'
		print "\033[36m" +"2)Descifrar"+ '\033[0;m'
		print "\033[36m" +"3)Salir"+ '\033[0;m'
		opcion=raw_input("\033[36m" +"Introduce una opción:"+ '\033[0;m' )
		if opcion=="1":
			cifrado_vernam()	
		elif opcion=="2":
			descifrado_vernam()
		elif opcion=="3":
			salir=True
			
		else: 
			print "\033[36m" +"Introduce un número entre 1 y 3"+ '\033[0;m'
		

