import math
import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QApplication, QLineEdit, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QWidget, QButtonGroup, QGridLayout, QScrollArea, QTableWidget, \
    QTableWidgetItem, QToolBar, QAction

from cliente import Cliente


class Consulta_datos_tabular(QMainWindow):
    def __init__(self, anterior):
        super().__init__()

        self.Anterior = anterior
        # creacion de la ventana
        self.setWindowTitle("Usuarios Registrados")
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
        self.vertical = QVBoxLayout()

        self.file = open('datos/clientes.txt', 'rb')
        self.usuarios = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')
            lista = linea.split(";")

            if linea == '':
                break

            u = Cliente(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8],
                lista[9],
                lista[10]
            )

            self.usuarios.append(u)
        self.file.close()

        self.numeroUsuarios = len(self.usuarios)
        self.contador = 0

        # ---- Construccion del toolbar----
        self.toolbar = QToolBar('Main Toolbar')
        self.toolbar.setIconSize(QSize(25, 25))
        self.addToolBar(self.toolbar)

        # toolbar eliminar
        self.delete = QAction(QIcon('imagenes/delete.jpg'), "&delete", self)
        self.delete.triggered.connect(self.accion_delete)
        self.toolbar.addAction(self.delete)

        # toolbar agregar
        self.agregar = QAction(QIcon('imagenes/agregar.png'), "&agregar", self)
        self.agregar.triggered.connect(self.accion_agregar)
        self.toolbar.addAction(self.agregar)

        # toolbar editar
        self.editar = QAction(QIcon('imagenes/editar.png'), "&editar", self)
        self.editar.triggered.connect(self.acciion_editar)
        self.toolbar.addAction(self.editar)

        # ---- Fin toolbar------

        # hacemos los labels informativos
        self.letrero1 = QLabel()
        self.letrero1.setText("Usuario registrado")
        self.letrero1.setFont(QFont("Arial", 20))
        self.letrero1.setStyleSheet('color: black;')

        self.vertical.addWidget(self.letrero1)
        self.vertical.addStretch()

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)


        # para crear la tabla para que se vean de forma tabular
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(11)

        # definimos los numeros de colimnas que tendra la tabla

        self.tabla.setColumnWidth(0, 150)
        self.tabla.setColumnWidth(1, 150)
        self.tabla.setColumnWidth(2, 150)
        self.tabla.setColumnWidth(3, 150)
        self.tabla.setColumnWidth(4, 150)
        self.tabla.setColumnWidth(5, 150)
        self.tabla.setColumnWidth(6, 150)
        self.tabla.setColumnWidth(7, 150)
        self.tabla.setColumnWidth(8, 150)
        self.tabla.setColumnWidth(9, 150)
        self.tabla.setColumnWidth(10, 150)

        self.tabla.setHorizontalHeaderLabels(["Nombre",
                                              "Usuario",
                                              "Contraseña",
                                              "Documento",
                                              "Correo",
                                              "Pregunta 1",
                                              "Pregunta 2",
                                              "Pregunta 3",
                                              "Respuesta 1",
                                              "Respuesta 2",
                                              "Respuesta 3"
                                              ])

        self.tabla.setRowCount(self.numeroUsuarios)

        for u in self.usuarios:
            self.tabla.setItem(self.contador, 0, QTableWidgetItem(u.nombreCompleto))
            # evitar que se deje modificar
            self.tabla.item(self.contador, 0).setFlags(Qt.ItemIsEnabled)
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.usuario))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.contrasena))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.documento))
            # evitar que se deje modificar
            self.tabla.item(self.contador, 3).setFlags(Qt.ItemIsEnabled)
            self.tabla.setItem(self.contador, 4, QTableWidgetItem(u.correo))
            self.tabla.setItem(self.contador, 5, QTableWidgetItem(u.respuesta1))
            self.tabla.setItem(self.contador, 6, QTableWidgetItem(u.respuesta2))
            self.tabla.setItem(self.contador, 7, QTableWidgetItem(u.respuesta3))
            self.tabla.setItem(self.contador, 8, QTableWidgetItem(u.respuesta4))
            self.tabla.setItem(self.contador, 9, QTableWidgetItem(u.respuesta5))
            self.tabla.setItem(self.contador, 10, QTableWidgetItem(u.respuesta6))

            self.contador += 1

        self.scrollArea.setWidget(self.tabla)
        self.vertical.addWidget(self.scrollArea)

        self.vertical.addStretch()


        # Boton volver

        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(100)
        self.botonVolver.setStyleSheet('background-color: #008B45;'
                                       'color:#FFFFFF;'
                                       'padding:5px;')

        self.botonVolver.clicked.connect(self.metodo_botonVolver)

        # Se agrega el boton al layout vertical

        self.vertical.addWidget(self.botonVolver)


        self.fondo.setLayout(self.vertical)


    def metodo_botonVolver(self):
        self.hide()
        self.Anterior.show()

    def accion_delete(self):
        pass

    def accion_agregar(self):
        pass

    def acciion_editar(self):
        pass