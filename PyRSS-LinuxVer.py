# initial imports #
import sys
import os
from time import sleep
import json
# initial imports end #

os.system("clear")

## Base Check for pylibcheck
try:
	import pylibcheck
except ImportError as error:
	print(error, 'Want me to install it for you?')
	x = input('(y/n) : ')
	choice = x.upper()
	if choice == 'Y':
		os.system('pip install pylibcheck')
		import pylibcheck
	elif choice == 'N':
		print('Suit yourself then.')

## use pylibcheck for installing yrs
if not pylibcheck.checkPackage("youtube-rss-subscriber"):
	print('yrs doesn\'t exist. Want me to install it for you?')
	x = input('(y/n) : ')
	choice = x.upper()
	if choice == 'Y':
		os.system('pip install youtube-rss-subscriber')
	elif choice == 'N':
		print('Suit yourself then.')
else:
	print("Yrs is installed? : True")

## use pylibcheck for installing requests
if not pylibcheck.checkPackage("requests"):
	print('requests doesn\'t exist. Want me to install it for you?')
	x = input('(y/n) : ')
	choice = x.upper()
	if choice == 'Y':
		os.system('pip install requests')
	elif choice == 'N':
		print('Suit yourself then.')
else:
	print("requests is installed? : True")

## use pylibcheck for installing PyQt5
if not pylibcheck.checkPackage("pyqt5"): # PyQt5 NEEDS to be lowercase on this line
	print('PyQt5 doesn\'t exist. Want me to install it for you?')
	x = input('(y/n) : ')
	choice = x.upper()
	if choice == 'Y':
		os.system('pip install PyQt5')
	elif choice == 'N':
		print('Suit yourself then.')
else:
	print("PyQt5 is installed? : True")


##### imports #####
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
import requests
##### imports end #####


#### Layout & Geometry ####

mainApp = QApplication([])
mainWindow = QWidget()
mainWindow.setGeometry(0, 0, 1110, 440)
mainWindow.setWindowTitle('PyRSS : KorOwOzin')
layout = QGridLayout(mainWindow)
mainWindow.setLayout(layout)

#### Layout & Geometry End ####


#### Console GUI ####

global consoleLog
consoleLog = QTextEdit(mainWindow)
consoleLog.move(5, 130)
consoleLog.resize(1100,300)
consoleLog.setFontPointSize(10)
consoleLog.setReadOnly(True)

consoleLabel = QLabel('Console GUI', parent=mainWindow)
consoleLabel.move(5, 100)

#### Console GUI End ####


#### Subscribe Function ####

def Subscribe():

	def dataReady():
		cursor = consoleLog.textCursor()
		cursor.movePosition(cursor.End)
		cursor.insertText(process.readAll().data().decode())
		output.ensureCursorVisible()
		subBox.clear()

	def callProgram():
		output.clear()
		subText = subBox.text()
		consoleLog.setText(f'URL Set: {subText}\n\n')
		process.start(f'yrs subscribe {subText}')

	def SubscribeStart():
		global output
		output =  consoleLog

		global process
		process = QtCore.QProcess()
		process.readyRead.connect(dataReady)

		process.started.connect(lambda: subBox.setEnabled(False))
		process.finished.connect(lambda: subBox.setEnabled(True))


	os.system("clear")
	consoleLog.clear()
	SubscribeStart()
	callProgram()

# Subscribe Label #
subLabel = QLabel('Subscribe', parent=mainWindow)
subLabel.move(5, 0)

# Subscribe Textbox #
subBox = QLineEdit(mainWindow)
subBox.move(5, 25)
subBox.resize(180,20)
subBox.returnPressed.connect(Subscribe)
subBox.setToolTip('Enter a YouTube Channel\'s URL to Subscribe!')

#### Subscribe Function End ####



#### UnSubscribe Function ####

