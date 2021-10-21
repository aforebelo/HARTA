from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QBrush, QPen, QPainter, QImage, QPixmap, QColor
from PyQt5.QtCore import Qt, QRect
from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import os
import cv2 as cv
import numpy as np

import _automatic_
import _semiautomatic_
import resources

global flag


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        'STYLESHEET'
        buttonStyle = """
        QPushButton{
                border-style: solid;
                border-width: 0px;
                border-radius: 10px;
                background-color: rgb(234,234,234);
        }
        QPushButton::hover{
                background-color: rgb(183,181,181);
        }
        """
        groupBoxStyle = """
        QGroupBox{
                background-color:none;
                border: 1px solid rgb(183,181,181);
                border-radius: 10px;
        }
        """

        closeStyle = """
        QPushButton{
            border-style: solid;
            border-width: 0px;
            border-radius: 10px;
            background-color: rgb(234,67,53);
            color:rgb(255, 255, 255)
        }
        QPushButton::hover{
            background-color: rgb(172,16,12);
        }
        """

        generateVolumeStyle = """
        QPushButton{
                border-style: solid;
                border-width: 0px;
                border-radius: 10px;
                background-color: rgb(70,136,244);
                color:rgb(255, 255, 255)
        }

        QPushButton::hover
        {
                background-color: rgb(18,77,150);
        }
        """

        boxStyle = """
        QGroupBox{
            border-style: none;
            background-color:none;
        }
        """

        textEditStyle = """
        QTextEdit{
            border-style: solid;
            border-width: 1px;
            border-radius: 10px;
            border-color: rgb(183,181,181);
        }
        """

        lineEditStyle = """
        QLineEdit{
            border-style: solid;
            border-width: 1px;
            border-radius: 10px;
            border-color: rgb(183,181,181);
        }
        """

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1208, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1208, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1208, 700))
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.filename = QtWidgets.QLineEdit(self.centralwidget)
        self.filename.setGeometry(QtCore.QRect(740, 50, 411, 28))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.filename.setFont(font)
        self.filename.setStyleSheet(lineEditStyle)
        self.filename.setFrame(False)
        self.filename.setObjectName("filename")
        self.openFile = QtWidgets.QPushButton(self.centralwidget)
        self.openFile.setGeometry(QtCore.QRect(600, 50, 131, 28))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.openFile.setFont(font)
        self.openFile.setStyleSheet(buttonStyle)
        self.openFile.setObjectName("openFile")
        self.imageHeart = QtWidgets.QLabel(self.centralwidget)
        self.imageHeart.setEnabled(True)
        self.imageHeart.setGeometry(QtCore.QRect(30, 20, 520, 520))
        self.imageHeart.setText("")
        self.imageHeart.setPixmap(QtGui.QPixmap(":/aux/default_txt.png"))
        self.imageHeart.setScaledContents(True)
        self.imageHeart.setAlignment(QtCore.Qt.AlignCenter)
        self.imageHeart.setObjectName("imageHeart")
        self.manual_intervention = QtWidgets.QGroupBox(self.centralwidget)
        self.manual_intervention.setEnabled(True)
        self.manual_intervention.setGeometry(QtCore.QRect(590, 320, 591, 211))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.manual_intervention.setFont(font)
        self.manual_intervention.setStyleSheet(groupBoxStyle)
        self.manual_intervention.setTitle("")
        self.manual_intervention.setObjectName("manual_intervention")
        self.duringEditionBox = QtWidgets.QGroupBox(self.manual_intervention)
        self.duringEditionBox.setGeometry(QtCore.QRect(0, 15, 571, 91))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.duringEditionBox.setFont(font)
        self.duringEditionBox.setStyleSheet(boxStyle)
        self.duringEditionBox.setTitle("")
        self.duringEditionBox.setObjectName("duringEditionBox")
        self.generateVolumeSemi = QtWidgets.QPushButton(self.duringEditionBox)
        self.generateVolumeSemi.setGeometry(QtCore.QRect(430, 0, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.generateVolumeSemi.setFont(font)
        self.generateVolumeSemi.setMouseTracking(False)
        self.generateVolumeSemi.setStyleSheet(generateVolumeStyle)
        self.generateVolumeSemi.setObjectName("generateVolumeSemi")
        self.slices = QtWidgets.QTextEdit(self.duringEditionBox)
        self.slices.setGeometry(QtCore.QRect(130, 3, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.slices.setFont(font)
        self.slices.setStyleSheet(textEditStyle)
        self.slices.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.slices.setReadOnly(True)
        self.slices.setObjectName("slices")
        self.slices_edited = QtWidgets.QLabel(self.duringEditionBox)
        self.slices_edited.setGeometry(QtCore.QRect(30, 10, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        self.slices_edited.setFont(font)
        self.slices_edited.setObjectName("slices_edited")
        self.infoAuto_2 = QtWidgets.QGroupBox(self.duringEditionBox)
        self.infoAuto_2.setGeometry(QtCore.QRect(320, 50, 251, 41))
        self.infoAuto_2.setStyleSheet(boxStyle)
        self.infoAuto_2.setTitle("")
        self.infoAuto_2.setObjectName("infoAuto_2")
        self.textAuto_2 = QtWidgets.QLabel(self.infoAuto_2)
        self.textAuto_2.setGeometry(QtCore.QRect(30, 10, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.textAuto_2.setFont(font)
        self.textAuto_2.setStyleSheet("background-color:none;")
        self.textAuto_2.setObjectName("textAuto_2")
        self.iconAuto_2 = QtWidgets.QLabel(self.infoAuto_2)
        self.iconAuto_2.setGeometry(QtCore.QRect(10, 10, 15, 15))
        self.iconAuto_2.setAutoFillBackground(False)
        self.iconAuto_2.setText("")
        self.iconAuto_2.setPixmap(QtGui.QPixmap(":/aux/info.png"))
        self.iconAuto_2.setScaledContents(True)
        self.iconAuto_2.setObjectName("iconAuto_2")
        self.afterEditionBox = QtWidgets.QGroupBox(self.manual_intervention)
        self.afterEditionBox.setGeometry(QtCore.QRect(0, 100, 571, 101))
        self.afterEditionBox.setStyleSheet(boxStyle)
        self.afterEditionBox.setTitle("")
        self.afterEditionBox.setObjectName("afterEditionBox")
        self.volume_2 = QtWidgets.QTextEdit(self.afterEditionBox)
        self.volume_2.setGeometry(QtCore.QRect(30, 45, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.volume_2.setFont(font)
        self.volume_2.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.volume_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.volume_2.setReadOnly(True)
        self.volume_2.setObjectName("volume_2")
        self.new_volume = QtWidgets.QLabel(self.afterEditionBox)
        self.new_volume.setGeometry(QtCore.QRect(30, 20, 180, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        self.new_volume.setFont(font)
        self.new_volume.setObjectName("new_volume")
        self.view3DSemi = QtWidgets.QPushButton(self.afterEditionBox)
        self.view3DSemi.setGeometry(QtCore.QRect(430, 60, 131, 28))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        self.view3DSemi.setFont(font)
        self.view3DSemi.setStyleSheet(buttonStyle)
        self.view3DSemi.setObjectName("view3DSemi")
        self.dicom_file = QtWidgets.QLabel(self.centralwidget)
        self.dicom_file.setGeometry(QtCore.QRect(600, 20, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        self.dicom_file.setFont(font)
        self.dicom_file.setObjectName("dicom_file")
        self.generateVolumeAuto = QtWidgets.QPushButton(self.centralwidget)
        self.generateVolumeAuto.setEnabled(True)
        self.generateVolumeAuto.setGeometry(QtCore.QRect(1020, 90, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.generateVolumeAuto.setFont(font)
        self.generateVolumeAuto.setMouseTracking(False)
        self.generateVolumeAuto.setStyleSheet(generateVolumeStyle)
        self.generateVolumeAuto.setObjectName("generateVolumeAuto")
        self.automatic_intervention = QtWidgets.QGroupBox(self.centralwidget)
        self.automatic_intervention.setEnabled(True)
        self.automatic_intervention.setGeometry(QtCore.QRect(590, 180, 591, 111))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.automatic_intervention.setFont(font)
        self.automatic_intervention.setStyleSheet(groupBoxStyle)
        self.automatic_intervention.setTitle("")
        self.automatic_intervention.setObjectName("automatic_intervention")
        self.view3DAuto = QtWidgets.QPushButton(self.automatic_intervention)
        self.view3DAuto.setGeometry(QtCore.QRect(430, 60, 131, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.view3DAuto.setFont(font)
        self.view3DAuto.setStyleSheet(buttonStyle)
        self.view3DAuto.setObjectName("view3DAuto")
        self.volume_detected = QtWidgets.QLabel(self.automatic_intervention)
        self.volume_detected.setGeometry(QtCore.QRect(30, 30, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.volume_detected.setFont(font)
        self.volume_detected.setObjectName("volume_detected")
        self.volume = QtWidgets.QLineEdit(self.automatic_intervention)
        self.volume.setGeometry(QtCore.QRect(30, 55, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.volume.setFont(font)
        self.volume.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.volume.setText("")
        self.volume.setFrame(False)
        self.volume.setReadOnly(True)
        self.volume.setObjectName("volume")
        self.slicesManager = QtWidgets.QGroupBox(self.centralwidget)
        self.slicesManager.setEnabled(False)
        self.slicesManager.setGeometry(QtCore.QRect(30, 550, 521, 101))
        self.slicesManager.setStyleSheet(boxStyle)
        self.slicesManager.setTitle("")
        self.slicesManager.setObjectName("slicesManager")
        self.total_slices = QtWidgets.QTextEdit(self.slicesManager)
        self.total_slices.setGeometry(QtCore.QRect(300, 10, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.total_slices.setFont(font)
        self.total_slices.setMouseTracking(True)
        self.total_slices.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.total_slices.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.total_slices.setLineWidth(1)
        self.total_slices.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.total_slices.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.total_slices.setPlaceholderText("")
        self.total_slices.setObjectName("total_slices")
        self.label_2 = QtWidgets.QLabel(self.slicesManager)
        self.label_2.setGeometry(QtCore.QRect(180, 10, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.of = QtWidgets.QLabel(self.slicesManager)
        self.of.setGeometry(QtCore.QRect(260, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        self.of.setFont(font)
        self.of.setAlignment(QtCore.Qt.AlignCenter)
        self.of.setObjectName("of")
        self.previous = QtWidgets.QPushButton(self.slicesManager)
        self.previous.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        self.previous.setFont(font)
        self.previous.setStyleSheet(buttonStyle)
        self.previous.setObjectName("previous")
        self.next = QtWidgets.QPushButton(self.slicesManager)
        self.next.setGeometry(QtCore.QRect(420, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        self.next.setFont(font)
        self.next.setStyleSheet(buttonStyle)
        self.next.setObjectName("next")
        self.edit_slice = QtWidgets.QPushButton(self.slicesManager)
        self.edit_slice.setGeometry(QtCore.QRect(180, 60, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        self.edit_slice.setFont(font)
        self.edit_slice.setStyleSheet(buttonStyle)
        self.edit_slice.setObjectName("edit_slice")
        self.actual_slice = QtWidgets.QTextEdit(self.slicesManager)
        self.actual_slice.setGeometry(QtCore.QRect(232, 10, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.actual_slice.setFont(font)
        self.actual_slice.setMouseTracking(True)
        self.actual_slice.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.actual_slice.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.actual_slice.setLineWidth(1)
        self.actual_slice.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.actual_slice.setReadOnly(True)
        self.actual_slice.setPlaceholderText("")
        self.actual_slice.setObjectName("actual_slice")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(1020, 600, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet(closeStyle)
        self.closeButton.setObjectName("closeButton")
        self.autoLabel = QtWidgets.QLabel(self.centralwidget)
        self.autoLabel.setGeometry(QtCore.QRect(610, 170, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.autoLabel.setFont(font)
        self.autoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.autoLabel.setObjectName("autoLabel")
        self.semiLabel = QtWidgets.QLabel(self.centralwidget)
        self.semiLabel.setGeometry(QtCore.QRect(610, 310, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.semiLabel.setFont(font)
        self.semiLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.semiLabel.setObjectName("semiLabel")
        self.infoAuto = QtWidgets.QGroupBox(self.centralwidget)
        self.infoAuto.setGeometry(QtCore.QRect(910, 140, 251, 41))
        self.infoAuto.setStyleSheet(boxStyle)
        self.infoAuto.setTitle("")
        self.infoAuto.setObjectName("infoAuto")
        self.textAuto = QtWidgets.QLabel(self.infoAuto)
        self.textAuto.setGeometry(QtCore.QRect(30, 8, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.textAuto.setFont(font)
        self.textAuto.setStyleSheet("background-color:none;")
        self.textAuto.setObjectName("textAuto")
        self.iconAuto = QtWidgets.QLabel(self.infoAuto)
        self.iconAuto.setGeometry(QtCore.QRect(10, 10, 15, 15))
        self.iconAuto.setAutoFillBackground(False)
        self.iconAuto.setText("")
        self.iconAuto.setPixmap(QtGui.QPixmap(":/aux/info.png"))
        self.iconAuto.setScaledContents(True)
        self.iconAuto.setObjectName("iconAuto")
        self.automatic_intervention.raise_()
        self.manual_intervention.raise_()
        self.filename.raise_()
        self.openFile.raise_()
        self.imageHeart.raise_()
        self.dicom_file.raise_()
        self.generateVolumeAuto.raise_()
        self.slicesManager.raise_()
        self.closeButton.raise_()
        self.autoLabel.raise_()
        self.semiLabel.raise_()
        self.infoAuto.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1208, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")

        'Flag to manager the text shown in slices label'
        self.newEdition = False

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    'WINDOWS MANAGER'

    def searchFolder(self):
        global dir
        dir = QFileDialog.getExistingDirectory()
        self.filename.setText(dir)
        self.enableGenerateVolume()

    def openWindow(self):
        self.clearEditLine()

        'Variables to send to edit window'
        self.patient_edit = patient_id
        current_slice = int(self.actual_slice.toPlainText())
        self.slice_edit = current_slice

        "Send data to second window"
        self.secondwindow = SecondWindow(self.slice_edit, self.patient_edit)
        self.secondwindow.submited.connect(self.updateImage)

    def closeProgram(self):
        self.cleanAll()
        MainWindow.close()

    def cleanAll(self):
        dir = 'aux_img'
        for f in os.listdir(dir):
            subdir = f'{dir}/{f}'
            for subf in os.listdir(subdir):
                os.remove(os.path.join(subdir, subf))

    def closeEvent(self, event):
        msgBox = QMessageBox()
        msgBox.setText("Close Program")
        msgBox.setStandardButtons(QMessageBox.Cancel | QMessageBox.Yes | QMessageBox.No);
        msgBox.setDefaultButton(QMessageBox.Yes)
        if msgBox.exec_() == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    'GENERATE AUTOMATIC AND SEMIAUTOMATIC VOLUME'

    def generateVolume(self):
        global patient_id
        global no_slices
        patient_id, no_slices, vol = _automatic_.segmentEpicardialFat(DICOM_DATASET=dir, OUTPUT_FOLDER='aux_img/')
        self.volume.setText(str(round(vol, 1)))
        self.refreshAfterAutomatic()

    def generateNewVolume(self):
        patient_id, no_slices, vol = _semiautomatic_.segmentEpicardialFat(DICOM_DATASET=dir, OUTPUT_FOLDER='aux_img/')
        self.volume_2.setText(str(round(vol, 1)))
        self.refreshAfterSemiAutomatic()

    'INTERFACE MANAGER'

    def updateImage(self, slice_id):
        "Show container"
        self.manual_intervention.show()
        self.semiLabel.show()
        self.afterEditionBox.hide()
        self.slice_id = slice_id
        self.editionHandler()

        'Show the image with new contour'
        self.imageHeart.setPixmap(QtGui.QPixmap(':/aux/edited_successfully_bg.png'))

    def clearEditLine(self):
        'Clean the slices label'
        if self.newEdition:
            self.slices.setText('')
            self.newEdition = False

    def refreshAfterAutomatic(self):
        self.infoAuto.hide()
        self.automatic_intervention.show()
        self.autoLabel.show()
        self.slicesManager.setEnabled(True)
        self.setFirstSlice()

    def refreshAfterSemiAutomatic(self):
        self.afterEditionBox.show()
        self.setFirstSlice()
        self.newEdition = True

    def enableGenerateVolume(self):
        if self.filename.text():
            self.generateVolumeAuto.show()
            self.infoAuto.show()

    'SLICE NAVIGATOR'
    def setFirstSlice(self):
        'Show the number of slices and the first slice'
        self.total_slices.setText(str(no_slices - 1))
        self.actual_slice.setText(str(1))
        'Show image of slice 0'
        self.imageHeart.setPixmap(QtGui.QPixmap(f"aux_img/combined/{patient_id}_{0}_combined.png"))

    def getCurrentSlice(self):
        return self.actual_slice.toPlainText()

    def displaySlice(self):
        current = self.getCurrentSlice()
        slice = int(current) - 1
        self.imageHeart.setPixmap(QtGui.QPixmap(f"aux_img/combined/{patient_id}_{slice}_combined.png"))

    def nextSlice(self):
        current = int(self.getCurrentSlice())
        if current < no_slices - 1:
            self.actual_slice.setText(str(current + 1))
        else:
            self.actual_slice.setText(str(no_slices - 1))
        self.displaySlice()

    def previousSlice(self):
        current = int(self.getCurrentSlice())
        if current > 1:
            self.actual_slice.setText(str(current - 1))
        else:
            self.actual_slice.setText(str(1))
        self.displaySlice()

    def editionHandler(self):
        current = int(self.getCurrentSlice())
        current_text = self.slices.toPlainText()

        if not current_text:
            self.slices.setText(str(current))
        else:
            current_text = f'{current_text}, {current}'
            self.slices.setText(str(current_text))

    'RETRANSLATE UI'

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("HARTA - Epicardial Fat Segmentation Software", "HARTA - Epicardial Fat Segmentation Software"))
        MainWindow.setWindowIcon(QtGui.QIcon(':/aux/logo_w.png'))
        MainWindow.setIconSize(QtCore.QSize(500, 200))
        self.openFile.setText(_translate("MainWindow", "Open Exam..."))
        self.generateVolumeSemi.setText(_translate("MainWindow", "Calculate New \n"
                                                                 "Volume"))
        self.slices_edited.setText(_translate("MainWindow", "Slices edited:"))
        self.textAuto_2.setText(_translate("MainWindow", "This process may takes a few seconds."))
        self.new_volume.setText(_translate("MainWindow", "Epicardial Fat Volume (ml)"))
        self.view3DSemi.setText(_translate("MainWindow", "3D View"))
        self.dicom_file.setText(_translate("MainWindow", "DICOM File"))
        self.generateVolumeAuto.setText(_translate("MainWindow", "Calculate \n"
                                                                 "Volume"))
        self.view3DAuto.setText(_translate("MainWindow", "3D View"))
        self.volume_detected.setText(_translate("MainWindow", "Epicardial Fat Volume (ml)"))
        self.label_2.setText(_translate("MainWindow", "Slice"))
        self.of.setText(_translate("MainWindow", "of"))
        self.previous.setText(_translate("MainWindow", "« Previous"))
        self.next.setText(_translate("MainWindow", "Next »"))
        self.edit_slice.setText(_translate("MainWindow", "Edit slice"))
        self.closeButton.setText(_translate("MainWindow", "Close"))
        self.autoLabel.setText(_translate("MainWindow", "Automatic detection"))
        self.semiLabel.setText(_translate("MainWindow", "Manual intervention"))
        self.textAuto.setText(_translate("MainWindow", "This process may takes a few seconds."))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File..."))

        'ASSIGN FUNCTIONS'
        'Hide all elements'
        self.generateVolumeAuto.hide()
        self.automatic_intervention.hide()
        self.manual_intervention.hide()
        self.infoAuto.hide()
        self.autoLabel.hide()
        self.semiLabel.hide()

        self.view3DAuto.hide()
        self.view3DSemi.hide()

        'Button to search file'
        self.openFile.clicked.connect(self.searchFolder)

        'Button to generate volume'
        self.generateVolumeAuto.clicked.connect(self.generateVolume)
        self.generateVolumeSemi.clicked.connect(self.generateNewVolume)

        'Edit slice button'
        self.edit_slice.clicked.connect(self.openWindow)

        'Button to go to next and previous slice'
        self.next.clicked.connect(self.nextSlice)
        self.previous.clicked.connect(self.previousSlice)

        'Button to close the program'
        self.closeButton.clicked.connect(self.closeProgram)


'***************************************************************************************************************************************************'
'SECOND WINDOW'
'***************************************************************************************************************************************************'


class SecondWindow(QWidget):
    submited = QtCore.pyqtSignal(int)

    def __init__(self, slice_edit, patient_edit):
        super().__init__()
        self.slice_edit = slice_edit
        self.patient_edit = patient_edit
        self.eventhandler = EventHandler(self)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Pericardium delineation")
        self.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.setWindowIcon(QtGui.QIcon(':/aux/logo_w.png'))

        self.img = self.eventhandler
        img = cv.imread(f"aux_img/slices/{self.patient_edit}_{self.slice_edit}.png")
        height, width, bytesPerComponent = img.shape
        bytesPerLine = 3 * width
        cv.cvtColor(img, cv.COLOR_BGR2RGB, img)
        QImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(QImg)
        self.img.setPixmap(pixmap)

        'Size of window'
        self.resize(860, 920)

        'Image properties'
        self.img.setMinimumSize(QtCore.QSize(800, 800))
        self.img.setBaseSize(QtCore.QSize(512, 512))
        self.img.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.img.setScaledContents(True)
        self.img.setGeometry(QRect(30, 30, width, height))
        self.img.setCursor(Qt.CrossCursor)

        'Buttons properties'
        font = QtGui.QFont()
        font.setPointSize(9)
        buttonStyle = """
        QPushButton{
            border-style: solid;
            border-width: 0px;
            border-radius: 10px;
            background-color: rgb(234,234,234);
        }
        QPushButton::hover{
            background-color: rgb(183,181,181);
        }
        """
        ' > Done '
        self.doneButton = QPushButton('Done', self)
        self.doneButton.setGeometry(QRect(624, 860, 93, 28))
        self.doneButton.setFont(font)
        self.doneButton.setStyleSheet(buttonStyle)
        self.doneButton.clicked.connect(self.onSubmit)

        ' > Cancel '
        self.cancelButton = QPushButton('Cancel', self)
        self.cancelButton.setGeometry(QRect(737, 860, 93, 28))
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet(buttonStyle)
        self.cancelButton.clicked.connect(lambda: self.close())

        self.show()

    'SUBMIT HANDLER'

    def onSubmit(self):
        'Get the drawing of path'
        path = self.eventhandler.getPath()
        self.image = QImage(800, 800, QImage.Format_RGB32)
        self.image.fill(Qt.black)
        painter = QPainter(self.image)
        painter.drawImage(self.rect(), self.image, self.image.rect())
        painter.setPen(Qt.white)
        painter.fillPath(path, QBrush(QColor("white")))
        painter.drawPath(path)

        self.submited.emit(self.slice_edit)
        'Save path'
        filePath = f'aux_img/contours/{self.patient_edit}_{int(self.slice_edit) - 1}_c.png'
        self.image.save(filePath)
        'Rescale path to original size of dicom images'
        self.rescaleImage()
        'Save edited image'
        self.combineImages()
        'Clear path'
        self.eventhandler.clearPath()
        'Close the second window'
        self.close()

    def rescaleImage(self):
        filePath = f'aux_img/contours/{self.patient_edit}_{int(self.slice_edit) - 1}_c.png'
        img = cv.imread(filePath)
        dim = (512, 512)
        resized = cv.resize(img, dim, interpolation=cv.INTER_NEAREST)
        cv.imwrite(filePath, resized)

    def combineImages(self):
        mask_rgb = cv.imread(f'aux_img/contours/{self.patient_edit}_{int(self.slice_edit) - 1}_c.png')
        img = cv.imread(f'aux_img/slices/{self.patient_edit}_{int(self.slice_edit) - 1}.png')
        mask_rgb[np.where((mask_rgb == [255, 255, 255]).all(axis=2))] = [22, 9, 224]
        out = cv.addWeighted(mask_rgb, 0.2, img, 1, 0, img)
        filepath = f'aux_img/combined/{self.patient_edit}_{int(self.slice_edit) - 1}_combined.png'
        cv.imwrite(filepath, out)


class EventHandler(QLabel):
    flag = True
    points = []
    path = QtGui.QPainterPath()

    def mousePressEvent(self, event):
        self.points.append(event.pos())
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.flag:
            self.points = []
            self.path = QtGui.QPainterPath()
            self.flag = False
        painter = QPainter(self)
        'Pen of the points'
        painter.setPen(QPen(QColor(224, 9, 22), 10, Qt.SolidLine))
        'Draw all points'
        for pos in self.points:
            painter.drawPoint(pos)
        'Build the path'
        if len(self.points) > 2:
            self.buildPath()
            'Pen of the line'
            painter.setPen(QPen(QColor(70, 136, 244), 3, Qt.SolidLine))
            # Draw path
            painter.drawPath(self.path)

    'PATH HANDLER'
    def buildPath(self):
        factor = 0.5
        self.path = QtGui.QPainterPath(self.points[0])
        for p, current in enumerate(self.points[1:-1], 1):
            'Previous segment'
            source = QtCore.QLineF(self.points[p - 1], current)
            'Next segment'
            target = QtCore.QLineF(current, self.points[p + 1])
            targetAngle = target.angleTo(source)
            if targetAngle > 180:
                angle = (source.angle() + source.angleTo(target) / 2) % 360
            else:
                angle = (target.angle() + target.angleTo(source) / 2) % 360

            revTarget = QtCore.QLineF.fromPolar(source.length() * factor, angle + 180).translated(current)
            cp2 = revTarget.p2()

            if p == 1:
                self.path.quadTo(cp2, current)
            else:
                'Use the control point "cp1" set in the * previous * cycle'
                self.path.cubicTo(cp1, cp2, current)

            revSource = QtCore.QLineF.fromPolar(target.length() * factor, angle).translated(current)
            cp1 = revSource.p2()

        'The final curve, that joins to the last point'
        self.path.quadTo(cp1, self.points[-1])

    def getPath(self):
        return self.path

    def clearPath(self):
        self.flag = True


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())