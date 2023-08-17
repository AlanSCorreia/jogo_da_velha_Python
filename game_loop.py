import players
import validation
import matrix

players = players.Players()
validation = validation.MatrixValidation()
matrix = matrix.Matrix()


def game_loop():
    for number in range(10):
        if number == 9:
            matrix.draw()
            print("EMPATE!")
            break

        else:
            matrix.draw()
            matrix.update(players.choose_position, players.actual_player)

            if validation.validate(matrix.matrix, players.actual_player):
                matrix.draw()
                print(f"O jogador {players.actual_player} foi o VENCEDOR!")
                break

            players.switch_player()

    print("FIM DE JOGO.")