def UnSubscribe():

	def dataReady():
		cursor = consoleLog.textCursor()
		cursor.movePosition(cursor.End)
		cursor.insertText(process.readAll().data().decode())
		output.ensureCursorVisible()
		unsubBox.clear()

	def callProgram():
		output.clear()
		unsubText = unsubBox.text()
		consoleLog.setText(f'Channel URL Set: {unsubText}\n\n')
		process.start(f'yrs unsubscribe {unsubText}')

	def UnSubscribeStart():
		global output
		output =  consoleLog

		global process
		process = QtCore.QProcess()
		process.readyRead.connect(dataReady)

		process.started.connect(lambda: unsubBox.setEnabled(False))
		process.finished.connect(lambda: unsubBox.setEnabled(True))

	os.system("clear")
	consoleLog.clear()
	UnSubscribeStart()
	callProgram()

# UnSubscribe Label #
unsubLabel = QLabel('UnSubscribe', parent=mainWindow)
unsubLabel.move(190, 0)

# UnSubscribe Textbox #
unsubBox = QLineEdit(mainWindow)
unsubBox.move(190, 25)
unsubBox.resize(180,20)
unsubBox.returnPressed.connect(UnSubscribe)
unsubBox.setToolTip('UnSubscribe from a YouTube Channel\'s Feed')

#### UnSubscribe Function End ####



#### Show Specific Channels Function ####

def showChanVids():

	def dataReady():
		cursor = consoleLog.textCursor()
		cursor.movePosition(cursor.End)
		cursor.insertText(process.readAll().data().decode())
		output.ensureCursorVisible()
		chanVidBox.clear()

	def callProgram():
		output.clear()
		chanVidText = chanVidBox.text()
		consoleLog.setText(f'Channel Set: {chanVidText}\n\n')
		process.start(f'yrs list-videos {chanVidText}')

	def showChanVidsStart():
		global output
		output =  consoleLog

		global process
		process = QtCore.QProcess()
		process.readyRead.connect(dataReady)

		process.started.connect(lambda: chanVidBox.setEnabled(False))
		process.finished.connect(lambda: chanVidBox.setEnabled(True))


	os.system("clear")
	consoleLog.clear()
	showChanVidsStart()
	callProgram()

# Channel Vid Label #
chanVidLabel = QLabel('Show Channel\'s Videos', parent=mainWindow)
chanVidLabel.move(5, 50)
chanVidLabel.resize(180, 20)

# Channel Vid Textbox #
chanVidBox = QLineEdit(mainWindow)
chanVidBox.move(5, 70)
chanVidBox.resize(180,20)
chanVidBox.returnPressed.connect(showChanVids)
chanVidBox.setToolTip('Show a specifc Channel\'s Videos')

#### Show Specific Channels Function End ####



#### Download Video Function ####

def downloadVid():

	def dataReady():
		cursor = consoleLog.textCursor()
		cursor.movePosition(cursor.End)
		cursor.insertText(process.readAll().data().decode())
		output.ensureCursorVisible()
		downloadVidBox.clear()

	def callProgram():
		output.clear()
		downloadText = downloadVidBox.text()
		consoleLog.setText(f'Video Set: {downloadText}\n\n')
		process.start(f'youtube-dl {downloadText}')

	def startDownload():
		global output
		output =  consoleLog

		global process
		process = QtCore.QProcess()
		process.readyRead.connect(dataReady)

		process.started.connect(lambda: downloadVidBox.setEnabled(False))
		process.finished.connect(lambda: downloadVidBox.setEnabled(True))


	os.system("clear")
	consoleLog.clear()
	startDownload()
	callProgram()

# Channel Vid Label #
downloadVidLabel = QLabel('Download Video', parent=mainWindow)
downloadVidLabel.move(190, 50)
downloadVidLabel.resize(180, 20)

# Channel Vid Textbox #
downloadVidBox = QLineEdit(mainWindow)
downloadVidBox.move(190, 70)
downloadVidBox.resize(180,20)
downloadVidBox.returnPressed.connect(downloadVid)
downloadVidBox.setToolTip('Download a YouTube Video')

#### Show Specific Channels Function End ####



#### Show Vid Info Function ####

