from PyQt5 import QtCore, QtGui, QtWidgets

from db import DB


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        db = DB()
        self.questions = db.load_data()

        self.correct = 0
        self.quantity = len(self.questions)
        self.index = 0


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setStatusTip("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: #D4DEF4;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 160, 611, 101))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.question = QtWidgets.QLabel(self.centralwidget)
        self.question.setGeometry(QtCore.QRect(350, 280, 611, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.question.setFont(font)
        self.question.setToolTip("")
        self.question.setStyleSheet("")
        self.question.setText("")
        self.question.setAlignment(QtCore.Qt.AlignCenter)
        self.question.setObjectName("question")
        self.answer = QtWidgets.QLineEdit(self.centralwidget)
        self.answer.setGeometry(QtCore.QRect(350, 450, 621, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.answer.setFont(font)
        self.answer.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.answer.setStyleSheet("")
        self.answer.setObjectName("answer")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(510, 580, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.question.setText(self.questions[self.index]['question'])
        self.submit.clicked.connect(self.show_questions)
        self.answer.returnPressed.connect(self.show_questions)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Викторина по словам"))
        self.label.setText(_translate("MainWindow", "Напишите перевод данного слова"))
        self.answer.setPlaceholderText(_translate("MainWindow", "Ваш ответ"))
        self.submit.setText(_translate("MainWindow", "Отправить ответ"))

    def show_questions(self):
        if self.index < self.quantity:
            self.questions[self.index]['user_answer'] = self.answer.text().lower()

            if self.questions[self.index]['answer'] == self.questions[self.index]['user_answer']:
                self.correct += 1

            self.answer.clear()
            self.index += 1

            if self.index < self.quantity:
                self.question.setText(self.questions[self.index]['question'])

            else:
                self.answer.hide()
                self.submit.hide()
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(25)
                self.label.setFont(font)
                self.label.setText(f'Вы ответили на {self.correct} вопросов из {self.quantity}')
                self.question.hide()
