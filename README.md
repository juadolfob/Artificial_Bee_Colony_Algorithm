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

Search domain: -5 > x, y < 5
Global minimun: 0

```python

ackley_function = lambda x, y: -20 * math.exp(-.02 * math.sqrt(0.5 * (x ** 2 + y ** 2))) - math.exp(
    0.5 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y))) + math.e + 20


sn = 4
limit = 50
mcn = 1000
bound = 5
beecolony = ABC(ackley_function, sn, bound, limit, mcn)

print(beecolony.best_solution())

>>> {
    'solution': [3.7329822787012874e-10, 8.777613943111147e-10, 9.50420947639729e-10, -7.802346958025154e-09],
    'function': 9.910615005712959e-17,
    'fitness': 1.0,
    'trial': 17
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

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
