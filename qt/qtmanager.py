#!/usr/bin/env python3
import sys
import os
from PyQt5.QtWidgets import QApplication
from appconfig.appConfigScreen import appConfigScreen as appConfig
app=QApplication(["AirManager"])
config=appConfig("AirManager",{'app':app})
config.setRsrcPath("/usr/share/airmanager/rsrc")
config.setIcon('airmanager')
config.setBanner('airmanager_banner.png')
config.setBackgroundImage('airmanager_login.svg')
config.setConfig(confDirs={'system':'/usr/share/airmanager','user':'%s/.config'%os.environ['HOME']},confFile="airmanager.conf")
config.Show()
config.setFixedSize(config.width(),config.height())

app.exec_()
