import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QApplication, QLineEdit, \
    QPushButton


class Ventana1(QMainWindow):
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

        # creacion de la ventana
        self.setWindowTitle("Formulario de registro")
        self.setWindowIcon(QtGui.QIcon('imagenes/mochila_clase9.jpg'))
        self.ancho = 900
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap('imagenes/kamehouse.jpg')
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)

        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        self.setCentralWidget(self.fondo)

        # creacion de layout horizontal para la distribucion
        self.horizontal = QHBoxLayout()

        self.horizontal.setContentsMargins(30, 30, 30, 30)

        # ---------Creacion del layout izquierdo---------
        self.layoutIzq_form = QFormLayout()

        # hacemos los labels informativos
        self.letrero1 = QLabel()
        self.letrero1.setText("Información del cliente")
        self.letrero1.setFont(QFont("Arial", 20))
        self.letrero1.setStyleSheet('color: black;')

        self.letrero2 = QLabel()
        self.letrero2.setFixedWidth(355)
        self.letrero2.setText("Por favor ingrese la información del cliente"
                              "\nen el formulario de abajo. los campos marcados"
                              "\ncon asterisco son obligatorios."
                              )
        self.letrero2.setFont(QFont("Arial", 10))
        self.letrero2.setStyleSheet('color: black; margin-bottom: 40px;'
                                    'margin-top: 25px;'
                                    'padding-bottom: 10;'
                                    'border: 2px solid black;'
                                    'border-left: none;'
                                    'border-right: none;'
                                    'border-top: none;'
                                    )

        # labels y campos
        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        self.contrasena = QLineEdit()
        self.contrasena.setFixedWidth(250)
        self.contrasena.setEchoMode(QLineEdit.Password)

        self.confirmar_contrasena = QLineEdit()
        self.confirmar_contrasena.setFixedWidth(250)
        self.confirmar_contrasena.setEchoMode(QLineEdit.Password)

        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)
        self.documento.setMaxLength(10)

        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)
        # Creacion de botones limpiar y registrar

        self.botonregistrar = QPushButton("Registrar")
        self.botonregistrar.setFixedWidth(90)
        self.botonregistrar.setStyleSheet('background-color: #008845;'
                                          'color: #FFFFFF;'
                                          'padding: 10px;'
                                          'margin-top: 40px;'
                                          )
        self.botonregistrar.clicked.connect(self.accionRegistrar)

        self.botonlimpiar = QPushButton("Limpiar")
        self.botonlimpiar.setFixedWidth(90)
        self.botonlimpiar.setStyleSheet('background-color: #008845;'
                                        'color: #FFFFFF;'
                                        'padding: 10px;'
                                        'margin-top: 40px;'
                                        )
        self.botonlimpiar.clicked.connect(self.accionLimpiar)

        # Se agrega todo al layout formulario izquierdo
        self.layoutIzq_form.addRow(self.letrero1)
        self.layoutIzq_form.addRow(self.letrero2)
        self.layoutIzq_form.addRow("Nombre completo*", self.nombreCompleto)
        self.layoutIzq_form.addRow("Ingrese usuario*", self.usuario)
        self.layoutIzq_form.addRow("Ingrese contraseña*", self.contrasena)
        self.layoutIzq_form.addRow("Confirmar contraseña*", self.confirmar_contrasena)
        self.layoutIzq_form.addRow("Documento ID*", self.documento)
        self.layoutIzq_form.addRow("Correo*", self.correo)
        self.layoutIzq_form.addRow(self.botonregistrar, self.botonlimpiar)

        # Agregamos layout formulario al layout horizontal
        self.horizontal.addLayout(self.layoutIzq_form)

        # --------Layout que almacena toda la ventana----------
        self.fondo.setLayout(self.horizontal)

    def accionRegistrar(self):
        pass

    def accionLimpiar(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana1 = Ventana1()
    ventana1.show()
    sys.exit(app.exec())
