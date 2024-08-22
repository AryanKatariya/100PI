def add_without_plus(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    
    return a

num1 = 15
num2 = 27
result = add_without_plus_operator(num1, num2)
print(f"The sum of {num1} and {num2} is: {result}")
