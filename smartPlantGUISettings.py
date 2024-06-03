import sys

from PyQt5 import QtCore, QtGui, QtWidgets



plant_name_init = "Name/Plant"

max_temp_init = 50

min_temp_init = 0

max_humid_init = 100

min_humid_init = 0

max_moisture_init = 100

min_moisture_init = 0

max_light_init = 5000

min_light_init = 0

email_init = ""

receive_notifications_init = 0

flag = 0



class Ui_SettingsWindow(object):

    def setupUi(self, SettingsWindow):

        SettingsWindow.setObjectName("SettingsWindow")

        SettingsWindow.resize(498, 371)

        self.centralwidget = QtWidgets.QWidget(SettingsWindow)

        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)

        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.setSpacing(0)

        self.horizontalLayout.setObjectName("horizontalLayout")

        self.main_body = QtWidgets.QFrame(self.centralwidget)

        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)

        self.main_body.setObjectName("main_body")

        self.gridLayout = QtWidgets.QGridLayout(self.main_body)

        self.gridLayout.setObjectName("gridLayout")

        self.plant_name_frame = QtWidgets.QFrame(self.main_body)

        self.plant_name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.plant_name_frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.plant_name_frame.setObjectName("plant_name_frame")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.plant_name_frame)

        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label = QtWidgets.QLabel(self.plant_name_frame)

        self.label.setObjectName("label")

        self.horizontalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignLeft)

        self.plant_name_edit = QtWidgets.QLineEdit(self.plant_name_frame)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        sizePolicy.setHorizontalStretch(0)

        sizePolicy.setVerticalStretch(0)

        sizePolicy.setHeightForWidth(self.plant_name_edit.sizePolicy().hasHeightForWidth())

        self.plant_name_edit.setSizePolicy(sizePolicy)

        self.plant_name_edit.setObjectName("plant_name_edit")

        self.horizontalLayout_2.addWidget(self.plant_name_edit, 0, QtCore.Qt.AlignHCenter)

        self.gridLayout.addWidget(self.plant_name_frame, 0, 0, 1, 1)

        self.empty_space = QtWidgets.QFrame(self.main_body)

        self.empty_space.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.empty_space.setFrameShadow(QtWidgets.QFrame.Raised)

        self.empty_space.setObjectName("empty_space")

        self.gridLayout.addWidget(self.empty_space, 0, 1, 1, 1)

        self.temp = QtWidgets.QFrame(self.main_body)

        self.temp.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.temp.setFrameShadow(QtWidgets.QFrame.Raised)

        self.temp.setObjectName("temp")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.temp)

        self.gridLayout_2.setObjectName("gridLayout_2")

        self.label_3 = QtWidgets.QLabel(self.temp)

        self.label_3.setObjectName("label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1, QtCore.Qt.AlignLeft)

        self.label_2 = QtWidgets.QLabel(self.temp)

        self.label_2.setObjectName("label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.max_temp = QtWidgets.QLineEdit(self.temp)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        sizePolicy.setHorizontalStretch(0)

        sizePolicy.setVerticalStretch(0)

        sizePolicy.setHeightForWidth(self.max_temp.sizePolicy().hasHeightForWidth())

        self.max_temp.setSizePolicy(sizePolicy)

        self.max_temp.setObjectName("max_temp")

        self.gridLayout_2.addWidget(self.max_temp, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)

        self.label_4 = QtWidgets.QLabel(self.temp)

        self.label_4.setObjectName("label_4")

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.min_temp = QtWidgets.QLineEdit(self.temp)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        sizePolicy.setHorizontalStretch(0)

        sizePolicy.setVerticalStretch(0)

        sizePolicy.setHeightForWidth(self.min_temp.sizePolicy().hasHeightForWidth())

        self.min_temp.setSizePolicy(sizePolicy)

        self.min_temp.setObjectName("min_temp")

        self.gridLayout_2.addWidget(self.min_temp, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)

        self.gridLayout.addWidget(self.temp, 1, 0, 1, 1)

        self.humid = QtWidgets.QFrame(self.main_body)

        self.humid.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.humid.setFrameShadow(QtWidgets.QFrame.Raised)

        self.humid.setObjectName("humid")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.humid)

        self.gridLayout_3.setObjectName("gridLayout_3")

        self.label_5 = QtWidgets.QLabel(self.humid)

        self.label_5.setObjectName("label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_6 = QtWidgets.QLabel(self.humid)

        self.label_6.setObjectName("label_6")

        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)

        self.max_humid = QtWidgets.QLineEdit(self.humid)

        self.max_humid.setObjectName("max_humid")

        self.gridLayout_3.addWidget(self.max_humid, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)

        self.label_7 = QtWidgets.QLabel(self.humid)

        self.label_7.setObjectName("label_7")

        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)

        self.min_humid = QtWidgets.QLineEdit(self.humid)

        self.min_humid.setObjectName("min_humid")

        self.gridLayout_3.addWidget(self.min_humid, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)

        self.gridLayout.addWidget(self.humid, 1, 1, 1, 1)

        self.moisture = QtWidgets.QFrame(self.main_body)

        self.moisture.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.moisture.setFrameShadow(QtWidgets.QFrame.Raised)

        self.moisture.setObjectName("moisture")

        self.gridLayout_4 = QtWidgets.QGridLayout(self.moisture)

        self.gridLayout_4.setObjectName("gridLayout_4")

        self.label_8 = QtWidgets.QLabel(self.moisture)

        self.label_8.setObjectName("label_8")

        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_9 = QtWidgets.QLabel(self.moisture)

        self.label_9.setObjectName("label_9")

        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 1)

        self.max_moisture = QtWidgets.QLineEdit(self.moisture)

        self.max_moisture.setObjectName("max_moisture")

        self.gridLayout_4.addWidget(self.max_moisture, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)

        self.label_10 = QtWidgets.QLabel(self.moisture)

        self.label_10.setObjectName("label_10")

        self.gridLayout_4.addWidget(self.label_10, 2, 0, 1, 1)

        self.min_moisture = QtWidgets.QLineEdit(self.moisture)

        self.min_moisture.setObjectName("min_moisture")

        self.gridLayout_4.addWidget(self.min_moisture, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)

        self.gridLayout.addWidget(self.moisture, 2, 0, 1, 1)

        self.light = QtWidgets.QFrame(self.main_body)

        self.light.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.light.setFrameShadow(QtWidgets.QFrame.Raised)

        self.light.setObjectName("light")

        self.gridLayout_5 = QtWidgets.QGridLayout(self.light)

        self.gridLayout_5.setObjectName("gridLayout_5")

        self.label_11 = QtWidgets.QLabel(self.light)

        self.label_11.setObjectName("label_11")

        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_12 = QtWidgets.QLabel(self.light)

        self.label_12.setObjectName("label_12")

        self.gridLayout_5.addWidget(self.label_12, 1, 0, 1, 1)

        self.max_light = QtWidgets.QLineEdit(self.light)

        self.max_light.setObjectName("max_light")

        self.gridLayout_5.addWidget(self.max_light, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)

        self.label_13 = QtWidgets.QLabel(self.light)

        self.label_13.setObjectName("label_13")

        self.gridLayout_5.addWidget(self.label_13, 2, 0, 1, 1)

        self.min_light = QtWidgets.QLineEdit(self.light)

        self.min_light.setObjectName("min_light")

        self.gridLayout_5.addWidget(self.min_light, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)

        self.gridLayout.addWidget(self.light, 2, 1, 1, 1)

        self.notifications = QtWidgets.QFrame(self.main_body)

        self.notifications.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.notifications.setFrameShadow(QtWidgets.QFrame.Raised)

        self.notifications.setObjectName("notifications")

        self.gridLayout_6 = QtWidgets.QGridLayout(self.notifications)

        self.gridLayout_6.setObjectName("gridLayout_6")

        self.notifications_checkbox = QtWidgets.QCheckBox(self.notifications)

        self.notifications_checkbox.setObjectName("notifications_checkbox")

        self.gridLayout_6.addWidget(self.notifications_checkbox, 0, 0, 1, 1, QtCore.Qt.AlignLeft)

        self.label_14 = QtWidgets.QLabel(self.notifications)

        self.label_14.setObjectName("label_14")

        self.gridLayout_6.addWidget(self.label_14, 2, 0, 1, 1, QtCore.Qt.AlignLeft)

        self.email_edit = QtWidgets.QLineEdit(self.notifications)

        self.email_edit.setObjectName("email_edit")

        self.gridLayout_6.addWidget(self.email_edit, 3, 0, 1, 1)

        self.gridLayout.addWidget(self.notifications, 3, 0, 1, 1)

        self.save = QtWidgets.QFrame(self.main_body)

        self.save.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.save.setFrameShadow(QtWidgets.QFrame.Raised)

        self.save.setObjectName("save")

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.save)

        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.save_button = QtWidgets.QPushButton(self.save)

        self.save_button.setObjectName("save_button")

        self.horizontalLayout_4.addWidget(self.save_button)

        self.cancel_button = QtWidgets.QPushButton(self.save)

        self.cancel_button.setObjectName("cancel_button")

        self.horizontalLayout_4.addWidget(self.cancel_button)

        self.gridLayout.addWidget(self.save, 3, 1, 1, 1)

        self.horizontalLayout.addWidget(self.main_body)

        SettingsWindow.setCentralWidget(self.centralwidget)



        self.retranslateUi(SettingsWindow)

        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)



    def retranslateUi(self, SettingsWindow):

        _translate = QtCore.QCoreApplication.translate

        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "SettingsWindow"))

        self.label.setText(_translate("SettingsWindow", "Plant/Name:"))

        self.label_3.setText(_translate("SettingsWindow", "Max"))

        self.label_2.setText(_translate("SettingsWindow", "Temperature (C)"))

        self.max_temp.setInputMask(_translate("SettingsWindow", "99"))

        self.max_temp.setText(_translate("SettingsWindow", "."))

        self.label_4.setText(_translate("SettingsWindow", "Min"))

        self.min_temp.setInputMask(_translate("SettingsWindow", "99"))

        self.label_5.setText(_translate("SettingsWindow", "Humidity(%)"))

        self.label_6.setText(_translate("SettingsWindow", "Max"))

        self.max_humid.setInputMask(_translate("SettingsWindow", "999"))

        self.label_7.setText(_translate("SettingsWindow", "Min"))

        self.min_humid.setInputMask(_translate("SettingsWindow", "99"))

        self.label_8.setText(_translate("SettingsWindow", "Moisture"))

        self.label_9.setText(_translate("SettingsWindow", "Max"))

        self.max_moisture.setInputMask(_translate("SettingsWindow", "999"))

        self.label_10.setText(_translate("SettingsWindow", "Min"))

        self.min_moisture.setInputMask(_translate("SettingsWindow", "99"))

        self.label_11.setText(_translate("SettingsWindow", "Light Exposure"))

        self.label_12.setText(_translate("SettingsWindow", "Max"))

        self.max_light.setInputMask(_translate("SettingsWindow", "99999"))

        self.label_13.setText(_translate("SettingsWindow", "Min"))

        self.min_light.setInputMask(_translate("SettingsWindow", "99999"))

        self.notifications_checkbox.setText(_translate("SettingsWindow", "Receive Notifications"))

        self.label_14.setText(_translate("SettingsWindow", "Email"))

        self.save_button.setText(_translate("SettingsWindow", "Save"))

        self.cancel_button.setText(_translate("SettingsWindow", "Cancel"))



