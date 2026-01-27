#  PySide6 para GUI (interface gráfica) com Qt em Python - Instalação
# A seção original desse curso usou PyQt5 (estamos atualizando para PySide6)
# Essas bibliotecas (PySide e PyQt) usam a biblioteca Qt
# Qt é uma biblioteca usada para a criação de GUI (interface gráfica do usuário) escrita em C++.
# PySide e PyQt conseguem fazer a ponte (binding) entre o Python e a biblioteca para a criação de interfaces gráficas sem ter que usar outra linguagem de programação.
# PySide6 é uma referencia à versão 6 da Qt (Qt 6)
# Qt é multiplataforma, ou seja, deve funcionar em Windows, Linux e Mac.

# Por que mudei de PyQt para PySide na atualização?
# PySide foi desenvolvido pela The Qt Company (da Nokia), como parte do projeto Qt for Python project - https://doc.qt.io/qtforpython/
# Por usarem a mesma biblioteca (Qt), PySide e PyQt são extremamente similares, muitas vezes os códigos são idênticos. Portanto, mesmo que você ainda queira usar PyQt, será muito simples portar os códigos. Muitas vezes basta trocar o nome de PySide para PyQt e vice-versa.
# A maior diferença entre PyQt e PySide está na licença:
# PyQt usa GPL ou commercial e PySide usa LGPL.
# Em resumo: com PySide, você tem a permissão uso da biblioteca para fins       comerciais, sem ter que compartilhar o código escrito por você para o público.
# Licenças são tópicos complexos, portanto, se oriente sobre elas antes de usar qualquer software de terceiros.
# https://tldrlegal.com/license/gnu-lesser-general-public-license-v3-(lgpl-3)

#import PySide6.QtCore

# Prints PySide6 version
#print(PySide6.__version__)

# Prints the Qt version used to compile PySide6
#print(PySide6.QtCore.__version__) #type: ignore

# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6

import sys
from PySide6.QtWidgets import QApplication, QPushButton, QTabWidget, QWidget, QMainWindow
from PySide6.QtCore import QSize, Qt, Slot
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout
            # HBox para horizontal, VBox para vertical, QGrid para criar um grid
            
class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = QWidget()

        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Minha janela bonita')

        # Botão
        self.botao1 = self.make_button('Texto do botão')
        self.botao1.clicked.connect(self.segunda_acao_marcada)  # type: ignore

        self.botao2 = self.make_button('Botão 2')

        self.botao3 = self.make_button('Terceiro')

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.botao1, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.botao2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.botao3, 3, 1, 1, 2)

        # statusBar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mostrar mensagem na barra')

        # menuBar
        self.menu = self.menuBar()
        self.primeiro_menu = self.menu.addMenu('Primeiro menu')
        self.primeira_acao = self.primeiro_menu.addAction('Primeira ação')
        self.primeira_acao.triggered.connect(  # type:ignore
            self.muda_mensagem_da_status_bar)

        self.segunda_action = self.primeiro_menu.addAction('Segunda ação')
        self.segunda_action.setCheckable(True)
        self.segunda_action.toggled.connect(  # type:ignore
            self.segunda_acao_marcada)
        self.segunda_action.hovered.connect(  # type:ignore
            self.segunda_acao_marcada)

    @Slot()
    def muda_mensagem_da_status_bar(self):
        self.status_bar.showMessage('O meu slot foi executado')

    @Slot()
    def segunda_acao_marcada(self):
        print('Está marcado?', self.segunda_action.isChecked())

    def make_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet('font-size: 80px;')
        return btn


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()  # O loop da aplicação