def fibonacci():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y

def f(num):
    fibonacci_numbers = list()
    fibonacci_generator = fibonacci() 
    for i in range(1,num*3):
        fibonacci_numbers.append(next(fibonacci_generator))
    print(fibonacci_numbers)
    fibonacci_even = [i for i in fibonacci_numbers if i % 2 == 0]
    return fibonacci_even

print(f(4))
