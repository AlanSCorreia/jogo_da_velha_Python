class Jogadores:
    def __init__(self):

        self.jogador1 = 'X'
        self.jogador2 = 'O'
        self.jogador_atual = self.jogador1

    def trocar_atual(self):

        match self.jogador_atual:
            case self.jogador1:
                self.jogador_atual = self.jogador2

            case self.jogador2:
                self.jogador_atual = self.jogador1

    @staticmethod
    def escolher_posicao():
        def inner(n):
            output = None

            while output not in range(1, 4):
                try:
                    output = int(input(f"Informe um número para a {n} [ 1 / 2 / 3 ]: "))
                    if output not in range(1, 4):
                        print("Informe um número válido. [ 1 / 2 / 3]")
                except ValueError:
                    print("Informe um valor número de 1 a 3.")

            return output

        return [inner("linha") - 1, inner("coluna") - 1]


if __name__ == "__main__":
    jogadores = Jogadores()
    print(jogadores.escolher_posicao())
