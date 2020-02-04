#!/usr/bin/python3
import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton,QVBoxLayout,QLineEdit,QGridLayout,QHBoxLayout,QComboBox,QCheckBox,QTableWidget, \
				QGraphicsDropShadowEffect, QHeaderView
from PyQt5 import QtGui
from PyQt5.QtCore import Qt,QSize
from appconfig.appConfigStack import appConfigStack as confStack
from edupals.ui import QAnimatedStatusBar
import airmanager.airmanager as installer
from app2menu import App2Menu

import gettext
_ = gettext.gettext

class manager(confStack):
	def __init_stack__(self):
		self.dbg=True
		self._debug("manager load")
		self.description=(_("Air Apps Manager"))
		self.menu_description=(_("Manage air apps"))
		self.icon=('dialog-password')
		self.tooltip=(_("From here you can manage the air apps installed on your system"))
		self.index=1
		self.enabled=True
		self.level='system'
		self.hideControlButtons()
		self.airinstaller=installer.AirManager()	
		self.menu=App2Menu.app2menu()
		self.setStyleSheet(self._setCss())
	#def __init__
	
	def _load_screen(self):
		box=QVBoxLayout()
		self.lst_airApps=QTableWidget(1,1)
		self.lst_airApps.setShowGrid(False)
		self.lst_airApps.horizontalHeader().hide()
		self.lst_airApps.verticalHeader().hide()
		self.lst_airApps.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		self.lst_airApps.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		box.addWidget(self.lst_airApps)
		self.setLayout(box)
		self.updateScreen()
		return(self)
	#def _load_screen

	def updateScreen(self):
		self.lst_airApps.clear()
		apps=self.airinstaller.get_installed_apps()
		cont=0
		for airapp,airinfo in apps.items():
			desktop=self.menu.get_desktop_info(airinfo.get('desktop',''))
			airCell=self._paintCell(desktop)
			if airCell:
				print("AirApp: %s"%airapp)
				self.lst_airApps.insertRow(cont)
				self.lst_airApps.setCellWidget(cont,0,airCell)
				self.lst_airApps.resizeRowToContents(cont)
				cont+=1
		return True
	#def _udpate_screen

	def _paintCell(self,desktop):
		widget=None
		name=desktop.get('Name','')
		if name:
			box=QGridLayout()
			widget=QWidget()
			effect=QGraphicsDropShadowEffect(blurRadius=5,xOffset=3,yOffset=3)
#			effect.setColor(QtGui.QColor(100,100,100,0))
			widget.setObjectName("cell")
			widget.setLayout(box)
			lbl_name=QLabel(name)
#			box.addWidget(lbl_name)
			icon=desktop.get('Icon','')
			if icon:
				qicon=None
				if QtGui.QIcon.hasThemeIcon(icon):
					qicon=QtGui.QIcon.fromTheme(icon)
				elif os.path.isfile(icon):
					qicon=QtGui.QIcon(icon)
				else:
					qicon=QtGui.QIcon.fromTheme("package-x-generic")
				if qicon:
					qbutton=QPushButton("")
					qbutton.setIcon(qicon)
					qbutton.setIconSize(QSize(64,64))
					qbutton.setMinimumHeight(72)
					box.addWidget(qbutton,0,0,2,1)
					qbutton.setGraphicsEffect(effect)
			lbl_name=QLabel(name)
			lbl_name.setObjectName("appName")
			box.addWidget(lbl_name,0,1,1,1)
			comment=desktop.get('Comment','')
			lbl_comment=QLabel(comment)
			box.addWidget(lbl_comment,1,1,1,2)
			btn_remove=QPushButton(_("Uninstall"))
			btn_remove.setObjectName("btnRemove")
			box.addWidget(btn_remove,0,2,1,1,Qt.AlignRight)
			widget.setToolTip("%s: %s"%(name,comment))
		return widget

	def _setCss(self):
		css="""
		#cell{
			padding:10px;
			margin:6px;
			background-color:rgb(250,250,250);

		}
		#appName{
			font-weight:bold;
			border:0px;
		}
		#btnRemove{
			background:red;
			color:white;
			font-size:9pt;
			padding:3px;
			margin:3px;
		}
		
		"""

		return(css)
	#def _setCss

