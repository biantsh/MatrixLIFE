from __future__ import annotations

from typing import Sequence


class Matrix:
    def __init__(self, values: Sequence[Sequence]) -> None:
        self.matrix = values
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

    def __repr__(self) -> str:
        return f'{self.num_rows} x {self.num_cols} matrix:\n' \
            + '\n'.join([str(row) for row in self.matrix])
