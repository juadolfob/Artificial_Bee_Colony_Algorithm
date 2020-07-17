from ArtificialBeeColony import ABC
import math


Bukin_function_N_6 = lambda x, y: 100 * (math.sqrt(abs(y - 0.01 * x ** 2)) + 0.01 * abs(x + 10))

# limit 5
# Global minimum = (0,0)
Ackley_function = lambda x, y: -20 * math.exp(-.02 * math.sqrt(0.5 * (x ** 2 + y ** 2))) - math.exp(
    0.5 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y))) + math.e + 20

# Global minimum = (0,0,0,...,xn)
sphere_funtion = lambda x1, x2, x3, x4, x5, x6: x1 ** 2 + x2 ** 2 + x3 ** 2 + x4 ** 2 + x5 ** 2 + x6 ** 2

SN = 15
limit = 20
MCN = 1000
bound = 100
result = ABC(sphere_funtion, SN, bound, limit, MCN)

print(result.trial)
print(result.best_solution())
