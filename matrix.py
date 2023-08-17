class Matrix:
    matrix: list[list[str]] = [[" " for _ in range(3)] for _ in range(3)]

    def draw(self) -> None:
        print()

        for line in self.matrix:
            print('#' * 13)

            for index, element in enumerate(line):
                match index:
                    case 0 | 1:
                        print(f"# {element}", end=' ')
                        continue

                    case 2:
                        print(f"# {element} #", end=' ')
                        continue

                print(element, end=' ')
            print()

        print('#' * 13)
        print()

    def update(self, inner_function, letter: str) -> None:
        while True:
            position = inner_function()

            if self.matrix[position[0]][position[1]] == ' ':
                self.matrix[position[0]][position[1]] = letter
                break

            else:
                print("POSIÇÃO INVÁLIDA. Tente novamente.")


if __name__ == "__main__":
    matrix: Matrix = Matrix()
    matrix.draw()
    matrix.update([0, 0], 'X')
    matrix.draw()
