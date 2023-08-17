class Players:
    def __init__(self):
        self.player1 = 'X'
        self.player2 = 'O'
        self.actual_player = self.player1

    def switch_player(self):
        match self.actual_player:
            case self.player1:
                self.actual_player = self.player2

            case self.player2:
                self.actual_player = self.player1

    @staticmethod
    def choose_position():
        def inner(n):
            output = None

            while output not in range(1, 4):
                try:
                    output = int(input(f"Informe uma das {n} [ 1 / 2 / 3 ]: "))
                    if output not in range(1, 4):
                        print("Informe um número válido. [ 1 / 2 / 3]")
                except ValueError:
                    print("Informe um valor númerico de 1 a 3.")

            return output

        return [inner("linhas") - 1, inner("colunas") - 1]


if __name__ == "__main__":
    players = Players()
    print(players.choose_position())
