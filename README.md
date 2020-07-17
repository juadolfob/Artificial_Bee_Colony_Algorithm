<a href="http://fvcproductions.com"><img src="https://avatars1.githubusercontent.com/u/4284691?v=3&s=200" title="FVCproductions" alt="FVCproductions"></a>

# Artificial Bee Colony Algorithm

> Artificial Bee Colony (ABC) Optimization Algorithm for Solving Constrained Optimization Problems

> ideally one sentence

> ABC, Artificial Bee Colony, Optimization Algorithm


## Table of Contents (Optional)

> If your `README` has a lot of info, section headers might be nice.

- [Installation](#installation)
- [Features](#features)
- [Contributing](#contributing)
- [Team](#team)
- [FAQ](#faq)
- [Support](#support)
- [License](#license)


---

## Example (Optional)

Class is designed to accept lambda functions but it will work with any method, and any number of parameters.

Ackley function:
<img src="https://static.packt-cdn.com/products/9781789612011/graphics/5f433384-3526-40ee-a25b-a1746b0ad84b.png" title="FVCproductions" alt="FVCproductions">

```python 3

Ackley_function = lambda x, y: -20 * math.exp(-.02 * math.sqrt(0.5 * (x ** 2 + y ** 2))) - math.exp(
    0.5 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y))) + math.e + 20


SN = 15
limit = 50
MCN = 1000
bound = 100
result = ABC(Ackley_function, SN, bound, limit, MCN)

print(result.best_solution())

```

---

### Clone

- Clone this repo to your local machine using `https://github.com/fvcproductions/SOMEREPO`


<!-- ## Features 
## Usage (Optional)
## Documentation (Optional)
## Tests (Optional)
-->

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2015 © <a href="http://fvcproductions.com" target="_blank">FVCproductions</a>.
