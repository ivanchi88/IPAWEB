# -*- coding: utf-8 -*-

"""
	This simple web browser is mainly used for learning the basics of GUI programming with python.
	You are free to do anything you want with it, so I guess it is released under the GNU GPL license. 
	I've used the library PySide (wich is released under LGPL): https://pypi.python.org/pypi/PySide/1.2.4 

	If I can, I'll add more stuff so if you like it, keep an eye out for future "updates" :)

	Made by: Iván Motos Montalbán
"""

from PySide import QtCore, QtGui
from PySide import QtWebKit
from PySide import QtNetwork
import sys

class VentanaNav(QtGui.QWidget):

	def __init__(self):
		#The super() method returns the parent object of the Example class and we call its constructor
		super(VentanaNav, self).__init__(parent=None) #Tengo que investigarlo mas.
		self.crearPantallaPrincipal()
		self.CrearVentana()

	def CrearVentana(self):
		self.showMaximized()
		self.setWindowTitle("IPAWEB") # Nombre del programa
		self.setWindowIcon(QtGui.QIcon('main_icon.ico')) # Icono del programa

	#Pantalla Principal
	def crearPantallaPrincipal(self):
		#Crear la tabla principal
		self.mainLayout = QtGui.QGridLayout(self)
		self.crearTablas()

		#cosas raras
		self.webkitThings()
		#manejadores de eventos
		self.acciones()

	def crearTablas(self):
		#Crear las tablas secundarias
		self.gridLayout1 = QtGui.QGridLayout(self)
		self.gridLayout2 = QtGui.QGridLayout(self)
		self.gridLayout3 = QtGui.QGridLayout(self)

		#Añadir las tablas secundarias a la principal
		self.mainLayout.addLayout(self.gridLayout1, 0, 0)
		self.mainLayout.addLayout(self.gridLayout2, 1, 0,)
		self.mainLayout.addLayout(self.gridLayout3, 2, 0)
		#Rellenar las tablas
		self.tabla1()
		self.tabla2()
		self.tabla3()

	def tabla1(self):
		self.pestanyasLayout = QtGui.QGridLayout(self)
		self.gridLayout1.addLayout(self.pestanyasLayout, 0, 0, 0, 20)

		self.masPestanyas = QtGui.QPushButton(self, text = 'MAS')
		self.gridLayout1.addWidget(self.masPestanyas, 0, 19, 1, 1)

		self.btnMenu = QtGui.QPushButton(self, text = 'Menu')
		self.gridLayout1.addWidget(self.btnMenu, 0, 20, 1, 1)
		#QtGui.QWidget.hide(self.btnMenu)

	def tabla2(self):
		self.btnAtras = QtGui.QPushButton(self, text = 'Volver')
		self.gridLayout2.addWidget(self.btnAtras, 0, 0, 1, 1)

		self.btnAdelante = QtGui.QPushButton(self, text = 'Adelante')
		self.gridLayout2.addWidget(self.btnAdelante, 0, 1, 1, 1)

		self.direcc = QtGui.QLabel(u'Dirección', self)
		self.gridLayout2.addWidget(self.direcc, 0, 2, 1, 1)

		self.urlBox = QtGui.QLineEdit(self)
		self.gridLayout2.addWidget(self.urlBox, 0, 3, 1, 1)

	def tabla3(self):
		#El navegador en sí
		self.navegadorP = QtWebKit.QWebView(self)
		self.gridLayout3.addWidget(self.navegadorP, 0, 0, 1, 1)
		#Url de inicio
		_url = "http://www.google.es"
		self.urlBox.setText(str(_url))
		self.navegadorP.load(QtCore.QUrl(_url))
		
	'''
		self.navegadorV = QtWebKit.QWebView(self)
		self.gridLayout.addWidget(self.navegadorV, 2, 4, 1, 5)

		_url = "http://www.google.es"
		self.navegadorV.load(QtCore.QUrl(_url))

		#Se crea una 'segunda pantalla' que por defecto está oculta. *Tengo que implementar un menu con la opcion de mostrarla.
		self.navegadorH = QtWebKit.QWebView(self)
		self.gridLayout.addWidget(self.navegadorH, 4, 0, 1, 9)

		# QtGui.QWidget.hide(self.navegador2) # esto oculta navegadorH

	#De momento lo voy a ocultar, porque no se que sera mas eficiente, si ir creando y destruyendo o tan solo ocultando.
	'''

	def webkitThings(self): #Ni idea de que es esto, pero parece para activar funcionalidades extra. Investigar en un futuro.
		QtNetwork.QNetworkProxyFactory.setUseSystemConfiguration(True)
		QtWebKit.QWebSettings.globalSettings().setAttribute(
			QtWebKit.QWebSettings.PluginsEnabled, True)
		QtWebKit.QWebSettings.globalSettings().setAttribute(
			QtWebKit.QWebSettings.JavascriptCanOpenWindows, True)
		QtWebKit.QWebSettings.globalSettings().setAttribute(
			QtWebKit.QWebSettings.DeveloperExtrasEnabled, True)

	def acciones(self):
		QtCore.QObject.connect(
			self.urlBox,
			QtCore.SIGNAL('returnPressed()'),
			self.cargarUrl)

		QtCore.QObject.connect(
			self.btnAdelante,
			QtCore.SIGNAL('clicked()'),
			self.navegadorP.forward)

		QtCore.QObject.connect(
			self.btnAtras,
			QtCore.SIGNAL('clicked()'),
			self.navegadorP.back)

		self.navegadorP.connect(  #de lo que forma parte
			self.navegadorP,		#el "objeto" que se ve implicado
			QtCore.SIGNAL('urlChanged(QUrl)'),	#la senyal que recibe
			self.actualizarUrl		#lo que ocurre al recibir la senyal
			)

	def actualizarUrl(self):
		self.urlBox.setText(str(self.navegadorP.url().toString()))

	def cargarUrl(self):
		url = self.urlBox.text()
		if url.startswith('http://') or url.startswith('https://'):
			url = url 
		else:
			if url.startswith('www.'):
				url = 'http://' + str(url)
			else:
				url = 'https://www.google.es/#q=' + str(url) #Motor de busqueda predeterminado: google.
		self.navegadorP.load(QtCore.QUrl(url))
		self.urlBox.setText(url)

def main():
	app = QtGui.QApplication(sys.argv)
	VentanaNavegadorP = VentanaNav()
	VentanaNavegadorP.show()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	main()
