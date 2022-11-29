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
		os.system("clear")
		print('pylibcheck is now installed')
	elif choice == 'N':
		print('Suit yourself then.')
		sys.exit()
	else:
		print('invalid choice')
		sys.exit()

## use pylibcheck for installing yrs
if not pylibcheck.checkPackage("youtube-rss-subscriber"):
	os.system("clear")
	print('yrs doesn\'t exist. Want me to install it for you?')
	x = input('(y/n) : ')
	choice = x.upper()
	if choice == 'Y':
		os.system('pip install youtube-rss-subscriber')
		os.system("clear")
		print('yrs is now installed')
	elif choice == 'N':
		print('Suit yourself then.')
		sys.exit()
	else:
		print('invalid choice')
		sys.exit()
else:
	print("yrs is installed? : True")

## use pylibcheck for installing requests
if not pylibcheck.checkPackage("requests"):
	os.system("clear")
	print('requests doesn\'t exist. Want me to install it for you?')
	x = input('(y/n) : ')
	choice = x.upper()
	if choice == 'Y':
		os.system('pip install requests')
		import requests
		os.system("clear")
		print('requests imported')
	elif choice == 'N':
		print('Suit yourself then.')
		sys.exit()
	else:
		print('invalid choice')
		sys.exit()
else:
	print("requests is installed? : True")

## use pylibcheck for installing PyQt5
if not pylibcheck.checkPackage("pyqt5"): # PyQt5 NEEDS to be lowercase on this line
	os.system("clear")
	print('PyQt5 doesn\'t exist. Want me to install it for you?')
	x = input('(y/n) : ')
	choice = x.upper()
	if choice == 'Y':
		os.system('pip install PyQt5')
		from PyQt5 import *
		os.system("clear")
		print('PyQt5 imported')
	elif choice == 'N':
		print('Suit yourself then.')
		sys.exit()
	else:
		print('invalid choice')
		sys.exit()
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

seperator = '-' * 229

#### Layout & Geometry ####

mainApp = QApplication([])

mainWindow = QWidget()
mainWindow.setFixedSize(1140, 555)
mainWindow.setWindowTitle('PyRSS : KorOwOzin')

layout = QGridLayout(mainWindow)

mainWindow.setLayout(layout)

label1 = QLabel('')
label2 = QLabel('')
labelA1 = QLabel('')
labelA2 = QLabel('')
labelA3 = QLabel('')
labelA4 = QLabel('')

layout1 = QtWidgets.QVBoxLayout(label1)
layout2 = QtWidgets.QVBoxLayout(label2)

layout3 = QtWidgets.QVBoxLayout(labelA1)
layout4 = QtWidgets.QVBoxLayout(labelA2)
layout5 = QtWidgets.QVBoxLayout(labelA3)
layout6 = QtWidgets.QGridLayout(labelA4)

tabwidget = QTabWidget(mainWindow)
tabwidget.addTab(label1, "Main")
tabwidget.addTab(label2, "Advanced Vid Info")

layout.addWidget(tabwidget)

infotab = QTabWidget(mainWindow)
infotab.addTab(labelA1, "Overview")
layout2.addWidget(infotab)

infotab.addTab(labelA2, "Thumbnail(s)")
layout2.addWidget(infotab)

infotab.addTab(labelA3, "Description")
layout2.addWidget(infotab)

infotab.addTab(labelA4, "Comments")
layout2.addWidget(infotab)

te1 = QTextEdit(mainWindow)
layout3.addWidget(te1)

te2 = QTextEdit(mainWindow)
layout4.addWidget(te2)

te3 = QTextEdit(mainWindow)
layout5.addWidget(te3)

te4 = QTextEdit(labelA4)
te4.move(9, 9)
te4.resize(1074, 361)

te1.setReadOnly(True)
te2.setReadOnly(True)
te3.setReadOnly(True)
te4.setReadOnly(True)

leLabel = QtWidgets.QLabel("Enter Video ID ( EX : Y2DNwLVZECM )")
le = QtWidgets.QLineEdit(mainWindow)

layout3.addWidget(leLabel)
layout3.addWidget(le)

comLabel = QtWidgets.QLabel("Max Comment Results : ", parent=labelA4)
comLabel.resize(180, 20)
comLabel.move(10, 385)

comle = QLineEdit(labelA4)
comle.move(185, 380)
comle.resize(30,30)

setComLabel = QtWidgets.QLabel(parent=labelA4)
setComLabel.resize(200, 20)
setComLabel.move(10, 415)

#### Layout & Geometry End ####


#### Console GUI ####

