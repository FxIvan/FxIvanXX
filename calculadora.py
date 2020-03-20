def encontrarMultiplos(a,j):
    d = 0
    multiplo = []
    while d <= a:
        if d % j == 0:
            multiplo.append(d)
            d = d + 1
        else:
            d = d + 1
    return  multiplo

numero1 = input("Ingrese numero:")
J = input("Ingrese otro numero:")
multiplo = encontrarMultiplos(numero1, J)
if J==5 :
    print "Fizz", multiplo
elif J!=5:
    print"MULTIPLOZ PERO NO PERTENEZE A Fizz",multiplo
######################

def encontrarMultiplos(a, b):
    d = 0
    multiplos = []
    while d <= a:
        if d % b == 0:
            multiplos.append(d)
            d = d + 1
        else:
            d = d + 1

    return multiplos


numero1 = input("Ingrese numero:")
B = input("Ingrese otro numero:")

multiplos = encontrarMultiplos(numero1, B)
if B==3:
    print "Buzz", multiplos
elif B!=3:
    print "MULTIPLO NO PERTENEZIENTE DE BUZZ",multiplos
###############
c=0
#Ingresa el Multiplo para econtrar el MCM
n=input("Introduzca Numero al Cual se le sacara el multiplo: ")
#El Usuario Indica los dos numeros que quiera saber los MCM
n1=input("Introduza Multiplo1:")
n2=input("Introduza Multiplo2:")

for d in range(1,n+1):
#Es verdadero si n1 y n2 valga 0 entonces este resultado se identificara como "FizzBuzz"
#como indica la actividad
    if d%n1==0 and d%n2==0:
        c+=1
    elif n1==3 and n2==5:
        print("FizzBuzz",d)
    elif n1==5 and n2==3:
        print("FizzBuzz",d)

