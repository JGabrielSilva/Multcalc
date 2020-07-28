from tkinter import *


class Janela(Tk):
    def __init__(self):
        super().__init__()

    def nome(self, nome:str='Janela principal'):
        super().title(nome)

    def dimensoes_com_espaco(self, largura=200, altura=200, espaco_a_direita=200, espaco_acima=200):
        super().geometry(f'{largura}x{altura}+{espaco_a_direita}+{espaco_acima}')

    def dimensoes(self, largura=200, altura=200):
        super().geometry(f'{largura}x{altura}')