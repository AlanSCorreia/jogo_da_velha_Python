class Matriz:
    matriz: list[list[str]] = [["-" for _ in range(3)] for _ in range(3)]

    def desenhar(self) -> None:
        for linha in self.matriz:
            print('#' * 13)

            for indice, elemento in enumerate(linha):
                match indice:
                    case 0 | 1:
                        print(f"# {elemento}", end=' ')
                        continue

                    case 2:
                        print(f"# {elemento} #", end=' ')
                        continue

                print(elemento, end=' ')
            print()

        print('#' * 13)

    def atualizar(self, posicao: list[int], letra: str) -> bool:
        if self.matriz[posicao[0]][posicao[1]] == ' ':

            self.matriz[posicao[0]][posicao[1]] = letra
            return True

        else:

            print("POSIÇÃO INVÁLIDA. Tente novamente.")
            return False


if __name__ == "__main__":
    matriz: Matriz = Matriz()
    matriz.desenhar()
    matriz.matriz[0][0] = 'a'
    matriz.desenhar()
