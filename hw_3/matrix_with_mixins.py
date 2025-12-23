from .matrix import Matrix
from .mixins import (
    NDArrayOperatorsMixin,
    FileOperationsMixin,
    StrMixin,
    PropertyMixin,
    HashMixin,
    CacheMixin,
)


class MatrixWithMixins(
    Matrix,
    NDArrayOperatorsMixin,
    FileOperationsMixin,
    StrMixin,
    PropertyMixin,
):
    def __sub__(self, other: "MatrixWithMixins") -> "MatrixWithMixins":
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(
                f"Matrix dimensions must match: "
                f"({self.rows}, {self.cols}) != ({other.rows}, {other.cols})"
            )
        result = []
        for i in range(self._rows):
            row = []
            for j in range(self._cols):
                row.append(self._data[i][j] - other._data[i][j])
            result.append(row)
        return MatrixWithMixins(result)

    def __truediv__(self, other: "MatrixWithMixins") -> "MatrixWithMixins":
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(
                f"Matrix dimensions must match: "
                f"({self.rows}, {self.cols}) != ({other.rows}, {other.cols})"
            )
        result = []
        for i in range(self._rows):
            row = []
            for j in range(self._cols):
                if other._data[i][j] != 0:
                    row.append(self._data[i][j] / other._data[i][j])
                else:
                    row.append(0)
            result.append(row)
        return MatrixWithMixins(result)

    def __floordiv__(self, other: "MatrixWithMixins") -> "MatrixWithMixins":
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(
                f"Matrix dimensions must match: "
                f"({self.rows}, {self.cols}) != ({other.rows}, {other.cols})"
            )
        result = []
        for i in range(self._rows):
            row = []
            for j in range(self._cols):
                if other._data[i][j] != 0:
                    row.append(self._data[i][j] // other._data[i][j])
                else:
                    row.append(0)
            result.append(row)
        return MatrixWithMixins(result)

    def __mod__(self, other: "MatrixWithMixins") -> "MatrixWithMixins":
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(
                f"Matrix dimensions must match: "
                f"({self.rows}, {self.cols}) != ({other.rows}, {other.cols})"
            )
        result = []
        for i in range(self._rows):
            row = []
            for j in range(self._cols):
                if other._data[i][j] != 0:
                    row.append(self._data[i][j] % other._data[i][j])
                else:
                    row.append(0)
            result.append(row)
        return MatrixWithMixins(result)

    def __pow__(self, power: int) -> "MatrixWithMixins":
        result = []
        for i in range(self._rows):
            row = []
            for j in range(self._cols):
                row.append(self._data[i][j] ** power)
            result.append(row)
        return MatrixWithMixins(result)


class CachedMatrix(
    HashMixin,
    CacheMixin,
    Matrix,
    FileOperationsMixin,
    StrMixin,
    PropertyMixin,
):
    def __init__(self, data):
        Matrix.__init__(self, data)
        CacheMixin.__init__(self)
