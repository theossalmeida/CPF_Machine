from backend import valida_cpf, gerador_cpf
from PyQt5.QtWidgets import QApplication, QMainWindow
import design
import sys


class GeraValidaCPF(QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnGerar.clicked.connect(self.gerar_cpf)
        self.btnValidar.clicked.connect(self.validar_cpf)

    def gerar_cpf(self):
        self.saidaResultado.setText(
            str(gerador_cpf())
        )
    
    def validar_cpf(self):
        cpf = self.inputValidar.text()
        if valida_cpf(cpf) == True:
            self.saidaResultado.setText('O CPF é válido.')
        else:
            self.saidaResultado.setText('O CPF é inválido.')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gera_valida_cpf = GeraValidaCPF()
    gera_valida_cpf.show()
    qt.exec_()
