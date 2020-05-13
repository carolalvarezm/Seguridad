#! /usr/bin/env python
# -*- coding: utf-8 -*
import numpy as np
from  multiplicacion import *


sbox =np.array([
["63", "7c", "77", "7b", "f2", "6b", "6f", "c5", "30", "01", "67", "2b", "fe", "d7", "ab", "76"],
["ca", "82", "c9", "7d", "fa", "59", "47", "f0", "ad", "d4", "a2", "af", "9c", "a4", "72", "c0"],
["b7", "fd", "93", "26", "36", "3f", "f7", "cc", "34", "a5", "e5", "f1", "71", "d8", "31", "15"],
["04", "c7", "23", "c3", "18", "96", "05", "9a", "07", "12", "80", "e2", "eb", "27", "b2", "75"],
["09", "83", "2c", "1a", "1b", "6e", "5a", "a0", "52", "3b", "d6", "b3", "29", "e3", "2f", "84"],
["53", "d1", "00", "ed", "20", "fc", "b1", "5b", "6a", "cb", "be", "39", "4a", "4c", "58", "cf"],
["d0", "ef", "aa", "fb", "43", "4d", "33", "85", "45", "f9", "02", "7f", "50", "3c", "9f", "a8"],
["51", "a3", "40", "8f", "92", "9d", "38", "f5", "bc", "b6", "da", "21", "10", "ff", "f3", "d2"],
["cd", "0c", "13", "ec", "5f", "97", "44", "17", "c4", "a7", "7e", "3d", "64", "5d", "19", "73"],
["60", "81", "4f", "dc", "22", "2a", "90", "88", "46", "ee", "b8", "14", "de", "5e", "0b", "db"],
["e0", "32", "3a", "0a", "49", "06", "24", "5c", "c2", "d3", "ac", "62", "91", "95", "e4", "79"],
["e7", "c8", "37", "6d", "8d", "d5", "4e", "a9", "6c", "56", "f4", "ea", "65", "7a", "ae", "08"],
["ba", "78", "25", "2e", "1c", "a6", "b4", "c6", "e8", "dd", "74", "1f", "4b", "bd", "8b", "8a"],
["70", "3e", "b5", "66", "48", "03", "f6", "0e", "61", "35", "57", "b9", "86", "c1", "1d", "9e"],
["e1", "f8", "98", "11", "69", "d9", "8e", "94", "9b", "1e", "87", "e9", "ce", "55", "28", "df"],
["8c", "a1", "89", "0d", "bf", "e6", "42", "68", "41", "99", "2d", "0f", "b0", "54", "bb", "16"],
])


def expansion_claves(key):
    Rc=np.array([
    ['01', '00', '00', '00'], 
    ['02', '00', '00', '00'],
    ['04', '00', '00', '00'],
    ['08', '00', '00', '00'],
    ['10', '00', '00', '00'],
    ['20', '00', '00', '00'],
    ['40', '00', '00', '00'],
    ['80', '00', '00', '00'],
    ['1B', '00', '00', '00'],
    ['36', '00', '00', '00']])

    wc=np.full((4,4),'00')
    wcn=np.full((4,4),'00')
    Resultado=[]
    for i in range(4):
        wc[i,0]=key[0,i]
        wc[i,1]=key[1,i]
        wc[i,2]=key[2,i]
        wc[i,3]=key[3,i]
    for i in range(10):
        columna=wc[3]
        result=rw(columna)
        result=sw(result)
        wcn[0,0]=str(pasar_hexadecimal(int(result[0],16)^int(wc[0,0],16)^int(Rc[i,0],16)))
        wcn[0,1]=str(pasar_hexadecimal(int(result[1],16)^int(wc[0,1],16)^int(Rc[i,1],16)))
        wcn[0,2]=str(pasar_hexadecimal(int(result[2],16)^int(wc[0,2],16)^int(Rc[i,2],16)))
        wcn[0,3]=str(pasar_hexadecimal(int(result[3],16)^int(wc[0,3],16)^int(Rc[i,3],16)))
        for j in range(3):
            wcn[j+1,0]=str(pasar_hexadecimal(int(wcn[j,0],16)^int(wc[j+1,0],16)))
            wcn[j+1,1]=str(pasar_hexadecimal(int(wcn[j,1],16)^int(wc[j+1,1],16)))
            wcn[j+1,2]=str(pasar_hexadecimal(int(wcn[j,2],16)^int(wc[j+1,2],16)))
            wcn[j+1,3]=str(pasar_hexadecimal(int(wcn[j,3],16)^int(wc[j+1,3],16)))
        wc=np.copy(wcn)
        Resultado.insert(i,np.transpose(wc))
    
    return Resultado

