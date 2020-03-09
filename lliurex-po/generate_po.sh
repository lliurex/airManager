#!/bin/bash

MANAGER_PYTHON_FILES="../air-manager/src/*py"
INSTALLER_PYTHON_FILES="../air-installer/src/*py" 
UI_FILES="../air-manager/rsrc/*ui"

mkdir -p air-manager/ air-installer/

xgettext $UI_FILES $MANAGER_PYTHON_FILES -o air-manager/air-manager.pot

xgettext $INSTALLER_PYTHON_FILES -o air-installer/air-installer.pot

