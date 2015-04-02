#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Name: PyQML Box Questionnaire
Purpose: Python interaction with QtQuick 1 questionnaire app
Date: 05-2014
Author: donK23 (datadonk23@gmail.com)
"""

import sys, csv
from PyQt4 import QtCore, QtGui
from PyQt4.QtDeclarative import QDeclarativeView
 
# Qt application and QDeclarative view
app = QtGui.QApplication(sys.argv)
view = QDeclarativeView()
url = QtCore.QUrl('main.qml')
view.setSource(url)
view.show()

# Reset output file and write column labels
with open("./data/output.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(("id", "Item01", "Item02", "Item03",
                     "Item04", "Item05", "Item06"))

def valSlot(s):
    """ Slot for values from qtquick """
    converted_list = s.toPyObject()
    writeValues(converted_list)

def writeValues(values):
    """ Append item values to csv file """
    with open("./data/output.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow(values)

# root object
mainRec = view.rootObject()
# Get value from slot
mainRec.emitValue.connect(valSlot)

# Qt main loop
sys.exit(app.exec_())