def showVidInfo():
	os.system("clear")
	consoleLog.clear()
	vid = VidInfoBox.text()

	url = requests.get(f'https://youtube.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id={vid}&key=AIzaSyA1_WyNYJOumLMknZE0OwW0IRehkJECgkk')
	text = url.text

	url2 = requests.get(f'https://returnyoutubedislikeapi.com/votes?videoId={vid}')
	text2 = url2.text
	
	data = json.loads(text)
	data2 = json.loads(text2)
	
	if data['pageInfo']['totalResults'] == 0:
		e1 = (f'Video ID "{vid}" not found!')
		consoleLog.setFontPointSize(10)
		consoleLog.setText(e1)
		VidInfoBox.clear()
	elif "kind" in data['items'][0]:
		p1 = (f'Video URL: youtube.com/watch?v={vid}\n')
		p2 = ('Title :', str(data['items'][0]['snippet']['title']))
		p3 = ('Author :', str(data['items'][0]['snippet']['channelTitle']))   
		p4 = ('Channel ID :', str(data['items'][0]['snippet']['channelId']))
		p5 = ('Uploaded At :', str(data['items'][0]['snippet']['publishedAt']))
		p6 = ('HD or SD? :', str(data['items'][0]['contentDetails']['definition']))
		p7 = ('Views :', str(data['items'][0]['statistics']['viewCount']))
		p8 = ('Likes :', str(data['items'][0]['statistics']['likeCount']))
		p9 = ('Dislikes :', str(data2['dislikes']))
		p10 = ('Comments :', str(data['items'][0]['statistics']['commentCount']))
		## No way to do this in a loop. Ugh ##
		consoleLog.setFontPointSize(10)
		consoleLog.setText(str(p1))
		consoleLog.append(str(p2))
		consoleLog.append(str(p3))
		consoleLog.append(str(p4))
		consoleLog.append(str(p5))
		consoleLog.append(str(p6))
		consoleLog.append(str(p7))
		consoleLog.append(str(p8))
		consoleLog.append(str(p9))
		consoleLog.append(str(p10))
		VidInfoBox.clear()

# Vid Info Label #
VidInfoLabel = QLabel('Show Video\'s Info', parent=mainWindow)
VidInfoLabel.move(375, 5)
VidInfoLabel.resize(180, 20)

# Vid Info Textbox #
VidInfoBox = QLineEdit(mainWindow)
VidInfoBox.move(375, 25)
VidInfoBox.resize(180,20)
VidInfoBox.returnPressed.connect(showVidInfo)
VidInfoBox.setToolTip('Show a specifc Videos\'s Information')

#### Show Vid Info Function End ####



#### VLC Stream Function ####

def vlcStream():

	def dataReady():
		cursor = consoleLog.textCursor()
		cursor.movePosition(cursor.End)
		cursor.insertText(process.readAll().data().decode())
		output.ensureCursorVisible()
		vlcBox.clear()

	def callProgram():
		output.clear()
		vlcText = vlcBox.text()
		consoleLog.setText(f'This feature might not work! Google constantly breaks VLC!\nHowever this should work 100% with any other Media URL\n\nURL Set: {vlcText}\n\n')
		process.start(f'vlc {vlcText}')

	def vlcStreamStart():
		global output
		output =  consoleLog

		global process
		process = QtCore.QProcess()
		process.readyRead.connect(dataReady)

		process.started.connect(lambda: vlcBox.setEnabled(False))
		process.finished.connect(lambda: vlcBox.setEnabled(True))


	os.system("clear")
	consoleLog.clear()
	vlcStreamStart()
	callProgram()

# VLC Stream Label #
vlcLabel = QLabel('Stream to VLC', parent=mainWindow)
vlcLabel.move(375, 50)
vlcLabel.resize(180, 20)

# VLC Stream Textbox #
vlcBox = QLineEdit(mainWindow)
vlcBox.move(375, 70)
vlcBox.resize(180,20)
vlcBox.returnPressed.connect(vlcStream)
vlcBox.setToolTip('Stream Media to VLC Player ( Please use FULL URL [ EX: https://example.com/video.mp4 ] )')

#### VLC Stream Function End ####



#### Update RSS Function ####