global consoleLog
consoleLog = QTextEdit(label1)
consoleLog.move(5, 180)
consoleLog.resize(1100,300)
consoleLog.setFontPointSize(11)
consoleLog.setReadOnly(True)

consoleLabel = QLabel('Console GUI', parent=label1)
consoleLabel.move(5, 150)

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
subLabel = QLabel('Subscribe', parent=label1)
subLabel.move(5, 0)

# Subscribe Textbox #
subBox = QLineEdit(label1)
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
unsubLabel = QLabel('UnSubscribe', parent=label1)
unsubLabel.move(190, 0)

# UnSubscribe Textbox #
unsubBox = QLineEdit(label1)
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
chanVidLabel = QLabel('Show Channel\'s Videos', parent=label1)
chanVidLabel.move(5, 50)
chanVidLabel.resize(180, 20)

# Channel Vid Textbox #
chanVidBox = QLineEdit(label1)
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
downloadVidLabel = QLabel('Download Video', parent=label1)
downloadVidLabel.move(190, 50)
downloadVidLabel.resize(180, 20)

# Channel Vid Textbox #
downloadVidBox = QLineEdit(label1)
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
		consoleLog.setFontPointSize(11)
		consoleLog.setText(e1)
		VidInfoBox.clear()
	elif "kind" in data['items'][0]:
		p1 = (f'Video URL : youtube.com/watch?v={vid}\n')
		p2 = ('Title : "' + str(data['items'][0]['snippet']['title']) + '"')
		p3 = ('Author : ' + str(data['items'][0]['snippet']['channelTitle']))   
		p4 = ('Channel ID : https://youtube.com/channel/' + str(data['items'][0]['snippet']['channelId']))
		p5 = ('Uploaded At : ' + str(data['items'][0]['snippet']['publishedAt']))
		p6 = ('HD or SD? : ' + str(data['items'][0]['contentDetails']['definition']).upper())
		p7 = ('Views : ' + str(data['items'][0]['statistics']['viewCount']))
		p8 = ('Likes : ' + str(data['items'][0]['statistics']['likeCount']))
		p9 = ('Dislikes : ' + str(data2['dislikes']))
		p10 = ('Comments : ' + str(data['items'][0]['statistics']['commentCount']))
		## No way to do this in a loop. Ugh ##
		consoleLog.setFontPointSize(11)
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
VidInfoLabel = QLabel('Show Basic Vid Info', parent=label1)
VidInfoLabel.move(375, 5)
VidInfoLabel.resize(180, 20)

# Vid Info Textbox #
VidInfoBox = QLineEdit(label1)
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
vlcLabel = QLabel('Stream to VLC', parent=label1)
vlcLabel.move(375, 50)
vlcLabel.resize(180, 20)

# VLC Stream Textbox #
vlcBox = QLineEdit(label1)
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
rssButton = QPushButton('Update RSS Feed', parent=label1)
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
allChannelsButton = QPushButton('List Channels', parent=label1)
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
#	consoleLog.setFontPointSize(11)
#	consoleLog.setText(op1)

# Show ALL Vids Button #
showAllVidsButton = QPushButton('List ALL Vids', parent=label1)
showAllVidsButton.setToolTip('Lists ALL Video\'s from subbed channels')
showAllVidsButton.move(700,50)
showAllVidsButton.resize(150,30)
showAllVidsButton.clicked.connect(showAllVids)

#### Show ALL Vids Function End ####



#### Clear GUI Log Function ####

def clearLog():
	os.system("clear")
	consoleLog.clear()
	consoleLog.setFontPointSize(11)
	consoleLog.setText('Cleared')

# Clear GUI Log Button #
clearLogButton = QPushButton('Clear Log', parent=label1)
clearLogButton.setToolTip('Clears the GUI Log')
clearLogButton.move(860,50)
clearLogButton.resize(150,30)
clearLogButton.clicked.connect(clearLog)

#### Clear GUI Log Function End ####

#### Advanced Info Pulling Function ####

maxRes = 10

setComLabel.setText(f'Currently set to : {maxRes}')
comLabel.setToolTip(f"Set Max Comment Results ( The Default is {maxRes} )")
comle.setToolTip(f'Set Max Comment Results ( The Default is {maxRes} )')

def setMaxRes():
	global maxRes
	maxRes = comle.text()

	if int(maxRes) > 100:
		maxRes = 100
		setComLabel.setText(f'The max is 100! Set to : {maxRes}')
	else:
		setComLabel.setText(f'Currently set to : {maxRes}')

	comle.clear()
	

