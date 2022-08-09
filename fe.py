'''
The following program is a powermod calculator that uses fast exponentiation
Author: Arjun Mehta
'''
import math

while True:
    m = int(input('Enter a base value: '))
    e = int(input('Enter an exponent value: '))
    n = int(input('Enter a Modulus value: '))
    powermods = {1 : (m % n)}
    x = 2
    while x <= e:
        y = ((powermods[x/2] % n) * (powermods[x/2] % n)) % n
        powermods[x] = y
        x = x * 2
    mult = 1
    exp = e
    while exp != 0:
        mult = mult * powermods[2 ** (math.floor(math.log2(exp)))]
        exp = exp - (2 ** (math.floor(math.log2(exp))))
    print((mult) % n)
