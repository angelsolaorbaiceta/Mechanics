# eqs

The _eqs_ package implements numeric methods to solve systems of equations.
This package also defines the [Matrix](./matrix.py) and [Vector](./vector.py) classes to define the systems of equations.

## Matrix

Matrices are created using the constructor, which takes as parameters the number of rows and columns:

```python
from eqs.matrix import Matrix

matrix = Matrix(2, 3)
```

A newly created `Matrix` is initialized full of zeroes:

```
⎡ 0 0 0 ⎤
⎣ 0 0 0 ⎦
```

To set values in a `Matrix`, you can set all of them at once (make sure the size of the list matches the total number of items in the matrix):

```python
from eqs.matrix import Matrix

matrix = Matrix(2, 3).set_data([1, 2, 3, 4, 5, 6])
```

which defines the matrix:
```
⎡ 1 2 3 ⎤
⎣ 4 5 6 ⎦
```

Values can also be set individually:

```python
from eqs.matrix import Matrix

matrix = Matrix(2, 3).set_value(50, 1, 2)
```

which defines the matrix:
```
⎡ 0 0 0  ⎤
⎣ 0 0 50 ⎦
```

To get a value from a matrix you can use the `value_at` method:

```python
matrix.value_at(1, 2)
```

All the methods that modify the matrix (`set_value`, `set_identity_row`, `scale` ...) return the matrix, so that several modifications can be chained like this:

```python
from eqs.matrix import Matrix

matrix = Matrix(2, 3) \
    .set_value(50, 1, 2) \
    .set_value(25, 2, 2)
```

### Matrix operations

Matrices can be added and subtracted.
For example, to add the matrices:

```
⎡ 1 2 ⎤   ⎡ 3 4 ⎤   ⎡ 4  6  ⎤
⎜ 3 4 ⎟ + ⎜ 5 6 ⎟ = ⎜ 8  10 ⎟
⎣ 4 5 ⎦   ⎣ 7 8 ⎦   ⎣ 12 14 ⎦
```

we can do:

```python
from eqs.matrix import Matrix

mat_a = Matrix(3, 2).set_data([1, 2, 3, 4, 5, 6])
mat_b = Matrix(3, 2).set_data([3, 4, 5, 6, 7, 8])
result = mat_a + mat_b
```

which yields the matrix:
```
⎡ 4  6  ⎤
⎜ 8  10 ⎟
⎣ 12 14 ⎦
```

To subtract the matrices:

```
⎡ 1 2 ⎤   ⎡ 3 4 ⎤   ⎡ -2 -2 ⎤
⎜ 3 4 ⎟ - ⎜ 5 6 ⎟ = ⎜ -2 -2 ⎟
⎣ 4 5 ⎦   ⎣ 7 8 ⎦   ⎣ -2 -2 ⎦
```

we can, using the matrices defined above:

```python
result = mat_a - mat_b
```

which yields the matrix:
```
⎡ -2 -2 ⎤
⎜ -2 -2 ⎟
⎣ -2 -2 ⎦
```

Matrices can also be multiplied.
For example:

```
⎡ 1 2 ⎤               ⎡ 15 18 21 ⎤
⎜ 3 4 ⎟ * ⎡ 1 2 3 ⎤ = ⎜ 33 40 47 ⎟
⎣ 4 5 ⎦   ⎣ 4 5 6 ⎦   ⎣ 51 62 73 ⎦
```

can be multiplied:

```python
from eqs.matrix import Matrix

mat_a = Matrix(3, 2).set_data([1, 2, 3, 4, 5, 6])
mat_b = Matrix(2, 3).set_data([3, 4, 5, 6, 7, 8])
result = mat_a * mat_b
```

which yields the matrix:
```
⎡ 15 18 21 ⎤
⎜ 33 40 47 ⎟
⎣ 51 62 73 ⎦
```

A matrix can also be multiplied with a vector.
For example:

```
⎡1 2 3⎤ ⎧1⎫   ⎧14⎫
⎢4 5 6⎥ ⎨2⎬ = ⎨32⎬
⎣7 8 9⎦ ⎩3⎭   ⎩50⎭
```

can be done:

```python
from eqs.matrix import Matrix, Vector

mat = Matrix(3, 3).set_data([1, 2, 3, 4, 5, 6, 7, 8, 9])
vec = Vector(3).set_data([1, 2, 3])
result = mat.times_vector(vec)
```

which results in the vector:

```
⎧14⎫
⎨32⎬
⎩50⎭
```


## Vector

Vectors are created passing the `Vector` class constructor a size:

```python
from eqs.vector import Vector

vec = Vector(3)
```

A newly created `Vector` is initialized with all zeroes:

```
⎧0⎫
⎨0⎬
⎩0⎭
```

## Cholesky Factorization

## Conjugate Gradient