def standardInfo():
	vid = le.text()

	url = requests.get(f'https://youtube.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id={vid}&key=AIzaSyA1_WyNYJOumLMknZE0OwW0IRehkJECgkk')
	text = url.text
	data = json.loads(text)

	url2 = requests.get(f'https://returnyoutubedislikeapi.com/votes?videoId={vid}')
	text2 = url2.text
	data2 = json.loads(text2)

	url3 = requests.get(f'https://www.googleapis.com/youtube/v3/commentThreads?key=AIzaSyA1_WyNYJOumLMknZE0OwW0IRehkJECgkk&textFormat=plainText&part=snippet&videoId={vid}&maxResults={maxRes}')
	text3 = url3.text
	data3 = json.loads(text3)

	if data['pageInfo']['totalResults'] == 0:
		e1 = (f'Video ID "{vid}" not found!')
		te1.setText(e1)
		te2.clear()
		te3.clear()
		te4.clear()
	elif "kind" in data['items'][0]:
		s1 = (f'Video URL : youtube.com/watch?v={vid}\n')
		s2 = ('Title : "' + str(data['items'][0]['snippet']['title']) + '"')
		s3 = ('Author : ' + str(data['items'][0]['snippet']['channelTitle']))   
		s4 = ('Channel ID : https://youtube.com/channel/' + str(data['items'][0]['snippet']['channelId']))
		s5 = ('Uploaded At : ' + str(data['items'][0]['snippet']['publishedAt']))
		s6 = ('HD or SD? : ' + str(data['items'][0]['contentDetails']['definition']).upper())
		s7 = ('Views : ' + str(data['items'][0]['statistics']['viewCount']))
		s8 = ('Likes : ' + str(data['items'][0]['statistics']['likeCount']))
		s9 = ('Dislikes : ' + str(data2['dislikes']))
		s10 = ('Comments : ' + str(data['items'][0]['statistics']['commentCount']))

		thumbnail = data['items'][0]['snippet']['thumbnails']['standard']['url']
		width = data['items'][0]['snippet']['thumbnails']['standard']['width']
		height = data['items'][0]['snippet']['thumbnails']['standard']['height']
		image = QImage()
		image.loadFromData(requests.get(thumbnail).content)
		image_label = QLabel(te2)
		image_label.setPixmap(QPixmap(image))
		image_label.resize(width, height)
		image_label.move(0, -25)
		te2.setText(f'{" " * 166}URL 1 : https://i.ytimg.com/vi/{vid}/default.jpg')
		te2.append(f'{" " * 166}URL 2 : https://i.ytimg.com/vi/{vid}/mqdefault.jpg')
		te2.append(f'{" " * 166}URL 3 : https://i.ytimg.com/vi/{vid}/hqdefault.jpg')
		te2.append(f'{" " * 166}URL 4 : https://i.ytimg.com/vi/{vid}/sddefault.jpg')

		d1 = ('## Description Start ##\n')
		d2 = (str(data['items'][0]['snippet']['description']))
		d3 = ('\n## Description End ##')

		## No way to do this in a loop. Ugh ##
		te1.setFontPointSize(11)
		te1.setText(str(s1))
		te1.append(str(s2))
		te1.append(str(s3))
		te1.append(str(s4))
		te1.append(str(s5))
		te1.append(str(s6))
		te1.append(str(s7))
		te1.append(str(s8))
		te1.append(str(s9))
		te1.append(str(s10))

		te3.setFontPointSize(11)
		te3.setText(str(d1))
		te3.append(str(d2))
		te3.append(str(d3))

	if data3['pageInfo']['totalResults'] == 0:
		c1 = (f'No Comments on this Video.')
		te4.setText(c1)
	else:
		te4.clear()

		amount = data3['pageInfo']['totalResults']
		count = 0
		for i in range(amount):
			e1 = data3['items'][count]['snippet']['topLevelComment']['snippet']['authorDisplayName']
			e2 = data3['items'][count]['snippet']['topLevelComment']['snippet']['textDisplay']
			e3 = (f'{seperator}\n')
			e4 = (f'@{e1} ⬇')
			e5 = (f': "{e2}"\n')

			blackColor = QColor(0, 0, 0)
			te4.setTextColor(blackColor)

			te4.append(e3)

			redColor = QColor(255, 0, 0)
			te4.setTextColor(redColor)

			te4.append(e4)

			blackColor = QColor(0, 0, 0)
			te4.setTextColor(blackColor)

			te4.append(e5)

			count += 1

			if count == amount:
				te4.append(seperator)
				te4.moveCursor(QTextCursor.Start)
				break

	te3.verticalScrollBar().setValue(0)

	le.clear()

le.returnPressed.connect(standardInfo)
comle.returnPressed.connect(setMaxRes)

#### Advanced Info Pulling Function End ####

##### ending agreement #####
mainWindow.show()
mainApp.exec()
##### ending agreement end #####
