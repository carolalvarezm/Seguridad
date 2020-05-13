#! /usr/bin/env python
# -*- coding: utf-8 -*-

def inicializacion(semilla):
    S=[]
    K=[]

    print  "\033[35m" +"Inicialización"+ '\033[0;m'
    
    for i in range(256):#inicialización
        S.insert(i,i)#0-255
        K.insert(i,semilla[i%len(semilla)])#
    j=0
    aux=0

    print "\033[35m" +"S:"+str(S)+ '\033[0;m'
    print "\n"
    print "\033[35m" +"K:"+str(K)+ '\033[0;m'
    print "\n"
    
    for i in range(256):
        j=(S[i]+K[i]+j)%256 #S + clave + la j anterior módulo 256
        imprimir="S["+str(i)+"]="+str(S[i])+" K["+str(i)+"]="+str(K[i]) #para imprimir
        aux=S[i] #intercambio
        S[i]=S[j]
        S[j]=aux
        imprimir=imprimir+" produce j="+str(j)+" y "+"S["+str(i)+"]="+str(S[i])+" S["+str(j)+"]="+str(S[j])#para imprimir
        print "\033[35m" +imprimir+ '\033[0;m'
    print "\n"
    print "\033[35m" +"S="+str(S)+ '\033[0;m'
    return S

