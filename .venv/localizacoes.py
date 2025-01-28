from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys

class Localizações (QWidget):
    def __init__(self):
        super().__init__()
        # vamos definir a posição e o tamanho da tela
        self.setGeometry(500, 200, 550, 300)
        # agora o título da janela
        self.setWindowTitle("Localização de Patrimônios")

        # Gerenciador de layout vertical
        self.layout_v = QVBoxLayout()

        # Labels e LineEdits para os dados do patrimônio
        self.label_id = QLabel("ID do Patrimônio:")
        self.label_id.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_id = QLineEdit()

        self.label_empresa = QLabel("Empresa:")
        self.label_empresa.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_empresa = QLineEdit()

        self.label_logradouro = QLabel("Logradouro:")
        self.label_logradouro.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_logradouro = QLineEdit()

        self.label_numero = QLabel("Número:")
        self.label_numero.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_numero = QLineEdit()

        self.label_predio = QLabel("Prédio:")
        self.label_predio.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_predio = QLineEdit()

        self.label_andar = QLabel("Andar:")
        self.label_andar.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_andar = QLineEdit()

        self.label_sala = QLabel("Sala:")
        self.label_sala.setStyleSheet("QLabel{font-size:12pt}")
        self.edit_sala = QLineEdit()

        #self.label_data_aquisicao = QLabel("Data de Aquisição:")
        #self.label_data_aquisicao.setStyleSheet("QLabel{font-size:12pt}")
        #self.edit_data_aquisicao = QLineEdit()

        # Adicionar as widgets ao layout
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)
        self.layout_v.addWidget(self.label_empresa)
        self.layout_v.addWidget(self.edit_empresa)
        self.layout_v.addWidget(self.label_logradouro)
        self.layout_v.addWidget(self.edit_logradouro)
        self.layout_v.addWidget(self.label_numero)
        self.layout_v.addWidget(self.edit_numero)
        self.layout_v.addWidget(self.label_predio)
        self.layout_v.addWidget(self.edit_predio)
        self.layout_v.addWidget(self.label_andar)
        self.layout_v.addWidget(self.edit_andar)
        self.layout_v.addWidget(self.label_sala)
        self.layout_v.addWidget(self.edit_sala)
        #self.layout_v.addWidget(self.label_data_aquisicao)
        #self.layout_v.addWidget(self.edit_data_aquisicao)

        # Botão de cadastro
        self.button = QPushButton("Cadastrar")
        self.button.clicked.connect(self.cadastrar)
        self.button.setStyleSheet("QPushButton{background-color:deepskyblue;color:white;font-size:12pt;font-weight:bold}")
        self.layout_v.addWidget(self.button)

        # Definir o layout da janela
        self.setLayout(self.layout_v)

    def cadastrar(self):
        # Vamos criar uma variável que fará referência ao arquivo de texto
        arquivo = open("localizacao.txt", "+a", encoding="utf-8") #+a é para entender os caracteres acentuados
        arquivo.write(f"ID: {self.edit_id.text()}\n")
        arquivo.write(f"Empresa: {self.edit_empresa.text()}\n")
        #arquivo.write(f"Nome do Patrimônio: {self.edit_empresa.text()}\n")
        arquivo.write(f"Logradouro: {self.edit_logradouro()}\n")
        arquivo.write(f"Número: {self.edit_numero.text()}\n")
        arquivo.write(f"Prédio: {self.edit_predio.text()}\n")
        arquivo.write(f"Andar: {self.edit_andar.text()}\n")
        arquivo.write(f"Sala: {self.edit_sala.text()}\n")
        arquivo.write("------------------------------------------\n")
        arquivo.close()
