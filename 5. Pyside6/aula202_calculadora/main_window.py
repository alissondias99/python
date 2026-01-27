from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QMessageBox

class MainWindow(QMainWindow):

    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
       
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        self.setWindowTitle('Calculadora')

    def adjustFixedSize(self):
        self.adjustSize() # a janela vai se adaptar aos textos dentro dela
        self.setFixedSize(self.width(), self.height()) # não será possivel alterar a altura ou largura da janela

    def addWidgetToVLayout(self, widget: QWidget): # boa pratica que diminui a quantidade de níveis em window.adjustFixedSize() do main.py
        self.vLayout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)