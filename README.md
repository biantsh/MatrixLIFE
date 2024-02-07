# MatrixLIFE

This document provides a description of the MatrixLIFE project, as well as a guide on how to use it as a Python package. 

This project was worked on as part of the second edition of Gjirafa's LIFE (Leadership Institute for Future Engineers) program, for the subject 'Mathematics for Computer Science'. It covers computer projects 2-4, and includes a few extra features such as element-wise operations on matrices.

The project functions as a Python package that is published on PyPI, and can be installed by running `pip install matrix-life`. Its source code and commit history can be viewed at https://github.com/biantsh/MatrixLIFE/.


## Features

- **Ease of use:** Simply include `from matrix_life.matrix import Matrix` in your code to start using the package's functionalities.  
- **Robust error-handling:** If you try to perform operations on matrices with invalid shapes, you will get a detailed explanation instead of a cryptic error message.  
- **No dependencies:** The only imports used in the code are for type annotations, which have no effect on execution but help to make the code easier to read and maintain.  

## Usage manual

As a package, matrix-life allows you to define _n_ x _m_ matrices and perform common mathematical operations on them. You can create a matrix by simply passing a list of values to the initializer:

```python
>>> matrix = Matrix([[1, 2], [3, 4], [5, 6]])
>>> matrix
3 x 2 matrix:
[1, 2]
[3, 4]
[5, 6]
```

Alternatively, you can create a unit matrix, or a matrix filled with any value, by using the `Matrix.identity()` and `Matrix.full_of()` methods:

```python
>>> matrix = Matrix.identity(3, 4)
>>> matrix
3 x 4 matrix:
[1, 0, 0, 0]
[0, 1, 0, 0]
[0, 0, 1, 0]

>>> matrix = Matrix.full_of(3, 4, -1)
>>> matrix
3 x 4 matrix:
[-1, -1, -1, -1]
[-1, -1, -1, -1]
[-1, -1, -1, -1]
```

## Basic operations

You can use the `+-*/` operators to perform basic element-wise operations such as addition, subtraction, multiplication and division on two matrices:

```python
>>> matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
>>> matrix_2 = Matrix.full_of(3, 2, -1)

>>> matrix_1 + matrix_2
3 x 2 matrix:
[0, 1]
[2, 3]
[4, 5]

>>> matrix_1 - matrix_2
3 x 2 matrix:
[2, 3]
[4, 5]
[6, 7]

>>> matrix_1 * matrix_2
3 x 2 matrix:
[-1, -2]
[-3, -4]
[-5, -6]
```

## Matrix multiplication

Instances of `Matrix` also support standard multiplication (i.e. dot product), via the `@` operator:

```python
>>> matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
>>> matrix_2 = Matrix.identity(2, 3)
>>> matrix_1 @ matrix_2
3 x 3 matrix:
[1, 2, 0]
[3, 4, 0]
[5, 6, 0]
```

As a shortcut for multiplying a matrix by itself _n_ times (defined as raising the matrix to the *n+1*th power), you can use the `matrix ** power` notation. Note that a matrix can be multiplied by itself only if it's square shaped:

```python
>>> matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
>>> matrix ** 3
3 x 3 matrix:
[468, 576, 684]
[1062, 1305, 1548]
[1656, 2034, 2412]
```
_Note: As per the mathematical definition, raising a square matrix to the 0th power will return an identity matrix._

## Transposition and symmetry

Transposing a matrix is as simple as calling the `transpose()` method:

```python
>>> matrix = Matrix([[1, 2], [3, 4], [5, 6]])
>>> matrix.transpose()
2 x 3 matrix:
[1, 3, 5]
[2, 4, 6]
```

A square matrix is defined as symmetrical if it is equal to its transpose. While this can be checked in a single line (`matrix == matrix.transpose()`), it is even simpler, and recommended, to use the `is_symmetric()` method:

```python
>>> matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
>>> matrix.is_symmetric()
False

>>> matrix = Matrix.identity(3, 3)
>>> matrix.is_symmetric()
True
```
