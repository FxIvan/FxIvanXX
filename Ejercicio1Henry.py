for fizzbuzz in range(1,100):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 ==0:
        print("fizzbuzz",fizzbuzz)
        continue
    if fizzbuzz %3 == 0 :
        print ("Fizz",fizzbuzz)
        continue
    if fizzbuzz%5 ==0:
        print ("Buzz",fizzbuzz)
        continue
    print(fizzbuzz)