class SettingsWindow(QtWidgets.QMainWindow, Ui_SettingsWindow):

        def __init__(self):

                super().__init__()

                self.setupUi(self)

                

                global plant_name_init, max_temp_init, min_temp_init, max_humid_init, min_humid_init, max_moisture_init, min_moisture_init, max_light_init, min_light_init, email_init, receive_notifications_init, flag

                

                if flag == 0:

                        self.plant_name_edit.setText(plant_name_init)

                        self.max_temp.setText(str(max_temp_init))

                        self.min_temp.setText(str(min_temp_init))

                        self.max_humid.setText(str(max_humid_init))

                        self.min_humid.setText(str(min_humid_init))

                        self.max_moisture.setText(str(max_moisture_init))

                        self.min_moisture.setText(str(min_moisture_init))

                        self.max_light.setText(str(max_light_init))

                        self.min_light.setText(str(min_light_init))

                        self.email_edit.setText(email_init)

                

                        with open('settings.txt', 'w') as f:

                                f.write(f"PlantName={plant_name_init}\n")

                                f.write(f"MaxTemp={max_temp_init}\n")

                                f.write(f"MinTemp={min_temp_init}\n")

                                f.write(f"MaxHumid={max_humid_init}\n")

                                f.write(f"MinHumid={min_humid_init}\n")

                                f.write(f"MaxMoisture={max_moisture_init}\n")

                                f.write(f"MinMoisture={min_moisture_init}\n")

                                f.write(f"MaxLight={max_light_init}\n")

                                f.write(f"MinLight={min_light_init}\n")

                                f.write(f"Email={email_init}\n")

                                f.write(f"ReceiveNotifications={receive_notifications_init}\n")

                                

                        flag = 1

                

                settings = load_settings()

                plant_name = settings.get('PlantName')

                max_temp = settings.get('MaxTemp')

                min_temp = settings.get('MinTemp')

                max_humid = settings.get('MaxHumid')

                min_humid = settings.get('MinHumid')

                max_moisture = settings.get('MaxMoisture')

                min_moisture = settings.get('MinMoisture')

                max_light = settings.get('MaxLight')

                min_light = settings.get('MinLight')

                email = settings.get('Email')

                receive_notifications = settings.get('ReceiveNotifications')

                receive_notifications_int = int(receive_notifications)

                self.plant_name_edit.setText(plant_name)

                self.max_temp.setText(max_temp)

                self.min_temp.setText(min_temp)

                self.max_humid.setText(max_humid)

                self.min_humid.setText(min_humid)

                self.max_moisture.setText(max_moisture)

                self.min_moisture.setText(min_moisture)

                self.max_light.setText(max_light)

                self.min_light.setText(min_light)

                if receive_notifications_int == 1:

                        self.notifications_checkbox.setChecked(True)

                

                self.save_button.clicked.connect(self.on_save_button_click)

                self.cancel_button.clicked.connect(self.close)

                

        def on_save_button_click(self):

                plant_name_value = self.plant_name_edit.text()

                max_temp_value = self.max_temp.text()

                min_temp_value = self.min_temp.text()

                max_humid_value = self.max_humid.text()

                min_humid_value = self.min_humid.text()

                max_moisture_value = self.max_moisture.text()

                min_moisture_value = self.min_moisture.text()

                max_light_value = self.max_light.text()

                min_light_value = self.min_light.text()

                email_value = self.email_edit.text()

                if self.notifications_checkbox.isChecked():

                        receive_notifications_value = 1

                else:

                        receive_notifications_value = 0

                        

                with open('settings.txt', 'w') as f:

                        f.write(f"PlantName={plant_name_value}\n")

                        f.write(f"MaxTemp={max_temp_value}\n")

                        f.write(f"MinTemp={min_temp_value}\n")

                        f.write(f"MaxHumid={max_humid_value}\n")

                        f.write(f"MinHumid={min_humid_value}\n")

                        f.write(f"MaxMoisture={max_moisture_value}\n")

                        f.write(f"MinMoisture={min_moisture_value}\n")

                        f.write(f"MaxLight={max_light_value}\n")

                        f.write(f"MinLight={min_light_value}\n")

                        f.write(f"Email={email_value}\n")

                        f.write(f"ReceiveNotifications={receive_notifications_value}\n")

                        

def load_settings():

        settings = {}

        with open('settings.txt', 'r') as f:

                for line in f:

                        key, value = line.strip().split('=')

                        settings[key.strip()] = value.strip()

        return settings

