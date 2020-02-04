#!/usr/bin/python3
import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton,QVBoxLayout,QLineEdit,QGridLayout,QHBoxLayout,QComboBox,QCheckBox, QListWidget
from PyQt5 import QtGui
from PyQt5.QtCore import Qt,QSize
from appconfig.appConfigStack import appConfigStack as confStack
from edupals.ui import QAnimatedStatusBar
import airmanager.airmanager as installer

import gettext
_ = gettext.gettext

class installAir(confStack):
	def __init_stack__(self):
		self.dbg=False
		self._debug("installer load")
		self.description=(_("Air Apps Installer"))
		self.menu_description=(_("Install air apps"))
		self.icon=('dialog-password')
		self.tooltip=(_("From here you can manage the air apps installed on your system"))
		self.index=2
		self.enabled=True
		self.level='system'
		self.hideControlButtons()
		self.airinstaller=installer.AirManager()	
	#def __init__
	
	def _load_screen(self):
		box=QGridLayout()
		box.addWidget(QLabel(_("App name")),0,0,1,1,Qt.AlignBottom)
		self.inp_name=QLineEdit()
		self.inp_name.setPlaceholderText(_("Application name"))
		box.addWidget(self.inp_name,1,0,1,1)
		self.btn_icon=QPushButton()
		self.btn_icon.setTool=QPushButton()
		self.btn_icon.setToolTip(_("Push for icon change"))
		box.addWidget(self.btn_icon,1,1,4,1,Qt.AlignTop)
		box.addWidget(QLabel(_("App description")),2,0,1,1,Qt.AlignBottom)
		self.inp_desc=QLineEdit()
		self.inp_desc.setPlaceholderText(_("Application description"))
		box.addWidget(self.inp_desc,3,0,1,1,Qt.AlignTop)
#		box.addWidget(self.lst_airApps)
		#self.btn_update=QPushButton(_("Update repositories"))
		#icn=QtGui.QIcon.fromTheme("view-refresh")
		#self.btn_update.setIcon(icn)
		#self.btn_update.setIconSize(QSize(48,48))
		#self.btn_update.clicked.connect(self._updateRepos)
		#btn_upgrade=QPushButton(_("Launch Lliurex-Up"))
		#icn=QtGui.QIcon.fromTheme("lliurex-up")
		#btn_upgrade.setIcon(icn)
		#btn_upgrade.setIconSize(QSize(48,48))
		#btn_upgrade.clicked.connect(self._launchUpgrade)
		#btn_install=QPushButton(_("Launch Lliurex-Store"))
		#icn=QtGui.QIcon.fromTheme("lliurex-store")
		#btn_install.setIcon(icn)
		#btn_install.setIconSize(QSize(48,48))
		#btn_install.clicked.connect(self._launchStore)
#		box.addWidget(self.statusBar,0,0,1,1)
		#box.addWidget(self.btn_update,Qt.AlignHCenter|Qt.AlignBottom)
		#box.addWidget(btn_upgrade,Qt.AlignHCenter)
		#box.addWidget(btn_install,Qt.AlignHCenter|Qt.AlignTop)
		self.setLayout(box)
		self.updateScreen()
		return(self)
	#def _load_screen

	def updateScreen(self):
		return True
	#def _udpate_screen

