def multiples():
    sum = 0

    for num in range(1001):
        if num%5 == 0 or num%3 == 0:
            sum= sum + num

    print(sum)

def even_fibonacci():

    sum = 0

    fib = [1,2]

    temp = 0

    while (fib[1]) <=4000000:
        if fib[1]%2 == 0:
            sum = sum + fib[1]

        temp = fib[0] + fib[1]
        fib[0] = fib[1]
        fib[1] = temp

    print(sum)

def prime_factor():
    number = 600851475143
    n = 2


    while n*2 < number:
        while number%n == 0:
            number = number / n

        n = n + 1


    print(number)

multiples()
even_fibonacci()
prime_factor()