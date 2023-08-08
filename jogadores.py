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

    def escolher_posicao(self, linha_coluna):

        input_jogador = None
