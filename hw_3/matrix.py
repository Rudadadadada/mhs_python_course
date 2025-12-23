import numpy as np
from typing import List


class Matrix:
    def __init__(self, data: List[List[float]]):
        if not data or not data[0]:
            raise ValueError("Matrix cannot be empty")
        rows = len(data)
        cols = len(data[0])
        if not all(len(row) == cols for row in data):
            raise ValueError("All rows must have the same length")
        self._data = [row[:] for row in data]
        self._rows = rows
        self._cols = cols

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def cols(self) -> int:
        return self._cols

    @property
    def data(self) -> List[List[float]]:
        return [row[:] for row in self._data]

    def __add__(self, other: "Matrix") -> "Matrix":
        if self._rows != other._rows or self._cols != other._cols:
            raise ValueError(
                f"Matrix dimensions must match: "
                f"({self._rows}, {self._cols}) != ({other._rows}, {other._cols})"
            )
        result = [
            [self._data[i][j] + other._data[i][j] for j in range(self._cols)]
            for i in range(self._rows)
        ]
        return Matrix(result)

    def __mul__(self, other: "Matrix") -> "Matrix":
        if self._rows != other._rows or self._cols != other._cols:
            raise ValueError(
                f"Matrix dimensions must match: "
                f"({self._rows}, {self._cols}) != ({other._rows}, {other._cols})"
            )
        result = [
            [self._data[i][j] * other._data[i][j] for j in range(self._cols)]
            for i in range(self._rows)
        ]
        return Matrix(result)

    def __matmul__(self, other: "Matrix") -> "Matrix":
        if self._cols != other._rows:
            raise ValueError(
                f"Matrix dimensions incompatible for multiplication: "
                f"({self._rows}, {self._cols}) @ ({other._rows}, {other._cols})"
            )
        result = []
        for i in range(self._rows):
            row = []
            for j in range(other._cols):
                s = 0
                for k in range(self._cols):
                    s += self._data[i][k] * other._data[k][j]
                row.append(s)
            result.append(row)
        return Matrix(result)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Matrix):
            return False
        if self._rows != other._rows or self._cols != other._cols:
            return False
        for i in range(self._rows):
            for j in range(self._cols):
                if self._data[i][j] != other._data[i][j]:
                    return False
        return True

    def __str__(self) -> str:
        lines = []
        for row in self._data:
            lines.append(" ".join(str(cell) for cell in row))
        return "\n".join(lines)

    def __repr__(self) -> str:
        return f"Matrix({self._data})"

    def to_file(self, filename: str) -> None:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(str(self))
