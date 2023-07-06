# Form implementation generated from reading ui file 'windows_stacked_02.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1525, 1030)
        
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 1501, 981))
        self.stackedWidget.setObjectName("stackedWidget")
        
        
        ### Page 2 _____________________________________________________________
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.painting_image_random = QtWidgets.QLabel(parent=self.page_2)
        self.painting_image_random.setGeometry(QtCore.QRect(620, 140, 661, 731))
        self.painting_image_random.setText("")
        self.painting_image_random.setPixmap(QtGui.QPixmap("../example_paintings/Pablo_Picasso_412.jpg"))
        self.painting_image_random.setScaledContents(True)
        self.painting_image_random.setObjectName("painting_image_random")
        
        self.stackedWidget_2 = QtWidgets.QStackedWidget(parent=self.page_2)
        self.stackedWidget_2.setGeometry(QtCore.QRect(160, 410, 301, 301))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        
        self.stack_01 = QtWidgets.QWidget()
        self.stack_01.setObjectName("stack_01")
        
        self.text_choose = QtWidgets.QLabel(parent=self.stack_01)
        self.text_choose.setGeometry(QtCore.QRect(20, 20, 261, 51))
        
        font = QtGui.QFont()
        font.setPointSize(16)
        
        self.text_choose.setFont(font)
        self.text_choose.setWordWrap(True)
        self.text_choose.setObjectName("text_choose")
        
        self.drop_down_artist = QtWidgets.QComboBox(parent=self.stack_01)
        self.drop_down_artist.setGeometry(QtCore.QRect(30, 100, 231, 141))
        
        font = QtGui.QFont()
        font.setPointSize(20)
        
        self.drop_down_artist.setFont(font)
        self.drop_down_artist.setObjectName("drop_down_artist")
        self.drop_down_artist.addItem("")
        self.drop_down_artist.addItem("")
        
        self.go_button = QtWidgets.QPushButton(parent=self.stack_01)
        self.go_button.setGeometry(QtCore.QRect(85, 245, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.go_button.setFont(font)
        self.go_button.setObjectName("Go_Button")
        self.go_button.setText("GO")
        
        self.stackedWidget_2.addWidget(self.stack_01)
        
        self.stack_02 = QtWidgets.QWidget()
        self.stack_02.setObjectName("stack_02")
        
        self.machine_answer = QtWidgets.QLabel(parent=self.stack_02)
        self.machine_answer.setGeometry(QtCore.QRect(10, 80, 281, 121))
        self.machine_answer.setObjectName("machine_answer")
        
        self.label = QtWidgets.QLabel(parent=self.stack_02)
        self.label.setGeometry(QtCore.QRect(90, 40, 141, 21))
        self.label.setObjectName("label")
        
        self.stackedWidget_2.addWidget(self.stack_02)
        self.pushButton_start2 = QtWidgets.QPushButton(parent=self.page_2)
        self.pushButton_start2.setGeometry(QtCore.QRect(160, 250, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.pushButton_start2.setFont(font)
        self.pushButton_start2.setObjectName("pushButton_start2")
        self.text_start_request_2 = QtWidgets.QLabel(parent=self.page_2)
        self.text_start_request_2.setGeometry(QtCore.QRect(160, 140, 301, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.text_start_request_2.setFont(font)
        self.text_start_request_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.text_start_request_2.setObjectName("text_start_request_2")
        self.title2 = QtWidgets.QLabel(parent=self.page_2)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.title2.setFont(font)
        self.title2.setObjectName("title2")
        self.line = QtWidgets.QFrame(parent=self.page_2)
        self.line.setGeometry(QtCore.QRect(-10, 900, 1521, 20))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(parent=self.page_2)
        self.line_2.setGeometry(QtCore.QRect(450, 120, 20, 751))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(parent=self.page_2)
        self.line_3.setGeometry(QtCore.QRect(150, 120, 20, 751))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_3 = QtWidgets.QLabel(parent=self.page_2)
        self.label_3.setGeometry(QtCore.QRect(160, 930, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(parent=self.page_2)
        self.label_6.setGeometry(QtCore.QRect(780, 930, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.stackedWidget.addWidget(self.page_2)
        
        
        ## PAGE 1 _____________________________________________________________
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.painting_image1 = QtWidgets.QLabel(parent=self.page_1)
        self.painting_image1.setGeometry(QtCore.QRect(40, 170, 331, 431))
        self.painting_image1.setText("")
        self.painting_image1.setPixmap(QtGui.QPixmap("../example_paintings/Vincent_van_Gogh_210.jpg"))
        self.painting_image1.setScaledContents(True)
        self.painting_image1.setObjectName("painting_image1")
        self.text_start_request = QtWidgets.QLabel(parent=self.page_1)
        self.text_start_request.setGeometry(QtCore.QRect(730, 740, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.text_start_request.setFont(font)
        self.text_start_request.setObjectName("text_start_request")
        self.pushButton_start_1 = QtWidgets.QPushButton(parent=self.page_1)
        self.pushButton_start_1.setGeometry(QtCore.QRect(990, 720, 401, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.pushButton_start_1.setFont(font)
        self.pushButton_start_1.setObjectName("pushButton_start_1")
        self.painting_image1_text = QtWidgets.QLabel(parent=self.page_1)
        self.painting_image1_text.setGeometry(QtCore.QRect(60, 620, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.painting_image1_text.setFont(font)
        self.painting_image1_text.setObjectName("painting_image1_text")
        self.painting_image2_text = QtWidgets.QLabel(parent=self.page_1)
        self.painting_image2_text.setGeometry(QtCore.QRect(430, 620, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.painting_image2_text.setFont(font)
        self.painting_image2_text.setObjectName("painting_image2_text")
        self.painting_image2 = QtWidgets.QLabel(parent=self.page_1)
        self.painting_image2.setGeometry(QtCore.QRect(400, 170, 331, 431))
        self.painting_image2.setText("")
        self.painting_image2.setPixmap(QtGui.QPixmap("../example_paintings/Vincent_van_Gogh_210.jpg"))
        self.painting_image2.setScaledContents(True)
        self.painting_image2.setObjectName("painting_image2")
        self.painting_image3_text = QtWidgets.QLabel(parent=self.page_1)
        self.painting_image3_text.setGeometry(QtCore.QRect(780, 620, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.painting_image3_text.setFont(font)
        self.painting_image3_text.setObjectName("painting_image3_text")
        self.painting_image3 = QtWidgets.QLabel(parent=self.page_1)
        self.painting_image3.setGeometry(QtCore.QRect(760, 170, 331, 431))
        self.painting_image3.setText("")
        self.painting_image3.setPixmap(QtGui.QPixmap("../example_paintings/Vincent_van_Gogh_210.jpg"))
        self.painting_image3.setScaledContents(True)
        self.painting_image3.setObjectName("painting_image3")
        self.painting_image4_text = QtWidgets.QLabel(parent=self.page_1)
        self.painting_image4_text.setGeometry(QtCore.QRect(1140, 620, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.painting_image4_text.setFont(font)
        self.painting_image4_text.setObjectName("painting_image4_text")
        self.painting_image4 = QtWidgets.QLabel(parent=self.page_1)
        self.painting_image4.setGeometry(QtCore.QRect(1120, 170, 331, 431))
        self.painting_image4.setText("")
        self.painting_image4.setPixmap(QtGui.QPixmap("../example_paintings/Vincent_van_Gogh_210.jpg"))
        self.painting_image4.setScaledContents(True)
        self.painting_image4.setObjectName("painting_image4")
        self.text_project = QtWidgets.QLabel(parent=self.page_1)
        self.text_project.setGeometry(QtCore.QRect(60, 680, 531, 191))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_project.setFont(font)
        self.text_project.setObjectName("text_project")
        self.title2_2 = QtWidgets.QLabel(parent=self.page_1)
        self.title2_2.setGeometry(QtCore.QRect(510, 20, 378, 64))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.title2_2.setFont(font)
        self.title2_2.setObjectName("title2_2")
        self.label_4 = QtWidgets.QLabel(parent=self.page_1)
        self.label_4.setGeometry(QtCore.QRect(160, 930, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.page_1)
        self.label_5.setGeometry(QtCore.QRect(730, 930, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.line_4 = QtWidgets.QFrame(parent=self.page_1)
        self.line_4.setGeometry(QtCore.QRect(-10, 900, 1521, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_6 = QtWidgets.QFrame(parent=self.page_1)
        self.line_6.setGeometry(QtCore.QRect(-10, 650, 1531, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.stackedWidget.addWidget(self.page_1)
        
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1525, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.text_choose.setText(_translate("MainWindow", "Please choose your answer from the drop down menu :"))
        self.drop_down_artist.setItemText(0, _translate("MainWindow", "Picasso"))
        self.drop_down_artist.setItemText(1, _translate("MainWindow", "Gaugain"))
        self.machine_answer.setText(_translate("MainWindow", "example: Pablo Picasso \n"
"machine Answer \n"
"and all information gathered \n"
"by machine etc. \n"
"including correct answer"))
        self.label.setText(_translate("MainWindow", "Machine Answer"))
        self.pushButton_start2.setText(_translate("MainWindow", "Reload image"))
        self.text_start_request_2.setText(_translate("MainWindow", "Push the button to begin\n"
" guessing the artist "))
        self.title2.setText(_translate("MainWindow", "Artist Recognition"))
        self.label_3.setText(_translate("MainWindow", "© 2023 von Dewitz, B., Al Turk, M., Wozniak, A."))
        self.label_6.setText(_translate("MainWindow", "Our Team  |      Contact Us     |      Imprint     |   Terms  "))
        self.text_start_request.setText(_translate("MainWindow", "Push the button to begin"))
        self.pushButton_start_1.setText(_translate("MainWindow", "Let\'s Start"))
        self.painting_image1_text.setText(_translate("MainWindow", "Artist name"))
        self.painting_image2_text.setText(_translate("MainWindow", "Artist name"))
        self.painting_image3_text.setText(_translate("MainWindow", "Artist name"))
        self.painting_image4_text.setText(_translate("MainWindow", "Artist name"))
        self.text_project.setText(_translate("MainWindow", "The idea of the project was to create a machine learning algorithm in Python\n"
"using libraries such as NumPy, Keras, and TensorFlow. Qt Creator 6 was used \n"
"to build the presented graphical user interface. \n"
"The images necessary for training and testing the algorithm were downloaded \n"
"from Kaggle (Kaggle Inc. 2023).\n"
"The model is based on ten artist and a total of 3000 images."))
        self.title2_2.setText(_translate("MainWindow", "Artist Recognition"))
        self.label_4.setText(_translate("MainWindow", "© 2023 von Dewitz, B., Al Turk, M., Wozniak, A."))
        self.label_5.setText(_translate("MainWindow", "Our Team  |      Contact Us     |      Imprint     |   Terms  "))
