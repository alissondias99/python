from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
       
        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)

        self.setWindowTitle('Calculadora')

    def adjustFixedSize(self):
        self.adjustSize() # a janela vai se adaptar aos textos dentro dela
        self.setFixedSize(self.width(), self.height()) # não será possivel alterar a altura ou largura da janela


    def addWidgetToLayout(self, widget: QWidget): # boa pratica que diminui a quantidade de níveis em window.adjustFixedSize() do main.py
        self.v_layout.addWidget(widget)