def rw(row):
    temp=row[0]
    row=row[1:]
    row=np.insert(row,3,temp)
    return row
    
def sw(row):
    for i in range(len(row)):
        a=str(row[i][0])
        b=str(row[i][1])
        row[i] = sbox[int(a,16),int(b,16)]
    return row 

def add_round_keys(state,key):
    for i in range(len(state)):
        for j in range(len(state[i])):
            state[i,j]=pasar_hexadecimal(int(state[i,j],16)^int(key[i,j],16))
    return state


def sub_bytes(state):
    for j in state:
        for i in range(len(j)):
            a=str(j[i][0])
            b=str(j[i][1])
            j[i] = sbox[int(a,16),int(b,16)]
    return state

def shift_row(state):
    
    state[0]=state[0]
    state[1]=rw(state[1])
    state[2]=rw(rw(state[2]))
    state[3]=rw(rw(rw(state[3])))
    return state


def mix_column(state):
    matrix=np.transpose(state)
    for i in matrix:
        temp=np.copy(i)
        i[0]=pasar_hexadecimal(multiplicar(temp[0],'02')^multiplicar(temp[1],'03')^int(temp[2],16)^int(temp[3],16))
        i[1]=pasar_hexadecimal(int(temp[0],16)^multiplicar(temp[1],'02')^multiplicar(temp[2],'03')^int(temp[3],16))        
        i[2]=pasar_hexadecimal(int(temp[0],16)^int(temp[1],16)^multiplicar(temp[2],'02')^multiplicar(temp[3],'03'))
        i[3]=pasar_hexadecimal(multiplicar(temp[0],'03')^int(temp[1],16)^int(temp[2],16)^multiplicar(temp[3],'02'))
    return state

def imprimir(estado,clave, iter):
    string=''
    clavestr=''

    for i in range(4):
        for j in range(4):
            string=string+estado[j,i]
            clavestr=clavestr+clave[j,i]
    print "R"+str(iter)+"(Subclave= " + clavestr + ")="+ string
    return string

def aes():
    #semilla=raw_input("Introduce la clave en hexadecimal: ")
    #mensaje=raw_input("Introduce el mensaje original en hexadecimal: ")
    semilla="000102030405060708090a0b0c0d0e0f"
    mensaje="00112233445566778899aabbccddeeff"
    print "Clave: "+semilla
    print "Bloque de Texto original: " + mensaje
    estado=np.full((4,4),'00')
    clave=np.full((4,4),'00')
    contador=0
    for i in range(4):
        for j in range(4):
            estado[j,i]=mensaje[contador]+ mensaje[contador+1]
            clave[j,i]=semilla[contador]+ semilla[contador+1]
            contador=contador+2
    #Expansión de claves
    claves=expansion_claves(clave)
    #Etapa inicial
    estado=add_round_keys(estado,clave)
    imprimir(estado,clave,0)
    # 9 Iteraciones
    for i in range(9):
        string=''
        clavestr=''
        subclave=claves[i]

        estado=sub_bytes(estado)
        estado=shift_row(estado)
        estado=mix_column(estado)
        estado=add_round_keys(estado, subclave)
        imprimir(estado,subclave,i+1)
    #Etapa final
    subclave=claves[9]
    estado=sub_bytes(estado)
    estado=shift_row(estado)
    estado=add_round_keys(estado,subclave)
    a=imprimir(estado,subclave,10)
    

    #Texto cifrado
    print "Bloque de texto cifrado: " + str(a)



def pasar_hexadecimal(num):
    if(len(str(hex(num)))==3):
        return '0'+ str(hex(num))[2]

    else:
        return str(hex(num))[2:4]

def menu(): #Muestra el menú
	salir=False
	print "Carolina Álvarez Martín - alu0100944723"
	print "P7:Algoritmo Rijndael"
	while not salir:

		print "¿Qué quieres hacer?"
		print "1)Cifrar"
		print "2)Salir"
		opcion=raw_input("Introduce una opción:" )
		if opcion=="1":
			aes()	
		elif opcion=="2":
			salir=True	
		else: 
			print "Introduce 1 o 2 "
