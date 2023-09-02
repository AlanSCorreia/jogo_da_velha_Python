import players
import validation
import matrix

PLAYERS = players.Players()
VALIDATION = validation.MatrixValidation()
matrix = matrix.Matrix()


def game_loop():
    for number in range(10):
        if number == 9:
            matrix.draw()
            print("EMPATE!")
            break

        else:
            matrix.draw()
            matrix.update(PLAYERS.choose_position, PLAYERS.actual_player)

            if VALIDATION.validate_win_condition(matrix.matrix, PLAYERS.actual_player):
                matrix.draw()
                print(f"O jogador {PLAYERS.actual_player} foi o VENCEDOR!")
                break

            PLAYERS.switch_player()

    print("FIM DE JOGO.")
