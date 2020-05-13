#! /usr/bin/env python
# -*- coding: utf-8 -*-

def inverso(a,b):
    return euclides_ext(a,b,'i')
def comprobacion(a,b):
    return euclides_ext(a,b,'c')

def euclides_ext(a,b,opcion):
    #incialización
    x=[-1,a,b]
    z=[0,1]
    

    i=2 #-1,0 y empezamos a actualizar el 1


    print "\033[35m" +"Traza de Euclides Extendido:"+'\033[0;m'
    print "\033[35m" +('{3}{0:8}{3} {3}{1:8}{3} {3}{2:8}{3}'.format('i', 'xi', 'zi', '|'))+'\033[0;m'
    print "\033[35m" +('{3}{0:8d}{3} {3}{1:8}{3} {3}{2:8d}{3}'.format(-1, ' ', z[0], '|'))+'\033[0;m'
    print "\033[35m" +('{3}{0:8d}{3} {3}{1:8d}{3} {3}{2:8d}{3}'.format(0, x[1],z[1], '|'))+'\033[0;m'

    while(x[i]!=0):
        x.append(x[i-1]%x[i])
        z.append((-(x[i-1]//x[i])*z[i-1])+z[i-2])
        

        print "\033[35m" +('{3}{0:8d}{3} {3}{1:8d}{3} {3}{2:8d}{3}'.format(i, x[i],z[i], '|'))+'\033[0;m'

        i=i+1
    if(opcion=='c'):
        if(x[i-1]==1):
            print "\033[35m" +str(b) + " es primo con " + str(a) + "\n"+'\033[0;m'
            return True
        else:
            print "\033[35m" +str(b) + " no es primo con " + str(a) + "\n"+'\033[0;m'
            return False
    elif(opcion=='i'):
        print "\033[35m" +"El inverso de " + str(b) + " mod " + str(a) +" es " + str(z[i-2]%a) + "\n"+'\033[0;m'
        return z[i-2]%a
