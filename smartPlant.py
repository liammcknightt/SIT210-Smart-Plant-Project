import sys
import importlib
import resources1_rc
import resources_rc
import smtplib
from email.mime.text import MIMEText
from flask import Flask, request, jsonify
from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime
from smartPlantGuiSettings import Ui_SettingsWindow, SettingsWindow
from email.mime.text import MIMEText


app = Flask(__name__)

light = None
temp = None
humid = None
moisture = None
email_counter = 0

@app.route('/sensor-data', methods=['POST'])
def sensor_data():
	
	global light, temp, humid, moisture
	
	print(request.data)
	data = request.json
	
	light = data.get('light')
	temp = data.get('temp')
	humid = data.get('humid')
	moisture = data.get('moisture')
	
	print("Received sensor data:")
	print("Light Sensor: ", light)
	print("Temp Sensor: ", temp)
	print("Humid Sensor: ",humid)
	print("Moisture Sensor: ", moisture)
	
	return jsonify({"status": "success"}), 200
	
def run_flask():
	app.run(host='0.0.0.0', port=5000)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(579, 471)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header_frame = QtWidgets.QFrame(self.centralwidget)
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left = QtWidgets.QFrame(self.header_frame)
        self.left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left.setObjectName("left")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.left)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.settings_button = QtWidgets.QToolButton(self.left)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_button.setIcon(icon)
        self.settings_button.setIconSize(QtCore.QSize(20, 20))
        self.settings_button.setObjectName("settings_button")
        self.horizontalLayout_2.addWidget(self.settings_button, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.left)
        self.middle = QtWidgets.QFrame(self.header_frame)
        self.middle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.middle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.middle.setObjectName("middle")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.middle)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.heading_label = QtWidgets.QLabel(self.middle)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.heading_label.setFont(font)
        self.heading_label.setAlignment(QtCore.Qt.AlignCenter)
        self.heading_label.setObjectName("heading_label")
        self.verticalLayout_6.addWidget(self.heading_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.name_label = QtWidgets.QLabel(self.middle)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name_label.setFont(font)
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.verticalLayout_6.addWidget(self.name_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.middle)
        self.right = QtWidgets.QFrame(self.header_frame)
        self.right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right.setObjectName("right")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.right)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.right)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout_4.addWidget(self.dateTimeEdit, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.right)
        self.verticalLayout.addWidget(self.header_frame, 0, QtCore.Qt.AlignTop)
        self.main_body = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy)
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.main_body)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.main_body)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.info_view = QtWidgets.QWidget()
        self.info_view.setObjectName("info_view")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.info_view)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.info_view_main_body = QtWidgets.QFrame(self.info_view)
        self.info_view_main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_view_main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_view_main_body.setObjectName("info_view_main_body")
        self.gridLayout = QtWidgets.QGridLayout(self.info_view_main_body)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.temperature_frame = QtWidgets.QFrame(self.info_view_main_body)
        self.temperature_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.temperature_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.temperature_frame.setObjectName("temperature_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.temperature_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.temp_heading_label = QtWidgets.QLabel(self.temperature_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.temp_heading_label.setFont(font)
        self.temp_heading_label.setObjectName("temp_heading_label")
        self.verticalLayout_2.addWidget(self.temp_heading_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.temp_lcd = QtWidgets.QLCDNumber(self.temperature_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temp_lcd.sizePolicy().hasHeightForWidth())
        self.temp_lcd.setSizePolicy(sizePolicy)
        self.temp_lcd.setObjectName("temp_lcd")
        self.verticalLayout_2.addWidget(self.temp_lcd)
        self.gridLayout.addWidget(self.temperature_frame, 0, 0, 1, 1)
        self.humidity_frame = QtWidgets.QFrame(self.info_view_main_body)
        self.humidity_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.humidity_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.humidity_frame.setObjectName("humidity_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.humidity_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.humid_heading_label = QtWidgets.QLabel(self.humidity_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.humid_heading_label.setFont(font)
        self.humid_heading_label.setObjectName("humid_heading_label")
        self.verticalLayout_3.addWidget(self.humid_heading_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.humid_lcd = QtWidgets.QLCDNumber(self.humidity_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.humid_lcd.sizePolicy().hasHeightForWidth())
        self.humid_lcd.setSizePolicy(sizePolicy)
        self.humid_lcd.setObjectName("humid_lcd")
        self.verticalLayout_3.addWidget(self.humid_lcd)
        self.gridLayout.addWidget(self.humidity_frame, 0, 1, 1, 1)
        self.moisture_frame = QtWidgets.QFrame(self.info_view_main_body)
        self.moisture_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.moisture_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.moisture_frame.setObjectName("moisture_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.moisture_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.moisture_heading_label = QtWidgets.QLabel(self.moisture_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.moisture_heading_label.setFont(font)
        self.moisture_heading_label.setObjectName("moisture_heading_label")
        self.verticalLayout_4.addWidget(self.moisture_heading_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.moisture_lcd = QtWidgets.QLCDNumber(self.moisture_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.moisture_lcd.sizePolicy().hasHeightForWidth())
        self.moisture_lcd.setSizePolicy(sizePolicy)
        self.moisture_lcd.setDigitCount(5)
        self.moisture_lcd.setObjectName("moisture_lcd")
        self.verticalLayout_4.addWidget(self.moisture_lcd)
        self.gridLayout.addWidget(self.moisture_frame, 1, 0, 1, 1)
        self.light_frame = QtWidgets.QFrame(self.info_view_main_body)
        self.light_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.light_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.light_frame.setObjectName("light_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.light_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.light_heading_label = QtWidgets.QLabel(self.light_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.light_heading_label.setFont(font)
        self.light_heading_label.setObjectName("light_heading_label")
        self.verticalLayout_5.addWidget(self.light_heading_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.light_lcd = QtWidgets.QLCDNumber(self.light_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.light_lcd.sizePolicy().hasHeightForWidth())
        self.light_lcd.setSizePolicy(sizePolicy)
        self.light_lcd.setObjectName("light_lcd")
        self.verticalLayout_5.addWidget(self.light_lcd)
        self.gridLayout.addWidget(self.light_frame, 1, 1, 1, 1)
        self.horizontalLayout_6.addWidget(self.info_view_main_body)
        self.tabWidget.addTab(self.info_view, "")
        self.graphic_view = QtWidgets.QWidget()
        self.graphic_view.setObjectName("graphic_view")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.graphic_view)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.graphic_view_main_body = QtWidgets.QFrame(self.graphic_view)
        self.graphic_view_main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graphic_view_main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graphic_view_main_body.setObjectName("graphic_view_main_body")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.graphic_view_main_body)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.stackedWidget = QtWidgets.QStackedWidget(self.graphic_view_main_body)
        self.stackedWidget.setObjectName("stackedWidget")
        self.healthy = QtWidgets.QWidget()
        self.healthy.setObjectName("healthy")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.healthy)
        self.gridLayout_2.setContentsMargins(0, 9, 0, 9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.healthy_heading = QtWidgets.QLabel(self.healthy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.healthy_heading.setFont(font)
        self.healthy_heading.setObjectName("healthy_heading")
        self.gridLayout_2.addWidget(self.healthy_heading, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.healthy_emoji = QtWidgets.QLabel(self.healthy)
        self.healthy_emoji.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.healthy_emoji.sizePolicy().hasHeightForWidth())
        self.healthy_emoji.setSizePolicy(sizePolicy)
        self.healthy_emoji.setMinimumSize(QtCore.QSize(0, 0))
        self.healthy_emoji.setMaximumSize(QtCore.QSize(300, 300))
        self.healthy_emoji.setText("")
        self.healthy_emoji.setPixmap(QtGui.QPixmap(":/emoji/happy.png"))
        self.healthy_emoji.setScaledContents(True)
        self.healthy_emoji.setAlignment(QtCore.Qt.AlignCenter)
        self.healthy_emoji.setObjectName("healthy_emoji")
        self.gridLayout_2.addWidget(self.healthy_emoji, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.healthy)
        self.thirsty = QtWidgets.QWidget()
        self.thirsty.setObjectName("thirsty")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.thirsty)
        self.gridLayout_3.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.thirsty_heading = QtWidgets.QLabel(self.thirsty)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.thirsty_heading.setFont(font)
        self.thirsty_heading.setObjectName("thirsty_heading")
        self.gridLayout_3.addWidget(self.thirsty_heading, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.thirsty_emoji = QtWidgets.QLabel(self.thirsty)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thirsty_emoji.sizePolicy().hasHeightForWidth())
        self.thirsty_emoji.setSizePolicy(sizePolicy)
        self.thirsty_emoji.setMinimumSize(QtCore.QSize(0, 0))
        self.thirsty_emoji.setMaximumSize(QtCore.QSize(300, 300))
        self.thirsty_emoji.setText("")
        self.thirsty_emoji.setPixmap(QtGui.QPixmap(":/emoji/sweat.png"))
        self.thirsty_emoji.setScaledContents(True)
        self.thirsty_emoji.setAlignment(QtCore.Qt.AlignCenter)
        self.thirsty_emoji.setObjectName("thirsty_emoji")
        self.gridLayout_3.addWidget(self.thirsty_emoji, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.thirsty)
        self.sleeping = QtWidgets.QWidget()
        self.sleeping.setObjectName("sleeping")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.sleeping)
        self.gridLayout_4.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.sleeping_heading = QtWidgets.QLabel(self.sleeping)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sleeping_heading.setFont(font)
        self.sleeping_heading.setObjectName("sleeping_heading")
        self.gridLayout_4.addWidget(self.sleeping_heading, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.sleeping_emoji = QtWidgets.QLabel(self.sleeping)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sleeping_emoji.sizePolicy().hasHeightForWidth())
        self.sleeping_emoji.setSizePolicy(sizePolicy)
        self.sleeping_emoji.setMinimumSize(QtCore.QSize(0, 0))
        self.sleeping_emoji.setMaximumSize(QtCore.QSize(300, 300))
        self.sleeping_emoji.setText("")
        self.sleeping_emoji.setPixmap(QtGui.QPixmap(":/emoji/sleeping.png"))
        self.sleeping_emoji.setScaledContents(True)
        self.sleeping_emoji.setAlignment(QtCore.Qt.AlignCenter)
        self.sleeping_emoji.setObjectName("sleeping_emoji")
        self.gridLayout_4.addWidget(self.sleeping_emoji, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.sleeping)
        self.hot = QtWidgets.QWidget()
        self.hot.setObjectName("hot")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.hot)
        self.gridLayout_5.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_5.setHorizontalSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.hot_heading = QtWidgets.QLabel(self.hot)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.hot_heading.setFont(font)
        self.hot_heading.setObjectName("hot_heading")
        self.gridLayout_5.addWidget(self.hot_heading, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.hot_emoji = QtWidgets.QLabel(self.hot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hot_emoji.sizePolicy().hasHeightForWidth())
        self.hot_emoji.setSizePolicy(sizePolicy)
        self.hot_emoji.setMinimumSize(QtCore.QSize(0, 0))
        self.hot_emoji.setMaximumSize(QtCore.QSize(300, 300))
        self.hot_emoji.setText("")
        self.hot_emoji.setPixmap(QtGui.QPixmap(":/emoji/hot.png"))
        self.hot_emoji.setScaledContents(True)
        self.hot_emoji.setAlignment(QtCore.Qt.AlignCenter)
        self.hot_emoji.setObjectName("hot_emoji")
        self.gridLayout_5.addWidget(self.hot_emoji, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.hot)
        self.cold = QtWidgets.QWidget()
        self.cold.setObjectName("cold")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.cold)
        self.gridLayout_6.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.cold_heading = QtWidgets.QLabel(self.cold)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cold_heading.setFont(font)
        self.cold_heading.setObjectName("cold_heading")
        self.gridLayout_6.addWidget(self.cold_heading, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.cold_emoji = QtWidgets.QLabel(self.cold)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cold_emoji.sizePolicy().hasHeightForWidth())
        self.cold_emoji.setSizePolicy(sizePolicy)
        self.cold_emoji.setMinimumSize(QtCore.QSize(0, 0))
        self.cold_emoji.setMaximumSize(QtCore.QSize(300, 300))
        self.cold_emoji.setText("")
        self.cold_emoji.setPixmap(QtGui.QPixmap(":/emoji/cold.png"))
        self.cold_emoji.setScaledContents(True)
        self.cold_emoji.setAlignment(QtCore.Qt.AlignCenter)
        self.cold_emoji.setObjectName("cold_emoji")
        self.gridLayout_6.addWidget(self.cold_emoji, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.cold)
        self.horizontalLayout_8.addWidget(self.stackedWidget)
        self.horizontalLayout_7.addWidget(self.graphic_view_main_body)
        self.tabWidget.addTab(self.graphic_view, "")
        self.horizontalLayout_5.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.main_body)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.settings_button.setText(_translate("MainWindow", "..."))
        self.heading_label.setText(_translate("MainWindow", "Smart Plant"))
        self.name_label.setText(_translate("MainWindow", "*Name/Plant*"))
        self.temp_heading_label.setText(_translate("MainWindow", "Temperature (Celcius)"))
        self.humid_heading_label.setText(_translate("MainWindow", "Humidity (%)"))
        self.moisture_heading_label.setText(_translate("MainWindow", "Soil Moisture (%)"))
        self.light_heading_label.setText(_translate("MainWindow", "Light Exposure (lx)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.info_view), _translate("MainWindow", "Info View"))
        self.healthy_heading.setText(_translate("MainWindow", "Healthy"))
        self.thirsty_heading.setText(_translate("MainWindow", "Thirsty"))
        self.sleeping_heading.setText(_translate("MainWindow", "Sleeping"))
        self.hot_heading.setText(_translate("MainWindow", "Hot"))
        self.cold_heading.setText(_translate("MainWindow", "Cold"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.graphic_view), _translate("MainWindow", "Graphic View"))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		
		global email_counter
		email_counter = 0
		
		current_datetime = QtCore.QDateTime.currentDateTime()
		self.dateTimeEdit.setDateTime(current_datetime)
		
		self.tabWidget.setCurrentIndex(0)
		self.stackedWidget.setCurrentIndex(0)
		
		self.update_gui_timer = QtCore.QTimer(self)
		self.update_gui_timer.timeout.connect(self.update_gui)
		self.update_gui_timer.start(1000)
		
		self.update_graphic_view_timer = QtCore.QTimer(self)
		self.update_graphic_view_timer.timeout.connect(self.update_graphic_view)
		self.update_graphic_view_timer.start(1000)
		
		self.check_send_email_timer = QtCore.QTimer(self)
		self.check_send_email_timer.timeout.connect(self.check_send_email)
		self.check_send_email_timer.start(1000)
		
		self.settings_button.clicked.connect(self.on_settings_button_click)
		
		
	def update_gui(self):
		
		global light, temp, humid, moisture
		
		plant_name = get_setting('PlantName')
		self.name_label.setText(plant_name)
		
		if light is not None and temp is not None and humid is not None and moisture is not None:
			self.light_lcd.display(light)
			self.temp_lcd.display(temp)
			self.humid_lcd.display(humid)
			self.moisture_lcd.display(moisture)
			
	def on_settings_button_click(self):
		self.settings_window = SettingsWindow()
		self.settings_window.show()
		
	def update_graphic_view(self):
		global light, temp, humid, moisture
		current_time = QTime.currentTime()
		start_time = QTime(20, 0)
		end_time = QTime(23, 59)
		start_time1 = QTime(24, 0)
		end_time1 = QTime(5, 0)
		
		max_temp = get_setting('MaxTemp')
		min_temp = get_setting('MinTemp')
		max_humid = get_setting('MaxHumid')
		min_humid = get_setting('MinHumid')
		max_moisture = get_setting('MaxMoisture')
		min_moisture = get_setting('MinMoisture')
		max_light = get_setting('MaxLight')
		min_light = get_setting('MinLight')
		max_temp_int = float(max_temp)
		min_temp_int = float(min_temp)
		max_humid_int = float(max_humid)
		min_humid_int = float(min_humid)
		max_moisture_int = int(max_moisture)
		min_moisture_int = int(min_moisture)
		max_light_int = float(max_light)
		min_light_int = float(min_light)
		
		if light is not None and temp is not None and humid is not None and moisture is not None:
			if start_time <= current_time <= end_time:
				self.stackedWidget.setCurrentIndex(2)
			elif start_time1 <= current_time <= end_time1:
				self.stackedWidget.setCurrentIndex(2)
			elif moisture < min_moisture_int:
				self.stackedWidget.setCurrentIndex(1)
			elif temp > max_temp_int:
				self.stackedWidget.setCurrentIndex(3)
			elif temp < min_temp_int:
				self.stackedWidget.setCurrentIndex(4)
			else:
				self.stackedWidget.setCurrentIndex(0)
				
	def check_send_email(self):
		global light, temp, humid, moisture, email_counter
		receive_notifications = get_setting('ReceiveNotifications')
		receive_notifications_int = int(receive_notifications)
		plant_name = get_setting('PlantName')
		email = get_setting('Email')
		current_index = self.stackedWidget.currentIndex()
		current_time = QTime.currentTime()

		light_str = str(light)
		temp_str = str(temp)
		humid_str = str(humid)
		moisture_str = str(moisture)

		if receive_notifications_int == 1 and email != '':
			if current_index == 2 and email_counter != 1:
				subject = 'Sleeping'
				body = plant_name + ' is sleeping, the time is currently ' + current_time
				send_email(subject, body)
				email_counter = 1
			elif current_index == 1 and email_counter != 2:
				subject = 'Thirsty'
				body = plant_name + ' is thirsty, soil moisture level is at ' + moisture_str + '%'
				send_email(subject, body)
				email_counter = 2
			elif current_index == 3 and email_counter != 3:
				subject = 'Hot'
				body = plant_name + ' is hot, the temperature is currently ' + temp_str + 'C'
				send_email(subject, body)
				email_counter = 3
			elif current_index == 4 and email_counter != 4:
				subject = 'Cold'
				body = plant_name + ' is cold, the temperature is currently ' + temp_str + 'C'
				send_email(subject, body)
				email_counter = 4
			elif current_index == 0 and email_counter != 5:
				subject = 'Healthy'
				body = plant_name + ' is healthy, current conditions are suitable.'
				send_email(subject, body)
				email_counter = 5

def send_email(subject, body):
	sender_email = 'SmartPlant861@outlook.com'
	recipient_email = get_setting('Email')
	smtp_server = 'smtp.office365.com'
	smtp_port = 587
	smtp_username = 'SmartPlant861@outlook.com'
	smtp_password = 'SmartPlant'
	
	msg = MIMEText(body)
	msg['Subject'] = subject
	msg['From'] = sender_email
	msg['To'] = recipient_email
	
	with smtplib.SMTP(smtp_server, smtp_port) as server:
		server.starttls()
		server.login(smtp_username, smtp_password)
		server.send_message(msg)

def get_setting(setting):
	settings = {}
	with open('settings.txt', 'r') as f:
		for line in f:
			key, value = line.strip().split('=')
			settings[key.strip()] = value.strip()
			
	return settings.get(setting)

def run_qt():
	app = QtWidgets.QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	flask_thread = Thread(target=run_flask)
	flask_thread.start()
	
	run_qt()
