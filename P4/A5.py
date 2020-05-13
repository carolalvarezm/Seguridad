#! /usr/bin/env python
# -*- coding: utf-8 -*

def suma(pol_re,LFSR):#Le pasamos las posiciones del polinomio de realimentación y el registro de desplazamiento
    result=0
    for i in pol_re:
        result=int(LFSR[i],2)^result
    return result

def mayoria(a,b,c):#Función mayoría que indica que registros se moverán o no
    return (int(a,2)&int(b,2))^(int(a,2)&int(c,2))^(int(b,2)&int(c,2))
def inicializacion(LFSR1,LFSR2,LFSR3):
    
    K=raw_input("Introduzca la semilla de clave de 64 bits ")#Introducimos la clave

    while(len(K)!=64): #Comprobamos que la longitud de la clave sea correcta
        print ("La clave debe tener 64 bits")
        K=raw_input("Introduzca la semilla de clave de 64 bits ")#Introducimos la clave

    for i in range(19):#Insertamos la semilla de la clave en los registros de desplazamiento
        LFSR1.insert(i,K[i])
    for i in range(22):
        LFSR2.insert(i,K[i+19])
    for i in range(23):
        LFSR3.insert(i,K[i+19+22])

def desplazar(LFSR,entra):

    LFSR=LFSR[1:] #Desplazamos el registro
    LFSR.append(str(entra)) #Realimentamos 
    return LFSR

def a5():
    salida=0
    LFSR1=[]
    LFSR2=[]
    LFSR3=[]
    resultado=''

    inicializacion(LFSR1,LFSR2,LFSR3)
    mensaje=raw_input("Introduce el mensaje a cifrar")


    for i in range(len(mensaje)):
        print "                    "+str(LFSR1)
        print "     "+str(LFSR2)
        print str(LFSR3)
        print "\n"        

        a=suma([0,1,2,5],LFSR1)#Xor de los registros 19,18,17 y 14
        b=suma([0,1],LFSR2)#Xor de los registros 22 y 21
        c=suma([0,1,2,15],LFSR3)#Xor de los registros 23,22,21 y 8
        
        salida=int(LFSR1[0],2)^int(LFSR2[0],2)^int(LFSR3[0],2) 
        #salida= a^b^c
        resultado=resultado+str(salida)
        
        clock=mayoria(LFSR1[10],LFSR2[11],LFSR3[12])#Función mayoría con los bits a9,b11,c11
        print "f("+LFSR1[10]+","+LFSR2[11]+","+LFSR3[12]+")="+str(clock)
        
        if int(LFSR1[10],2)==clock: #Desplazamos solo cuando estamos en la mayoría
            LFSR1=desplazar(LFSR1,a)
        else:
            print "Registro uno queda paralizado"
        if int(LFSR2[11],2)==clock:
            LFSR2=desplazar(LFSR2,b)
        else:
            print "Registro dos queda paralizado"
        if int(LFSR3[12],2)==clock:
            LFSR3=desplazar(LFSR3,c)

        else:
            print "Registro tres queda paralizado"
        if (int(LFSR3[12],2)==clock and int(LFSR2[11],2)==clock and int(LFSR1[10],2)==clock):
            print "Ningun registro queda paralizado"


    print "Mensaje original:   "+mensaje
    print "Secuencia cifrante: "+resultado
    print "Mensaje cifrado:    "+format((int(resultado,2)^int(mensaje,2)),'b').zfill(len(mensaje)) #Xor entre el mensaje y el resultado

def menu(): #Muestra el menú
	salir=False
	print "Carolina Álvarez Martín - alu0100944723"
	print "P4:Cifrado A5/1"
	while not salir:

		print "¿Qué quieres hacer?"
		print "1)Cifrar"
		print "2)Salir"
		opcion=raw_input("Introduce una opción:" )
		if opcion=="1":
			a5()	
		elif opcion=="2":
			salir=True	
		else: 
			print "Introduce 1 o 2 "
		
