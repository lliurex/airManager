#!/usr/bin/env python3
import sys
import os
from PySide2.QtWidgets import QApplication
from appconfig.appConfigScreen import appConfigScreen as appConfig
app=QApplication(["AirManager"])
config=appConfig("AirManager",{'app':app})
config.setRsrcPath("/usr/share/air-manager/rsrc")
config.setIcon('airmanager')
config.setBanner('air-manager_banner.png')
config.setBackgroundImage('drop_file.svg')
config.setConfig(confDirs={'system':'/usr/share/airmanager','user':'%s/.config'%os.environ['HOME']},confFile="airmanager.conf")
config.Show()
config.resize(config.width()+60,config.height()+60)

app.exec_()
