#!/usr/bin/env python3
import  airmanager.airmanager as installer
import sys
import subprocess
import tempfile

installer=installer.AirManager()
err=0
dbg=True

def _debug(msg):
	if dbg:
		print("Helper: %s"%msg)
#def _debug

if sys.argv[1]=='install':
	airFile=sys.argv[2]
	if (len(sys.argv))==4:
		iconFile=sys.argv[3]
	else:
		air_info=installer.get_air_info(airFile)
		if 'pb' in air_info.keys():
			if air_info['pb']:
				iconFile=tempfile.mkstemp()[1]
				iconFileTmp=air_info['pb']
				iconFileTmp.savev(iconFile,'png',[""],[""])

	_debug("Installing %s %s"%(airFile,iconFile))
	err=installer.install(airFile,iconFile)
	try:
		subprocess.check_call(['gtk-update-icon-cache','/usr/share/icons/hicolor/'])
	except:
		err=1
	os.remove(iconFile)
elif sys.argv[1]=='remove':
	_debug("Removing %s %s"%(sys.argv[2],sys.argv[3]))
	air_pkg={'desktop':sys.argv[3],'air_id':sys.argv[2]}
	err=installer.remove_air_app(air_pkg)
	try:
		subprocess.check_call(['gtk-update-icon-cache','/usr/share/icons/hicolor/'])
	except:
		err=1

exit(err)

