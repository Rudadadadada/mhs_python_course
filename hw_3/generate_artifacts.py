import numpy as np
from pathlib import Path

from hw_3.matrix import Matrix
from hw_3.matrix_with_mixins import MatrixWithMixins, CachedMatrix


ARTIFACTS_DIR = Path(__file__).parent / "artifacts"


def task_3_1():
    print("Выполнение задания 3.1...")
    np.random.seed(0)
    data1 = np.random.randint(0, 10, (10, 10)).tolist()
    data2 = np.random.randint(0, 10, (10, 10)).tolist()

    matrix1 = Matrix(data1)
    matrix2 = Matrix(data2)

    result_add = matrix1 + matrix2
    result_mul = matrix1 * matrix2
    result_matmul = matrix1 @ matrix2

    result_add.to_file(ARTIFACTS_DIR / "matrix+.txt")
    result_mul.to_file(ARTIFACTS_DIR / "matrix*.txt")
    result_matmul.to_file(ARTIFACTS_DIR / "matrix@.txt")

    print("Артефакты задания 3.1 созданы.")


def task_3_2():
    print("Выполнение задания 3.2...")
    np.random.seed(0)
    data1 = np.random.randint(0, 10, (10, 10)).tolist()
    data2 = np.random.randint(0, 10, (10, 10)).tolist()

    matrix1 = MatrixWithMixins(data1)
    matrix2 = MatrixWithMixins(data2)

    result_add = matrix1 + matrix2
    result_mul = matrix1 * matrix2
    result_matmul = matrix1 @ matrix2

    result_add.to_file(ARTIFACTS_DIR / "matrix+.txt")
    result_mul.to_file(ARTIFACTS_DIR / "matrix*.txt")
    result_matmul.to_file(ARTIFACTS_DIR / "matrix@.txt")

    print("Артефакты задания 3.2 созданы.")


def task_3_3():
    print("Выполнение задания 3.3...")
    print("Поиск коллизии в хэш-функции...")

    A_data = [[1, 1], [1, 1]]
    C_data = [[2, 0], [0, 2]]
    B_data = [[1, 0], [0, 1]]
    D_data = [[1, 0], [0, 1]]

    A = CachedMatrix(A_data)
    B = CachedMatrix(B_data)
    C = CachedMatrix(C_data)
    D = CachedMatrix(D_data)

    print(f"hash(A) = {hash(A)}")
    print(f"hash(C) = {hash(C)}")
    print(f"A == C: {A == C}")
    print(f"B == D: {B == D}")

    if hash(A) == hash(C) and A != C and B == D:
        AB = A @ B
        CD = C @ D

        print(f"A @ B == C @ D: {AB == CD}")

        if AB != CD:
            print("Коллизия найдена!")

            A.to_file(ARTIFACTS_DIR / "A.txt")
            B.to_file(ARTIFACTS_DIR / "B.txt")
            C.to_file(ARTIFACTS_DIR / "C.txt")
            D.to_file(ARTIFACTS_DIR / "D.txt")
            AB.to_file(ARTIFACTS_DIR / "AB.txt")
            CD.to_file(ARTIFACTS_DIR / "CD.txt")

            with open(ARTIFACTS_DIR / "hash.txt", "w", encoding="utf-8") as f:
                f.write(f"hash(A) = {hash(A)}\n")
                f.write(f"hash(C) = {hash(C)}\n")
                f.write(f"hash(AB) = {hash(AB)}\n")
                f.write(f"hash(CD) = {hash(CD)}\n")

            print("Артефакты задания 3.3 созданы.")
        else:
            print("Ошибка: A @ B == C @ D, но должно быть разным!")
    else:
        print("Ошибка: условия коллизии не выполнены!")


def main():
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

    task_3_1()
    print()
    task_3_2()
    print()
    task_3_3()


if __name__ == "__main__":
    main()
