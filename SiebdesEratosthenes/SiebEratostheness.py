#Sieb des Eratosthenes1

try:

    end =  int(input("Maximum: "))
    start = 2
    primes = []

    for i in range(start, end):

        if len(primes) == 0:
            primes.append(i)
            continue

        prime = True

        for p in primes:

            if i % p == 0:
                prime = False
                break

        if prime:
            primes.append(i)


    print(primes)
            


except Exception as ex:
    #pass
    print("Es ist folgender Fehler aufgetreten: \n" + ex.args[0])