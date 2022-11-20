# initial imports #
import sys
import os
import os.path
from time import sleep
import json, requests
config_exist = os.path.isfile("depend.config")
# initial imports end #

os.system("clear")

if config_exist == False:
	print('No Config File detected!\nInstalling dependencies. Please wait until it finishes')
	f = open("depend.config", "a")
	f.write("is YRS Installed? : True\nis PyQt5 installed? : True\nis Requests installed? : True")
	f.close()
	os.system("pip install youtube-rss-subscriber")
	sleep(2)
	os.system("pip install PyQt5")
	sleep(2)
	os.system("pip install requests")
	os.system("clear")
	print('Finished installing dependencies')
else:
	f = open("depend.config", "r")
	print(f.read())
	f.close()

##### imports #####
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
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
	os.system("clear")
	consoleLog.clear()
	subText = subBox.text()
	op1 = (f'Channel URL Set: {subText}\n')
	op2 = os.popen(f'yrs subscribe {subText}').read()
	op3 = '\n'
	op4 = op1 + op2 + op3
	consoleLog.setFontPointSize(10)
	consoleLog.setText(op4)
	subBox.clear()

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
	os.system("clear")
	consoleLog.clear()
	unsubText = unsubBox.text()
	op1 = (f'Channel URL Set: {unsubText}\n')
	op2 = os.popen(f'yrs unsubscribe {unsubText}').read()
	op3 = 'UnSubbed from: {unsubText}\n'
	op4 = op1 + op2 + op3
	consoleLog.setFontPointSize(10)
	consoleLog.setText(op4)
	unsubBox.clear()

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
	os.system("clear")
	consoleLog.clear()
	chanVidText = chanVidBox.text()
	op1 = (f'Channel URL Set: {chanVidText}\n')
	op2 = os.popen(f'yrs list-videos {chanVidText}').read()
	op3 = '\n'
	op4 = op1 + op2 + op3
	consoleLog.setFontPointSize(10)
	consoleLog.setText(op4)
	chanVidBox.clear()

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
	os.system("clear")
	consoleLog.clear()
	downloadText = downloadVidBox.text()
	op0 = ('Real-Time Download Progress not shown in this Beta!\n')
	op1 = (f'Video Set: {downloadText}\n')
	op2 = os.popen(f'youtube-dl {downloadText}').read()
	op3 = '\n'
	op4 = op0 + op1 + op2 + op3
	consoleLog.setFontPointSize(10)
	consoleLog.setText(op4)
	downloadVidBox.clear()

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
	os.system("clear")
	consoleLog.clear()
	vlcText = vlcBox.text()
	op0 = ('This feature might not work! Google constantly breaks VLC!\nHowever this should work 100% with any other Media URL\n')
	op1 = (f'Video Set: {vlcText}\n')
	op2 = os.popen(f'vlc {vlcText}').read()
	op3 = '\n'
	op4 = op0 + op1 + op2 + op3
	consoleLog.setFontPointSize(10)
	consoleLog.setText(op4)
	vlcBox.clear()

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
	os.system("clear")
	consoleLog.clear()
	op0 = (f'Updating RSS...\n')
	op1 = os.popen(f'yrs update').read()
	op2 = 'done\n'
	op3 = op0 + op1 + op2
	consoleLog.setFontPointSize(10)
	consoleLog.setText(op3)

# Update RSS Button #
showAllVids = QPushButton('Update RSS Feed', parent=mainWindow)
showAllVids.setToolTip('Update RSS Feed of Subbed Channels')
showAllVids.move(700,15)
showAllVids.resize(150,30)
showAllVids.clicked.connect(updateRSS)

#### Update RSS Function End ####



#### Show Channels Function ####

def showAllChannels():
	os.system("clear")
	consoleLog.clear()
	op1 = os.popen(f'yrs list-channels').read()
	consoleLog.setFontPointSize(10)
	consoleLog.setText(op1)

# Show Channels Button #
allChannelsButton = QPushButton('List Channels', parent=mainWindow)
allChannelsButton.setToolTip('Lists all Subbed Channels')
allChannelsButton.move(860,15)
allChannelsButton.resize(150,30)
allChannelsButton.clicked.connect(showAllChannels)

#### Show Channels Function End ####



#### Show ALL Vids Function ####

def showAllVids():
	os.system("clear")
	consoleLog.clear()
	op1 = os.popen(f'yrs list-all-videos').read()
	consoleLog.setFontPointSize(10)
	consoleLog.setText(op1)

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
