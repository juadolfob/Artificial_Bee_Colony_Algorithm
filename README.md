<img src="https://pluspng.com/img-png/bee-free-png-cartoon-bee-png-800.png" width="190" height="190" title="bee">

# Artificial Bee Colony Algorithm

> Artificial Bee Colony (ABC) Optimization Algorithm for Solving Constrained Optimization Problems



> ABC, Artificial Bee Colony, Optimization Algorithm

---

## Example (Optional)

Class is designed to accept lambda functions but it will work with any method, and any number of parameters.

Ackley function:
<img src="https://static.packt-cdn.com/products/9781789612011/graphics/5f433384-3526-40ee-a25b-a1746b0ad84b.png" title="Ackley_function">

```python

Ackley_function = lambda x, y: -20 * math.exp(-.02 * math.sqrt(0.5 * (x ** 2 + y ** 2))) - math.exp(
    0.5 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y))) + math.e + 20


sn = 15
limit = 50
mcn = 1000
bound = 100
beecolony = ABC(Ackley_function, sn, bound, limit, mcn)

print(beecolony.best_solution())

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
