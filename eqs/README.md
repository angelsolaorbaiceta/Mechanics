# eqs

The _eqs_ package implements numeric methods to solve systems of equations.
This package also defines the [Matrix](./matrix.py) and [Vector](./vector.py) classes to define the systems of equations.

## Matrix

Matrices are created using the constructor, which takes as parameters the number of rows and columns:

```python
from eqs.matrix import Matrix

matrix = Matrix(2, 3)
```

A newly created matrix is initialized full of zeroes.
To set values in the matrix, you can set all at once:

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

## Vector

## Cholesky Factorization

## Conjugate Gradient