##### imports #####
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from time import sleep
import sys
import os
import os.path
config_exist = os.path.isfile("isYrsInstalled")
##### imports end #####


def StartUp():
	os.system("clear")

StartUp()


if config_exist == False:
	f = open("isYrsInstalled", "a")
	f.write("True")
	f.close()
	os.system("pip install youtube-rss-subscriber")
else:
	f = open("isYrsInstalled", "r")
	print('Is Yrs Installed? :', f.read())
	f.close()


application = QApplication([])
mainWindow = QWidget()
layout = QGridLayout()
mainWindow.setLayout(layout)

label1 = QLabel('')

tabwidget = QTabWidget()
tabwidget.addTab(label1, "Main")
layout.addWidget(tabwidget, 0, 0)

mainWindow.setGeometry(0, 0, 310, 250)
mainWindow.setWindowTitle('PyRSS Client by : KorOwOzin')

def updateRSS():
    os.system("clear")
    print('Updating RSS Feed..')
    sleep(0.5)    
    os.system("yrs update")
    print('Done')

mainWindow.bb = QPushButton('Update RSS Feed', parent=label1)
mainWindow.bb.setToolTip('This is button will update the RSS Feed of your Subscribed Channels!')
mainWindow.bb.move(20,120)
mainWindow.bb.clicked.connect(updateRSS)

def showVideos():
    os.system("clear")
    os.system("yrs list-all-videos")

dispVid = QPushButton('Display ALL Vids', parent=label1)
dispVid.setToolTip('This is button will show the avaliable videos from ALL of your Subbed Channels!')
dispVid.move(20,160)
dispVid.clicked.connect(showVideos)

def showChannels():
    os.system("clear")
    os.system("yrs list-channels")

dispCha = QPushButton('List Channels', parent=label1)
dispCha.setToolTip('This is button will show the Channels you\'re subbed to.')
dispCha.move(160,120)
dispCha.clicked.connect(showChannels)

def ClearTerm():
    os.system("clear")

clearTerm = QPushButton('Clear Terminal', parent=label1)
clearTerm.setToolTip('Clears the Terminal')
clearTerm.move(160,160)
clearTerm.clicked.connect(ClearTerm)

def Subscribe():
        os.system("clear")
        textboxValue = textbox.text()
        print('Channel URL Set: '+textboxValue)
        URL = textboxValue
        os.system(f"yrs subscribe {URL}")
        textbox.clear()


#        # Create textbox
textbox = QLineEdit(parent=label1)
textbox.move(0, 0)
textbox.resize(180,20)

button = QPushButton('Subscribe', parent=label1)
button.move(181,0)
button.resize(100,20)
button.clicked.connect(Subscribe)
button.setToolTip('Enter a YouTube Channel\'s URL to Subscribe!')


def UnSubscribe():
        os.system("clear")
        textboxValue = unsubBox.text()
        print('Channel URL Set: '+textboxValue)
        URL = textboxValue
        os.system(f"yrs unsubscribe {URL}")
        print('UnSubbed!')
        unsubBox.clear()


#        # Create textbox
unsubBox = QLineEdit(parent=label1)
unsubBox.move(0, 25)
unsubBox.resize(180,20)

unsubButton = QPushButton('UnSubscribe', parent=label1)
unsubButton.move(181,25)
unsubButton.resize(100,20)
unsubButton.clicked.connect(UnSubscribe)
unsubButton.setToolTip('Enter a YouTube Channel\'s URL to UnSub!')



def DownloadVid():
        os.system("clear")
        textboxValue = downloadBox.text()
        print('Video URL Set: '+textboxValue)
        URL = textboxValue
        os.system(f"yrs download {URL}")
        downloadBox.clear()


#        # Create textbox
downloadBox = QLineEdit(parent=label1)
downloadBox.move(0, 50)
downloadBox.resize(180,20)

downloadButton = QPushButton('Download Vid', parent=label1)
downloadButton.move(181,50)
downloadButton.resize(100,20)
downloadButton.clicked.connect(DownloadVid)
downloadButton.setToolTip('Enter a YouTube Video\'s URL to Download!')


def showChanVids():
        os.system("clear")
        textboxValue = chanVidBox.text()
        print('Channel Set: '+textboxValue)
        URL = textboxValue
        os.system(f"yrs list-videos {URL}")
        chanVidBox.clear()


#        # Create textbox
chanVidBox = QLineEdit(parent=label1)
chanVidBox.move(0, 75)
chanVidBox.resize(180,20)

chanVidButton = QPushButton('Channel Vids', parent=label1)
chanVidButton.move(181,75)
chanVidButton.resize(100,20)
chanVidButton.clicked.connect(showChanVids)
chanVidButton.setToolTip('Shows a specific Channel\'s Videos')


##### ending agreement #####
mainWindow.show()
application.exec()
##### ending agreement end #####
