from __future__ import annotations

from typing import Any, Sequence


class Matrix:
    def __init__(self, values: Sequence[Sequence]) -> None:
        self.matrix = [[value for value in row] for row in values]
        self.num_rows = len(values)
        self.num_cols = len(values[0])

    def __add__(self, other: Matrix) -> Matrix:
        result = [[value for value in row] for row in self.matrix]

        for row_idx, row in enumerate(other.matrix):
            for col_idx, value in enumerate(row):
                result[row_idx][col_idx] += value

        return Matrix(result)

    def __sub__(self, other: Matrix) -> Matrix:
        result = [[value for value in row] for row in self.matrix]

        for row_idx, row in enumerate(other.matrix):
            for col_idx, value in enumerate(row):
                result[row_idx][col_idx] -= value

        return Matrix(result)

    def __mul__(self, other: Matrix) -> Matrix:
        result = [[value for value in row] for row in self.matrix]

        for row_idx, row in enumerate(other.matrix):
            for col_idx, value in enumerate(row):
                result[row_idx][col_idx] *= value

        return Matrix(result)

    def __matmul__(self, other: Matrix) -> Matrix:
        result = Matrix.full_of(self.num_rows, other.num_cols, 0)

        for row_idx in range(len(self.matrix)):
            for col_idx in range(len(other.matrix[0])):
                for elem_idx in range(len(other.matrix)):
                    product = self.matrix[row_idx][elem_idx] \
                              * other.matrix[elem_idx][col_idx]

                    result.matrix[row_idx][col_idx] += product

        return result

    def __repr__(self) -> str:
        return f'{self.num_rows} x {self.num_cols} matrix:\n' \
            + '\n'.join([str(row) for row in self.matrix])

    @classmethod
    def full_of(cls, num_rows: int, num_cols: int, value: Any) -> Matrix:
        matrix = [[value for _ in range(num_cols)] for _ in range(num_rows)]

        return cls(matrix)

    @classmethod
    def identity(cls, num_rows: int, num_cols: int) -> Matrix:
        matrix = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

        for idx in range(min(num_rows, num_cols)):
            matrix[idx][idx] = 1

        return cls(matrix)
