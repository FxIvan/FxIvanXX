
c=0
#Ingresa el Multiplo para econtrar el MCM
n=input("Introduzca Numero al Cual se le sacara el multiplo: ")
#El Usuario Indica los dos numeros que quiera saber los MCM
n1=input("Introduza Multiplo1:")
n2=input("Introduza Multiplo2:")

for i in range(1,n+1):
#Es verdadero si n1 y n2 valga 0 entonces este resultado se identificara como "FizzBuzz"
#como indica la actividad
 if i % n1==0 and i%n2==0:
  c+=1
  print("FizzBuzz",i)

  #############################################################

  def encontrarMultiplos(a,b):
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
  numero2 = input("Ingrese otro numero:")

  multiplos = encontrarMultiplos(numero1, numero2)

  print "Fizz", multiplos