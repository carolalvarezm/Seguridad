#! /usr/bin/env python
# -*- coding: utf-8 -*

def inicializacion(lfsr1,lfsr2,lfsr3,lfsr4):
    #k1=raw_input("Introduce la semilla del primer registro(25b)")
    #k2=raw_input("Introduce la semilla del segundo registro(31b)")
    #k3=raw_input("Introduce la semilla del tercer registro(33b)")
    #k4=raw_input("Introduce la semilla del cuarto registro(39b)")
    
    k1="01111111111111111111111111"
    k2="0111111111111111111111111111111"
    k3="011111111111111111111111111111111"
    k4="010101010101010101010101010101010101010"

    for i in range(len(k1)):
        lfsr1.insert(i,int(k1[i]))
    for i in range(len(k2)):
        lfsr2.insert(i,int(k2[i]))
    for i in range(len(k3)):
        lfsr3.insert(i,int(k3[i]))
    for i in range(len(k4)):
        lfsr4.insert(i,int(k4[i]))

def suma(pr,LFSR):#Le pasamos el polinomio de realimentacion y el registro de desplazamiento
    result=0
    for i in pr:
        result=LFSR[i]^result
    return result

def desplazar(LFSR,entra):#Desplazamos los registros de desplazamiento
    #Desplazamos el registro
    LFSR=LFSR[0:len(LFSR)-1] #Desplazamos el registro
    LFSR.insert(0,entra) #Realimentamos 
    return LFSR

def t2(c1,c0):
    xor=int(c1,2)^int(c0,2)
    return str(c0)+str(xor)

def e0():
    lfsr1=[]
    lfsr2=[]
    lfsr3=[]
    lfsr4=[]
    T1=0
    T2=0
    salida=''

    r1=raw_input("Introduce la semilla de R1 ")
    iteraciones=int(raw_input("Introduce el número de bits de salida "),10)

    pr1=[7,11,19,24]#Polinomio de realimentación de cada registro
    pr2=[11,15,23,30]
    pr3=[3,23,27,32]
    pr4=[3,27,35,38]

    inicializacion(lfsr1,lfsr2,lfsr3,lfsr4)
    
    for i in range(iteraciones):#Por cada iteración
        x1=lfsr1[24]
        lfsr1=desplazar(lfsr1,suma(pr1,lfsr1))
        x2=lfsr2[30]
        lfsr2=desplazar(lfsr2,suma(pr2,lfsr2))
        x3=lfsr3[32]
        lfsr3=desplazar(lfsr3,suma(pr3,lfsr3))
        x4=lfsr4[38]
        lfsr4=desplazar(lfsr4,suma(pr4,lfsr4))

        suma1=x1+x2+x3+x4


        r1=r1[1]+r1[0]
        r2=r1[1]+r1[0]

        salida=salida + '{0:01b}'.format(x1^x2^x3^x4^int(r1[1],2))
        
        suma2=suma1+int(r1,2)
        
        T1=r1
        T2=t2(r2[0],r2[1])
        
        suma2='{0:03b}'.format(suma2)#lo tenemos en binario
        l2=suma2[0]+suma2[1]


        xor1=int(T2,2)^int(l2,2)
        xor2=xor1^int(T1,2)
        r1='{0:02b}'.format(xor2)
    print "salida="+salida

def menu(): #Muestra el menú
	salir=False
	print "Carolina Álvarez Martín - alu0100944723"
	print "P5:Generador E0 de Bluetooth"
	while not salir:
        print "\033[2J\033[1;1f"
		print "¿Qué quieres hacer?"
		print "1)Cifrar"
		print "2)Salir"
		opcion=raw_input("Introduce una opción:" )
		if opcion=="1":
			e0()	
		elif opcion=="2":
			salir=True	
		else: 
			print "Introduce 1 o 2 "
		