def generacion_secuencia_cifrante(opcion):
    semilla=raw_input("\033[36m" +"Introduce la semilla de clave:"+ '\033[0;m')
    semilla = semilla.split(',') #separar por comas los números
    for i in range(len(semilla)): #pasar a enteros
        semilla[i]=int(semilla[i])
    
    if opcion == True: #Cifrado/descifrado
        mensaje=raw_input("\033[36m" +"Introduce el texto original:"+ '\033[0;m' )
    else:
        mensaje=raw_input("\033[36m" +"Introduce el texto cifrado:"+ '\033[0;m' )

    mensaje = mensaje.split(',') #separar por comas los números
    for i in range(len(mensaje)): #pasar a enteros
        mensaje[i]=int(mensaje[i])

    print "\033[35m" +"Semilla de clave : "+str(semilla)+ '\033[0;m'
    print "\033[35m" +"Texto original : "+str(mensaje)+ '\033[0;m'
    print "\n"

    #S=inicializacion(semilla)
    S=[1, 9, 174, 61, 172, 71, 229, 27, 139, 16, 232, 209, 102, 38, 249, 231, 201, 53, 123, 14, 85, 74, 42, 79, 225, 148, 72, 34, 210, 33, 67, 96, 35, 21, 20, 235, 104, 109, 51, 130, 241, 119, 12, 248, 173, 147, 128, 207, 197, 86, 140, 146, 227, 159, 64, 206, 56, 184, 153, 200, 90, 92, 80, 125, 19, 116, 76, 166, 115, 221, 89, 11, 28, 82, 65, 199, 156, 25, 175, 237, 239, 129, 39, 213, 224, 84, 211, 228, 7, 157, 252, 254, 145, 32, 69, 247, 110, 3, 8, 219, 97, 98, 251, 178, 186, 155, 114, 57, 30, 70, 112, 190, 202, 37, 23, 204, 31, 45, 49, 182, 40, 179, 29, 127, 63, 245, 68, 138, 13, 132, 189, 253, 180, 0, 143, 88, 2, 95, 205, 191, 99, 46, 111, 54, 168, 52, 108, 133, 83, 196, 113, 58, 5, 149, 78, 165, 126, 48, 177, 158, 134, 94, 164, 107, 44, 208, 203, 181, 93, 26, 233, 91, 141, 101, 154, 17, 120, 192, 122, 212, 6, 131, 176, 226, 214, 117, 55, 75, 73, 220, 223, 142, 22, 105, 41, 24, 118, 170, 103, 234, 169, 36, 163, 217, 152, 47, 59, 216, 121, 18, 238, 194, 185, 244, 230, 246, 62, 188, 187, 60, 160, 136, 222, 87, 150, 135, 193, 4, 218, 198, 151, 10, 43, 81, 77, 215, 183, 124, 243, 255, 240, 242, 171, 250, 100, 144, 236, 195, 137, 162, 50, 161, 66, 167, 15, 106]
    i=0
    j=0
    aux=0

    print "\n"
    print "\033[35m" +"Generación de secuencia cifrante"+ '\033[0;m'
    print "\n"

    for k in range(len(mensaje)):#Para cada byte de secuencia cifrante
        i=(i+1)%256
        print "\033[35m" +"j="+ str(j)+"+S["+str(i)+"] y S["+str(i)+"]="+str(S[i])+ '\033[0;m'
        j=(j+S[i])%256

        aux=S[i]#Intercambiamos S[i] con S[j]
        print "\033[35m" +"Intercambiamos S["+str(i)+"] y S["+str(j)+"]"+ '\033[0;m'
        print "\033[35m" +str(S[i])+ '\033[0;m'
        print "\033[35m" +str(S[j])+ '\033[0;m'
        S[i]=S[j]
        S[j]=aux
        t=(S[i]+S[j])%256 #Sumamos S[i] con S[j] y hacemos el módulo
        print "\033[35m" +"S["+str(t)+"]="+ '\033[0;m'
        print "\033[35m" +str(S[t])+ '\033[0;m'
        cifrado=S[t]^mensaje[k] #Sumamos el byte de secuencia cifrante más el byte del mensaje
        print "\033[35m" +str(S)+ '\033[0;m'
        if opcion == True:
            print "\033[35m" +"Byte "+str(k+1)+" de secuencia cifrante: Salida: S["+str(t)+"] = "+str(S[t])+" "+'{0:08b}'.format(S[t])+ '\033[0;m'
            print "\033[35m" +"Byte "+str(k+1)+" de texto original: Entrada: M["+str(k+1)+"] = "+str(mensaje[k])+" "+'{0:08b}'.format(mensaje[k])+ '\033[0;m'
            print "\033[35m" +"Byte "+str(k+1)+" de secuencia cifrante: Salida: S["+str(cifrado)+"] ="+str(cifrado)+" "+'{0:08b}'.format(cifrado)+ '\033[0;m'
        else: 
            print "\033[35m" +"Byte "+str(k+1)+" de secuencia cifrante: Salida: S["+str(t)+"] = "+str(S[t])+" "+'{0:08b}'.format(S[t])+ '\033[0;m'
            print "\033[35m" +"Byte "+str(k+1)+" de texto cifrado: Entrada: M["+str(k+1)+"] = "+str(mensaje[k])+" "+'{0:08b}'.format(mensaje[k])+ '\033[0;m'
            print "\033[35m" +"Byte "+str(k+1)+" de secuencia original: Salida: S["+str(cifrado)+"] ="+str(cifrado)+" "+'{0:08b}'.format(cifrado)+ '\033[0;m'
    print "\n"

def menu(): #Muestra el menú
    salir=False
    print "\033[2J\033[1;1f"
    print "\033[36m" +"Carolina Álvarez Martín - alu0100944723"+ '\033[0;m'
    print "\033[36m" +"P3:Cifrado RC4"+ '\033[0;m'
    while not salir:
        print "\033[36m" +"¿Qué quieres hacer?"+ '\033[0;m'
        print "\033[36m" +"1)Cifrar"+ '\033[0;m'
        print "\033[36m" +"2)Descifrar"+ '\033[0;m'
        print "\033[36m" +"3)Salir"+ '\033[0;m'
        opcion=raw_input("\033[36m" +"Introduce una opción:"+ '\033[0;m')
        if opcion=="1":
            generacion_secuencia_cifrante(True)	
        elif opcion=="2":
            generacion_secuencia_cifrante(False)
        elif opcion=="3":
            salir=True
            
        else: 
            print "\033[36m" +"Introduce un número entre 1 y 3"+ '\033[0;m'
