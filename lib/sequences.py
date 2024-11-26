#!/usr/bin/env python3

def fibonacci(number):
    # base/stopping case
    if number<=1:
        return number
    return fibonacci(number- 1) +  fibonacci(number- 2)
    pass

# def print_fibonacci(length):
#     ar_ray=[]
#     for number in range(0, length+ 1):
#         # print(fibonacci(number))
#         # ar_ray.append(fibonacci(number))
#         if (not number )== 0:
#             ar_ray.append(fibonacci(number))
#     print(ar_ray)
#     pass

def print_fibonacci(length):
    # Generate the Fibonacci sequence as a list
    fib_sequence = [fibonacci(i) for i in range(length)]
    print(fib_sequence)
    pass

print_fibonacci(9)