# eqs

The _eqs_ package implements numeric methods to solve systems of equations.
This package also defines the [Matrix](./matrix.py) and [Vector](./vector.py) classes to define the systems of equations.

__Contents__:

- [Matrix](#Matrix)
    - [Matrix Operations](#matrix-operations)
- [Vector](#Vector)
    - [Vector Operations](#vector-operations)
- [Cholesky Factorization](#cholesky-factorization)
- [Conjugate Gradient](#conjugate-gradient)

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

### Matrix Operations

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

We can set the values of a vector:

```python
from eqs.vector import Vector

vec = Vector(3).set_data([1, 2, 3])
```

which would result in:

```
⎧1⎫
⎨2⎬
⎩3⎭
```

We can add to a given value in the vector:

```python
from eqs.vector import Vector

vec = Vector(3).set_data([1, 2, 3])
vec.add_to_value(10, 2)
```

results in:

```
⎧1 ⎫
⎨2 ⎬
⎩13⎭
```

We can use the `value_at` method to get a value:

```python
from eqs.vector import Vector

vec = Vector(3).set_data([1, 2, 3])
vec.value_at(2) # returns 3
```

### Vector Operations

Vectors can be added, subtracted an multiplied:

```python
from eqs.vector import Vector

vec_a = Vector(2).set_data([1, 2])
vec_b = Vector(2).set_data([4, 3])

addition = vec_a + vec_b
subtraction = vec_a - vec_b
multiplication = vec_a * vec_b
```

## Cholesky Factorization

The Cholesky factorization is a direct numerical method that can be used to solve systems of linear equations whose matrix is positive-definite.
We can use it to solve systems of equations like the following:

```
⎡4   -2   4⎤ ⎧x1⎫   ⎧ 0 ⎫
⎢-2  10  -2⎥ ⎨x2⎬ = ⎨-3 ⎬
⎣4   -2   8⎦ ⎩x3⎭   ⎩-15⎭
```

in our code:

```python
from eqs.vector import Vector
from eqs.matrix import Matrix
from eqs.cholesky import cholesky_solve

mat = Matrix(3, 3).set_data((4, -2, 4, -2, 10, -2, 4, -2, 8))
vec = Vector(3).set_data((0, -3, -15))

solution = cholesky_solve(mat, vec)
```

here, `solution` is the vector:

```
⎧ 3.583⎫
⎨-0.333⎬
⎩-3.75 ⎭
```

The Cholesky's lower matrix decomposition can also be obtained.
The Cholesky numerical method computes this lower triangular matrix as part of its process:

```python
from eqs.matrix import Matrix
from eqs.cholesky import lower_matrix_decomposition

mat = Matrix(3, 3).set_data((4, -2, 4, -2, 10, -2, 4, -2, 8))

lower_triangular = lower_matrix_decomposition(mat)
```

which yields the matrix:

```
⎡ 2  0  0⎤
⎢-1  3  0⎥
⎣ 2  0  2⎦
```

## Conjugate Gradient

The conjugate gradient method is a iterative numeric method to solve systems of linear equations.
Let's use it to solve the system:

```
⎡4   -2   4⎤ ⎧x1⎫   ⎧ 0 ⎫
⎢-2  10  -2⎥ ⎨x2⎬ = ⎨-3 ⎬
⎣4   -2   8⎦ ⎩x3⎭   ⎩-15⎭
```

in our code:

```python
from eqs.vector import Vector
from eqs.matrix import Matrix
from eqs.conjugate_gradient import conjugate_gradient_solve

mat = Matrix(3, 3).set_data((4, -2, 4, -2, 10, -2, 4, -2, 8))
vec = Vector(3).set_data((0, -3, -15))

solution = conjugate_gradient_solve(
    sys_mat=mat, 
    sys_vec=vec, 
    max_iter=100, 
    max_error=1E-5
)
```

here, `solution` is the vector:

```
⎧ 3.583⎫
⎨-0.333⎬
⎩-3.75 ⎭
```
