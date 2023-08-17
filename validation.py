class MatrixValidation:
    @staticmethod
    def __left_diagonal(matrix: list[list[str]], letter: str) -> bool:
        return matrix[0][0] == matrix[1][1] == matrix[2][2] == letter

    @staticmethod
    def __right_diagonal(matrix: list[list[str]], letter: str) -> bool:
        return matrix[0][2] == matrix[1][1] == matrix[2][0] == letter

    @staticmethod
    def __line(matrix: list[list[str]], letter: str) -> bool:
        return any([matrix[n][0] == matrix[n][1] == matrix[n][2] == letter for n in range(3)])

    @staticmethod
    def __column(matrix: list[list[str]], letter: str) -> bool:
        return any([matrix[0][n] == matrix[1][n] == matrix[2][n] == letter for n in range(3)])

    def validate(self, matrix: list[list[str]], letter: str) -> bool:
        return any([self.__left_diagonal(matrix, letter),
                   self.__right_diagonal(matrix, letter),
                   self.__line(matrix, letter),
                   self.__column(matrix, letter)])


if __name__ == "__main__":
    print(any([False, False, 1]))
