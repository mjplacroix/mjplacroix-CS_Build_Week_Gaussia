def Fibonacci(n):
   if n <= 1:
       return n
   else:
       return(Fibonacci(n-1) + Fibonacci(n-2))

print(Fibonacci(10))

for i in range(11):
    print(Fibonacci(i))




for num in range(21):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:               
        print(num)

for num in range(101):
    if num % 15 is 0:   # note remainder by 15
        print("FizzBuzz")
    elif num % 3 is 0:
        print("Fizz")
    elif num % 5 is 0:
        print("Buzz")
    else:
        print(num)