def updateRSS():

	def dataReady():
		cursor = consoleLog.textCursor()
		cursor.movePosition(cursor.End)
		cursor.insertText(process.readAll().data().decode())
		output.ensureCursorVisible()
		consoleLog.setText(f'Done')

	def callProgram():
		output.clear()
		consoleLog.setText(f'Updated RSS\n\n')
		process.start(f'yrs update')

	def updateRssStart():
		global output
		output =  consoleLog

		global process
		process = QtCore.QProcess()
		process.readyRead.connect(dataReady)

		process.started.connect(lambda: rssButton.setEnabled(False))
		process.finished.connect(lambda: rssButton.setEnabled(True))


	os.system("clear")
	consoleLog.clear()
	updateRssStart()
	callProgram()

# Update RSS Button #
rssButton = QPushButton('Update RSS Feed', parent=mainWindow)
rssButton.setToolTip('Update RSS Feed of Subbed Channels')
rssButton.move(700,15)
rssButton.resize(150,30)
rssButton.clicked.connect(updateRSS)

#### Update RSS Function End ####



#### Show Channels Function ####

def showAllChannels():

	def dataReady():
		cursor = consoleLog.textCursor()
		cursor.movePosition(cursor.End)
		cursor.insertText(process.readAll().data().decode())
		output.ensureCursorVisible()

	def callProgram():
		output.clear()
		process.start(f'yrs list-channels')

	def startShowAllChannels():
		global output
		output =  consoleLog

		global process
		process = QtCore.QProcess()
		process.readyRead.connect(dataReady)

		process.started.connect(lambda: allChannelsButton.setEnabled(False))
		process.finished.connect(lambda: allChannelsButton.setEnabled(True))


	os.system("clear")
	consoleLog.clear()
	startShowAllChannels()
	callProgram()

# Show Channels Button #
allChannelsButton = QPushButton('List Channels', parent=mainWindow)
allChannelsButton.setToolTip('Lists all Subbed Channels')
allChannelsButton.move(860,15)
allChannelsButton.resize(150,30)
allChannelsButton.clicked.connect(showAllChannels)

#### Show Channels Function End ####



#### Show ALL Vids Function ####

def showAllVids():

	def dataReady():
		cursor = consoleLog.textCursor()
		cursor.movePosition(cursor.End)
		cursor.insertText(process.readAll().data().decode())
		output.ensureCursorVisible()

	def callProgram():
		output.clear()
		process.start(f'yrs list-all-videos')

	def startShowAllVids():
		global output
		output =  consoleLog

		global process
		process = QtCore.QProcess()
		process.readyRead.connect(dataReady)

		process.started.connect(lambda: showAllVidsButton.setEnabled(False))
		process.finished.connect(lambda: showAllVidsButton.setEnabled(True))


	os.system("clear")
	consoleLog.clear()
	startShowAllVids()
	callProgram()

#	os.system("clear")
#	consoleLog.clear()
#	op1 = os.popen(f'yrs list-all-videos').read()
#	consoleLog.setFontPointSize(10)
#	consoleLog.setText(op1)

# Show ALL Vids Button #
showAllVidsButton = QPushButton('List ALL Vids', parent=mainWindow)
showAllVidsButton.setToolTip('Lists ALL Video\'s from subbed channels')
showAllVidsButton.move(700,50)
showAllVidsButton.resize(150,30)
showAllVidsButton.clicked.connect(showAllVids)

#### Show ALL Vids Function End ####



#### Clear GUI Log Function ####

def clearLog():
	os.system("clear")
	consoleLog.clear()
	consoleLog.setFontPointSize(10)
	consoleLog.setText('Cleared')

# Clear GUI Log Button #
clearLogButton = QPushButton('Clear Log', parent=mainWindow)
clearLogButton.setToolTip('Clears the GUI Log')
clearLogButton.move(860,50)
clearLogButton.resize(150,30)
clearLogButton.clicked.connect(clearLog)

#### Clear GUI Log Function End ####



##### ending agreement #####
mainWindow.show()
mainApp.exec()
##### ending agreement end #####
