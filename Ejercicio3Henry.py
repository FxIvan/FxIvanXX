
print"Bienvenido Usuario Este Maquina tiene un Limite de 6 digitos en caso de querer poner 3 digitos ponga 0 en los restante"

##########################3
n1=input("Numero 1:")
n2=input("Numero 2:")
n3=input("Numero 3:")
n4=input("Numero 4:")
n5=input("Numero 5:")
n6=input("Numero 6:")
list=[n1,n2,n3,n4,n5,n6]
##########
N=input("Ingrese numero que quiera saber:")
##########
if(N == n1 +n2):
    print"verdadero",n1,"+",n2
#########
elif(N == n1+n3):
    print "verdadero",n1,"+",n3
#########
elif(N == n1 +n4):
    print"verdadero",n1,"+",n4
#########
elif(N == n1+n5):
    print "verdadero",n1,"+",n5
#########
elif(N == n1+n6):
    print "verdadero",n1,"+",n6

#########
elif(N == n2 +n3):
    print"verdadero",n2,"+",n3
#########
elif(N == n2+n4):
    print "verdadero",n2,"+",n4
#########
elif(N == n2 +n5):
    print"verdadero",n2,"+",n5
#########
elif(N == n2+n6):
    print "verdadero",n2,"+",n6
#########

elif(N == n3 +n4):
    print"verdadero",n3,"+",n4
#########
elif(N == n3+n5):
    print "verdadero",n3,"+",n5
#########
elif(N == n3 +n6):
    print"verdadero",n3,"+",n6

#########
elif(N == n4 +n5):
    print"verdadero",n4,"+",n5
#########
elif(N == n4+n6):
    print "verdadero",n4,"+",n6
#########
elif(N == n5 +n6):
    print"verdadero",n5,"+",n6
#########
else:
    print "Falso"
