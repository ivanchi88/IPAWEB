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
		self.gridLayout = QtGui.QGridLayout(self)

		self.btnAtras = QtGui.QPushButton(self, text = 'Volver')
		self.gridLayout.addWidget(self.btnAtras, 1, 0, 1, 1)

		self.btnAdelante = QtGui.QPushButton(self, text = 'Adelante')
		self.gridLayout.addWidget(self.btnAdelante, 1, 1, 1, 1)

		self.direcc = QtGui.QLabel(u'Dirección', self)
		self.gridLayout.addWidget(self.direcc, 1, 2, 1, 1)

		self.urlBox = QtGui.QLineEdit(self)
		self.gridLayout.addWidget(self.urlBox, 1, 3, 1, 1)

		'''
		self.btnMenu = QtGui.QPushButton(self, text = 'Menu')
		self.gridLayout.addWidget(self.btnMenu, 0, 0, 1, 1)
		QtGui.QWidget.hide(self.btnMenu)
		'''
		self.navegadorP = QtWebKit.QWebView(self)
		self.gridLayout.addWidget(self.navegadorP, 2, 0, 1, 4)

		#Url de inicio
		_url = "http://www.google.es"
		self.navegadorP.load(QtCore.QUrl(_url))
		#cosas raras
		self.webkitThings()
		#manejadores de eventos
		self.acciones()

	'''
	#Segunda Pantalla Vertical
	def SegundaPantallaVer(self):

		self.btnAtrasV = QtGui.QPushButton(self, text = 'Volver')
		self.gridLayout.addWidget(self.btnAtrasV, 1, 4, 1, 1)

		self.btnAdelanteV = QtGui.QPushButton(self, text = 'Adelante')
		self.gridLayout.addWidget(self.btnAdelanteV, 1, 5, 1, 1)

		self.direccV = QtGui.QLabel(u'Dirección', self)
		self.gridLayout.addWidget(self.direccV, 1, 6, 1, 1)

		self.urlBoxV = QtGui.QLineEdit(self)
		self.gridLayout.addWidget(self.urlBoxV, 1, 8, 1, 1)

		self.navegadorV = QtWebKit.QWebView(self)
		self.gridLayout.addWidget(self.navegadorV, 2, 4, 1, 5)

		_url = "http://www.google.es"
		self.navegadorV.load(QtCore.QUrl(_url))

	#Ocultar la segunda pantalla vertical
	def ocultarSecPantVer(self):
		QtGui.QWidget.hide(self.btnAtrasV)
		QtGui.QWidget.hide(self.btnAdelanteV)
		QtGui.QWidget.hide(self.direccV)
		QtGui.QWidget.hide(self.urlBoxV)
		QtGui.QWidget.hide(self.navegadorV)

	def mostrarSecPantVer(self):
		QtGui.QWidget.show(self.btnAtrasV)
		QtGui.QWidget.show(self.btnAdelanteV)
		QtGui.QWidget.show(self.direccV)
		QtGui.QWidget.show(self.urlBoxV)
		QtGui.QWidget.show(self.navegadorV)

	#Segunda Pantalla Horizontal
	def SegundaPantallaHor(self):
		self.btnAtrasH = QtGui.QPushButton(self, text = 'Volver')
		self.gridLayout.addWidget(self.btnAtrasH, 3, 0, 1, 1)

		self.btnAdelanteH = QtGui.QPushButton(self, text = 'Adelante')
		self.gridLayout.addWidget(self.btnAdelanteH, 3, 1, 1, 1)

		self.direccH = QtGui.QLabel(u'Dirección', self)
		self.gridLayout.addWidget(self.direccH, 3, 2, 1, 1)

		self.urlBoxH = QtGui.QLineEdit(self)
		self.gridLayout.addWidget(self.urlBoxH, 3, 3, 1, 6)

		#Se crea una 'segunda pantalla' que por defecto está oculta. *Tengo que implementar un menu con la opcion de mostrarla.
		self.navegadorH = QtWebKit.QWebView(self)
		self.gridLayout.addWidget(self.navegadorH, 4, 0, 1, 9)
		# QtGui.QWidget.hide(self.navegador2) # esto oculto navegador2
		_url = "http://www.google.es"
		self.navegadorH.load(QtCore.QUrl(_url))
	#De momento lo voy a ocultar, porque no se que sera mas eficiente, si ir creando y destruyendo o tan solo ocultando.
	def ocultarSecPantHor(self):
		QtGui.QWidget.hide(self.btnAtrasH)
		QtGui.QWidget.hide(self.btnAdelanteH)
		QtGui.QWidget.hide(self.direccH)
		QtGui.QWidget.hide(self.urlBoxH)
		QtGui.QWidget.hide(self.navegadorH)

	def mostrarSecPantHor(self):
		QtGui.QWidget.show(self.btnAtrasH)
		QtGui.QWidget.show(self.btnAdelanteH)
		QtGui.QWidget.show(self.direccH)
		QtGui.QWidget.show(self.urlBoxH)
		QtGui.QWidget.show(self.navegadorH)
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
	
if __name__ == main():
	main()