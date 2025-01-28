import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from patrimonio import CadastroPatrimonio
from localizacoes import Localizações

class TelaInicial(QWidget):
    def __init__(self):#inicializa nossa janela, tudo que esta dentro sera executado por ele
        super().__init__()
        self.setWindowTitle("Gerenciar")
        self.setGeometry(300,200,200,150)
        
        self.layout_v = QVBoxLayout()

        self.label_titulo = QLabel("Clique para abrir a janela")
        self.button = QPushButton ("Abrir Patrimônio")
        self.label_titulo = QLabel("Clique para abrir a janela")
        self.button2 = QPushButton ("Abrir Localizações")

        self.layout_v.addWidget(self.label_titulo)
        self.layout_v.addWidget(self.button)
        self.layout_v.addWidget(self.button2)

        self.button.clicked.connect(self.abrir_cadastro) #nao esta dentro do def, precisa criar outro def, essa linha é so a chamada
        self.button2.clicked.connect(self.abrir_localizacoes)
        self.setLayout(self.layout_v)

    def abrir_cadastro(self):
        self.pat = CadastroPatrimonio()
        self.pat.show()

    def abrir_localizacoes(self):
        self.loc = Localizações()
        self.loc.show()
        
app =QApplication(sys.argv)
tela = TelaInicial()
tela.show()
app.exec()
