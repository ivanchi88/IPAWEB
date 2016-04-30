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
		self.setWindowFlags(self.windowFlags())

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
		self.masPestanyas.setIcon(QtGui.QIcon('more.ico'))
		self.gridLayout1.addWidget(self.masPestanyas, 0, 17, 1, 1)

		self.btnMin = QtGui.QPushButton(self)
		self.btnMin.setIcon(QtGui.QIcon('min.ico'))
		self.gridLayout1.addWidget(self.btnMin, 0, 18, 1, 1 )

		self.btnMax = QtGui.QPushButton(self)
		self.btnMax.setIcon(QtGui.QIcon('max.ico'))
		self.gridLayout1.addWidget(self.btnMax, 0, 19, 1, 1 )

		self.btnQuitar = QtGui.QPushButton(self)
		self.btnQuitar.setIcon(QtGui.QIcon('close.ico'))
		self.gridLayout1.addWidget(self.btnQuitar, 0, 20, 1, 1 )

		#QtGui.QWidget.hide(self.btnMenu)

	def tabla2(self):
		self.btnAtras = QtGui.QPushButton(self)
		self.btnAtras.setIcon(QtGui.QIcon('back_button.ico'))
		self.gridLayout2.addWidget(self.btnAtras, 0, 0, 1, 1)

		self.btnAdelante = QtGui.QPushButton(self)
		self.btnAdelante.setIcon(QtGui.QIcon('next_button.ico'))
		self.gridLayout2.addWidget(self.btnAdelante, 0, 1, 1, 1)

		self.btnReload = QtGui.QPushButton(self)
		self.btnReload.setIcon(QtGui.QIcon('reload.ico'))
		self.gridLayout2.addWidget(self.btnReload, 0, 2, 1, 1)

		self.direcc = QtGui.QLabel(u'Dirección', self)
		self.gridLayout2.addWidget(self.direcc, 0, 3, 1, 1)

		self.urlBox = QtGui.QLineEdit(self)
		self.gridLayout2.addWidget(self.urlBox, 0, 4, 1, 1)

		self.btnHome = QtGui.QPushButton(self)
		self.btnHome.setIcon(QtGui.QIcon('home.ico'))
		self.gridLayout2.addWidget(self.btnHome, 0, 5, 1, 1)

		self.btnMenu = QtGui.QPushButton(self)
		self.btnMenu.setIcon(QtGui.QIcon('settings.ico'))
		self.gridLayout2.addWidget(self.btnMenu, 0, 6, 1, 1)

	def tabla3(self):
		#El navegador en sí
		self.navegadorP = QtWebKit.QWebView(self)
		self.gridLayout3.addWidget(self.navegadorP, 0, 0, 1, 1)
		#Url de inicio
		self.cargarInicio()
		
	'''	
		self.navegador2 = QtWebKit.QWebView(self)
		self.gridLayout3.addWidget(self.navegador2, 0, 1, 1, 1)
		self.navegador2.load(QtCore.QUrl(_url))

		self.navegador3 = QtWebKit.QWebView(self)
		self.gridLayout3.addWidget(self.navegador3, 1, 0, 1, 1)
		self.navegador3.load(QtCore.QUrl(_url))

		self.navegador4 = QtWebKit.QWebView(self)
		self.gridLayout3.addWidget(self.navegador4, 1, 1, 1, 1)
		self.navegador4.load(QtCore.QUrl(_url))

		# QtGui.QWidget.hide(self.navegadorV) # esto oculta navegadorV

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
		''' #faltan cosas por pulir
		QtCore.QObject.connect(
			self.gridLayout1,
			QtCore.SIGNAL('clicked()'),
			self.moverVentana
			)
		'''
		#tabla1
		QtCore.QObject.connect(
			self.btnQuitar,
			QtCore.SIGNAL('clicked()'),
			exit
			)
		QtCore.QObject.connect(
			self.btnMax,
			QtCore.SIGNAL('clicked()'),
			self.maximizar
			)
		QtCore.QObject.connect(
			self.btnMin,
			QtCore.SIGNAL('clicked()'),
			self.minimizar
			)

		#tabla 2
		QtCore.QObject.connect(
			self.btnAdelante,
			QtCore.SIGNAL('clicked()'),
			self.navegadorP.forward
			)

		QtCore.QObject.connect(
			self.btnAtras,
			QtCore.SIGNAL('clicked()'),
			self.navegadorP.back
			)

		QtCore.QObject.connect(
			self.btnReload,
			QtCore.SIGNAL('clicked()'),
			self.navegadorP.reload
			)

		QtCore.QObject.connect(
			self.urlBox,
			QtCore.SIGNAL('returnPressed()'),
			self.cargarUrl
			)

		QtCore.QObject.connect(
			self.btnHome,
			QtCore.SIGNAL('clicked()'),
			self.cargarInicio
			)

		#tabla3
		self.navegadorP.connect(  #de lo que forma parte
			self.navegadorP,		#el "objeto" que se ve implicado
			QtCore.SIGNAL('urlChanged(QUrl)'),	#la senyal que recibe
			self.actualizarUrl		#lo que ocurre al recibir la senyal
			)
	''' faltan cosas por pulir
	def moverVentana(self):
		self.maximizar()
		self.move(QtGui.QMouseEvent.globalPos())
	'''
	def maximizar (self):
		if self.isMaximized() == False:
			self.showMaximized()
		else:
			self.showNormal()

	def minimizar (self):
			self.showMinimized()

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

	def cargarInicio(self):
		_url = "http://www.google.es"
		self.urlBox.setText(str(_url))
		self.navegadorP.load(QtCore.QUrl(_url))

def main():
	app = QtGui.QApplication(sys.argv)
	app.setWindowIcon(QtGui.QIcon('main_icon.ico')) # Icono del programa
	VentanaNavegadorP = VentanaNav()
	VentanaNavegadorP.show()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	main()
