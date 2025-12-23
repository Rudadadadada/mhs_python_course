from typing import Any


class NDArrayOperatorsMixin:
    def __add__(self, other: Any) -> Any:
        return self._apply_operation("__add__", other)

    def __sub__(self, other: Any) -> Any:
        return self._apply_operation("__sub__", other)

    def __mul__(self, other: Any) -> Any:
        return self._apply_operation("__mul__", other)

    def __truediv__(self, other: Any) -> Any:
        return self._apply_operation("__truediv__", other)

    def __floordiv__(self, other: Any) -> Any:
        return self._apply_operation("__floordiv__", other)

    def __mod__(self, other: Any) -> Any:
        return self._apply_operation("__mod__", other)

    def __pow__(self, other: Any) -> Any:
        return self._apply_operation("__pow__", other)

    def _apply_operation(self, op_name: str, other: Any) -> Any:
        if hasattr(self, "_matrix"):
            matrix = self._matrix
        else:
            matrix = self
        op = getattr(matrix, op_name, None)
        if op is None:
            raise NotImplementedError(f"Operation {op_name} not supported")
        return op(other)


class FileOperationsMixin:
    def to_file(self, filename: str) -> None:
        content = str(self)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)


class StrMixin:
    def __str__(self) -> str:
        if hasattr(self, "_matrix"):
            return str(self._matrix)
        return super().__str__()


class PropertyMixin:
    @property
    def rows(self) -> int:
        if hasattr(self, "_matrix"):
            return self._matrix.rows
        return getattr(self, "_rows", 0)

    @rows.setter
    def rows(self, value: int) -> None:
        if hasattr(self, "_matrix"):
            self._matrix._rows = value
        else:
            self._rows = value

    @property
    def cols(self) -> int:
        if hasattr(self, "_matrix"):
            return self._matrix.cols
        return getattr(self, "_cols", 0)

    @cols.setter
    def cols(self, value: int) -> None:
        if hasattr(self, "_matrix"):
            self._matrix._cols = value
        else:
            self._cols = value

    @property
    def data(self) -> list:
        if hasattr(self, "_matrix"):
            return self._matrix.data
        return getattr(self, "_data", [])

    @data.setter
    def data(self, value: list) -> None:
        if hasattr(self, "_matrix"):
            self._matrix._data = value
        else:
            self._data = value


class HashMixin:
    def __hash__(self) -> int:
        if hasattr(self, "_matrix"):
            matrix = self._matrix
        else:
            matrix = self

        total_sum = 0
        for row in matrix._data:
            for val in row:
                total_sum += val

        hash_value = int(total_sum * matrix._rows + matrix._rows * matrix._cols)
        return hash_value


class CacheMixin:
    def __init__(self, *args, **kwargs):
        if not hasattr(self, "_cache"):
            self._cache = {}

    def __matmul__(self, other: Any) -> Any:
        self_hash = hash(self)
        other_hash = hash(other)
        cache_key = (self_hash, other_hash)

        if cache_key in self._cache:
            return self._cache[cache_key]

        from .matrix import Matrix
        result_data = Matrix.__matmul__(self, other)
        result = type(self)(result_data._data)

        self._cache[cache_key] = result
        return result
