<img src="https://pluspng.com/img-png/bee-free-png-cartoon-bee-png-800.png" width="190" height="190" title="bee">

# Artificial Bee Colony Algorithm

> 


> ABC, Artificial Bee Colony, Optimization Algorithm

---

Based on article:

<a href=
https://www.researchgate.net/publication/221498082_Artificial_Bee_Colony_ABC_Optimization_Algorithm_for_Solving_Constrained_Optimization_Problems>Artificial Bee Colony (ABC) Optimization Algorithm for Solving Constrained Optimization Problems</a>
## Example

Class is designed to accept lambda functions but it will work with any method, and any number of parameters.

Ackley function:

<img src="https://static.packt-cdn.com/products/9781789612011/graphics/5f433384-3526-40ee-a25b-a1746b0ad84b.png" title="Ackley_function">

Search domain: -40 > x, y < 40

Global minimun: 0

```python

from ArtificialBeeColony import ABC
import math

ackley_function = lambda x, y: -20 * math.exp(-.02 * math.sqrt(0.5 * (x ** 2 + y ** 2))) - math.exp(
    0.5 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y))) + math.e + 20


sn = 10
limit = 50
mcn = 1000
bound = 40
beecolony = ABC(ackley_function, sn, bound, limit, mcn)

print(beecolony.best_solution())

>>> {
    'solution': [2.7091476396022223e-15, -1.998092029953233e-15],
    'function': 0.0,
    'fitness': 1.0,
    'trial': 39
    }
    
```

---

### Clone

- Clone this repo to your local machine using `https://github.com/juadolfob/Artificial_Bee_Colony_Algorithm`


<!-- ## Features 
## Usage (Optional)
## Documentation (Optional)
## Tests (Optional)
-->
todo:
gradient optimization
bfgs
ACO

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

Copyright (c) 2020 juadolfob

- **[MIT license](https://github.com/juadolfob/Artificial_Bee_Colony_Algorithm/blob/master/LICENSE)**
