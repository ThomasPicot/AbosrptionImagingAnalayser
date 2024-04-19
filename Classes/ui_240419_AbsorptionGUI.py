# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '240419_AbsorptionGUIjbOtmJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from pyqtgraph import GraphicsLayoutWidget
from pyqtgraph import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 920)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(67, 67, 67, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(246, 245, 244, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        brush3 = QBrush(QColor(26, 95, 180, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush3)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush4 = QBrush(QColor(246, 245, 244, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        brush5 = QBrush(QColor(190, 190, 190, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush6 = QBrush(QColor(0, 0, 0, 128))
        brush6.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(1200, 920))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Light, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.HighlightedText, brush)
        brush7 = QBrush(QColor(154, 153, 150, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        self.centralwidget.setPalette(palette1)
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.MainVerticalLayout = QVBoxLayout()
        self.MainVerticalLayout.setObjectName(u"MainVerticalLayout")
        self.MainVerticalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.TopHorizontal = QHBoxLayout()
        self.TopHorizontal.setObjectName(u"TopHorizontal")
        self.ImagePanel = QVBoxLayout()
        self.ImagePanel.setObjectName(u"ImagePanel")
        self.DisplaySettings = QHBoxLayout()
        self.DisplaySettings.setObjectName(u"DisplaySettings")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        palette2 = QPalette()
        self.comboBox.setPalette(palette2)
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.comboBox.setFont(font)

        self.DisplaySettings.addWidget(self.comboBox)

        self.toolButton_7 = QToolButton(self.centralwidget)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setFont(font)

        self.DisplaySettings.addWidget(self.toolButton_7)

        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        palette3 = QPalette()
        self.toolButton.setPalette(palette3)
        self.toolButton.setFont(font)

        self.DisplaySettings.addWidget(self.toolButton)

        self.toolButton_3 = QToolButton(self.centralwidget)
        self.toolButton_3.setObjectName(u"toolButton_3")
        palette4 = QPalette()
        self.toolButton_3.setPalette(palette4)
        self.toolButton_3.setFont(font)

        self.DisplaySettings.addWidget(self.toolButton_3)

        self.toolButton_6 = QToolButton(self.centralwidget)
        self.toolButton_6.setObjectName(u"toolButton_6")
        self.toolButton_6.setFont(font)

        self.DisplaySettings.addWidget(self.toolButton_6)

        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        palette5 = QPalette()
        self.comboBox_2.setPalette(palette5)
        self.comboBox_2.setFont(font)

        self.DisplaySettings.addWidget(self.comboBox_2)

        self.MinLabel = QLabel(self.centralwidget)
        self.MinLabel.setObjectName(u"MinLabel")
        palette6 = QPalette()
        self.MinLabel.setPalette(palette6)
        self.MinLabel.setFont(font)

        self.DisplaySettings.addWidget(self.MinLabel)

        self.MinSlider = QSlider(self.centralwidget)
        self.MinSlider.setObjectName(u"MinSlider")
        palette7 = QPalette()
        self.MinSlider.setPalette(palette7)
        self.MinSlider.setFont(font)
        self.MinSlider.setOrientation(Qt.Horizontal)

        self.DisplaySettings.addWidget(self.MinSlider)

        self.MinSpinBox = QDoubleSpinBox(self.centralwidget)
        self.MinSpinBox.setObjectName(u"MinSpinBox")
        palette8 = QPalette()
        self.MinSpinBox.setPalette(palette8)
        self.MinSpinBox.setFont(font)

        self.DisplaySettings.addWidget(self.MinSpinBox)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.DisplaySettings.addItem(self.horizontalSpacer_5)

        self.MaxLabel = QLabel(self.centralwidget)
        self.MaxLabel.setObjectName(u"MaxLabel")
        palette9 = QPalette()
        self.MaxLabel.setPalette(palette9)
        self.MaxLabel.setFont(font)

        self.DisplaySettings.addWidget(self.MaxLabel)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        palette10 = QPalette()
        self.doubleSpinBox_2.setPalette(palette10)
        self.doubleSpinBox_2.setFont(font)

        self.DisplaySettings.addWidget(self.doubleSpinBox_2)

        self.MaxSlider = QSlider(self.centralwidget)
        self.MaxSlider.setObjectName(u"MaxSlider")
        palette11 = QPalette()
        self.MaxSlider.setPalette(palette11)
        self.MaxSlider.setFont(font)
        self.MaxSlider.setOrientation(Qt.Horizontal)

        self.DisplaySettings.addWidget(self.MaxSlider)


        self.ImagePanel.addLayout(self.DisplaySettings)

        self.horizontalSpacer = QSpacerItem(100, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.ImagePanel.addItem(self.horizontalSpacer)

        self.ImageHistograms = QGridLayout()
        self.ImageHistograms.setObjectName(u"ImageHistograms")
        self.widget_Hcut = PlotWidget(self.centralwidget)
        self.widget_Hcut.setObjectName(u"widget_Hcut")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_Hcut.sizePolicy().hasHeightForWidth())
        self.widget_Hcut.setSizePolicy(sizePolicy2)
        self.widget_Hcut.setMinimumSize(QSize(0, 80))
        self.widget_Hcut.setMaximumSize(QSize(16777215, 60))
        self.widget_Hcut.setFont(font)

        self.ImageHistograms.addWidget(self.widget_Hcut, 2, 0, 1, 2)

        self.widgetFrame = GraphicsLayoutWidget(self.centralwidget)
        self.widgetFrame.setObjectName(u"widgetFrame")
        sizePolicy1.setHeightForWidth(self.widgetFrame.sizePolicy().hasHeightForWidth())
        self.widgetFrame.setSizePolicy(sizePolicy1)
        self.widgetFrame.setMinimumSize(QSize(400, 300))
        self.widgetFrame.setMaximumSize(QSize(19000, 19000))
        self.widgetFrame.setFont(font)
        self.widgetFrame.setStyleSheet(u"")

        self.ImageHistograms.addWidget(self.widgetFrame, 0, 0, 2, 2)

        self.widget_Vcut = PlotWidget(self.centralwidget)
        self.widget_Vcut.setObjectName(u"widget_Vcut")
        sizePolicy.setHeightForWidth(self.widget_Vcut.sizePolicy().hasHeightForWidth())
        self.widget_Vcut.setSizePolicy(sizePolicy)
        self.widget_Vcut.setMinimumSize(QSize(80, 0))
        self.widget_Vcut.setMaximumSize(QSize(60, 16777215))
        self.widget_Vcut.setFont(font)

        self.ImageHistograms.addWidget(self.widget_Vcut, 0, 2, 1, 1)


        self.ImagePanel.addLayout(self.ImageHistograms)


        self.TopHorizontal.addLayout(self.ImagePanel)

        self.verticalSpacer_3 = QSpacerItem(0, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.TopHorizontal.addItem(self.verticalSpacer_3)

        self.horizontalSpacer_6 = QSpacerItem(2, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.TopHorizontal.addItem(self.horizontalSpacer_6)

        self.AnalysisPanel = QVBoxLayout()
        self.AnalysisPanel.setObjectName(u"AnalysisPanel")
        self.AnalysisPanel.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.AnalysisPanel.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setMinimumSize(QSize(180, 0))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(24)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"    background-color: #333; /* Dark background color */\n"
"    color: red; /* Red numbers */\n"
"    font-size: calc(10px + 2vw); /* Adjust font size dynamically */\n"
"    font-family: Arial, sans-serif; /* Specify font family */\n"
"    padding: 10px; /* Add padding for spacing */\n"
"    text-align: center; /* Center the text horizontally */\n"
"    max-width: 100%; /* Limit the width to prevent overflow */\n"
"    white-space: nowrap; /* Prevent text from wrapping */\n"
"    overflow: hidden; /* Hide overflowing text */\n"
"    border: 3px solid #555; /* Dark framing */\n"
"    border-radius: 10px; /* Rounded edges */")
        self.label.setFrameShape(QFrame.WinPanel)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setLineWidth(0)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.AnalysisPanel.addLayout(self.horizontalLayout)

        self.FitPanel = QGroupBox(self.centralwidget)
        self.FitPanel.setObjectName(u"FitPanel")
        self.FitPanel.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.FitPanel.sizePolicy().hasHeightForWidth())
        self.FitPanel.setSizePolicy(sizePolicy1)
        palette12 = QPalette()
        self.FitPanel.setPalette(palette12)
        self.FitPanel.setFont(font)
        self.FitPanel.setCheckable(True)
        self.gridLayout_2 = QGridLayout(self.FitPanel)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radioButton = QRadioButton(self.FitPanel)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_2.addWidget(self.radioButton, 0, 0, 1, 1)


        self.AnalysisPanel.addWidget(self.FitPanel)


        self.TopHorizontal.addLayout(self.AnalysisPanel)


        self.MainVerticalLayout.addLayout(self.TopHorizontal)

        self.verticalSpacer = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.MainVerticalLayout.addItem(self.verticalSpacer)

        self.BottomHorizontal = QHBoxLayout()
        self.BottomHorizontal.setObjectName(u"BottomHorizontal")
        self.CameraSettings = QGroupBox(self.centralwidget)
        self.CameraSettings.setObjectName(u"CameraSettings")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.CameraSettings.sizePolicy().hasHeightForWidth())
        self.CameraSettings.setSizePolicy(sizePolicy4)
        self.CameraSettings.setFont(font)
        self.formLayout = QFormLayout(self.CameraSettings)
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(self.CameraSettings)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.comboBox_camchoice = QComboBox(self.CameraSettings)
        self.comboBox_camchoice.addItem("")
        self.comboBox_camchoice.addItem("")
        self.comboBox_camchoice.addItem("")
        self.comboBox_camchoice.setObjectName(u"comboBox_camchoice")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBox_camchoice)

        self.label_4 = QLabel(self.CameraSettings)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.spinBox_exptime = QDoubleSpinBox(self.CameraSettings)
        self.spinBox_exptime.setObjectName(u"spinBox_exptime")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spinBox_exptime)

        self.label_6 = QLabel(self.CameraSettings)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_6)

        self.label_8 = QLabel(self.CameraSettings)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_8)

        self.spinBox_pixelsize = QDoubleSpinBox(self.CameraSettings)
        self.spinBox_pixelsize.setObjectName(u"spinBox_pixelsize")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.spinBox_pixelsize)

        self.checkBo_ignoreTimeout = QCheckBox(self.CameraSettings)
        self.checkBo_ignoreTimeout.setObjectName(u"checkBo_ignoreTimeout")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.checkBo_ignoreTimeout)

        self.checkBox_trigOn = QCheckBox(self.CameraSettings)
        self.checkBox_trigOn.setObjectName(u"checkBox_trigOn")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.checkBox_trigOn)

        self.label_5 = QLabel(self.CameraSettings)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.comboBox_TrigType = QComboBox(self.CameraSettings)
        self.comboBox_TrigType.addItem("")
        self.comboBox_TrigType.addItem("")
        self.comboBox_TrigType.setObjectName(u"comboBox_TrigType")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBox_TrigType)


        self.BottomHorizontal.addWidget(self.CameraSettings)

        self.Acquisition = QGroupBox(self.centralwidget)
        self.Acquisition.setObjectName(u"Acquisition")
        sizePolicy2.setHeightForWidth(self.Acquisition.sizePolicy().hasHeightForWidth())
        self.Acquisition.setSizePolicy(sizePolicy2)
        self.Acquisition.setFont(font)
        self.formLayout_2 = QFormLayout(self.Acquisition)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.pushButton_start_acq = QPushButton(self.Acquisition)
        self.pushButton_start_acq.setObjectName(u"pushButton_start_acq")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_start_acq.sizePolicy().hasHeightForWidth())
        self.pushButton_start_acq.setSizePolicy(sizePolicy5)
        palette13 = QPalette()
        self.pushButton_start_acq.setPalette(palette13)
        self.pushButton_start_acq.setFont(font)
        self.pushButton_start_acq.setStyleSheet(u"")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.pushButton_start_acq)

        self.pushButton_stop_acq = QPushButton(self.Acquisition)
        self.pushButton_stop_acq.setObjectName(u"pushButton_stop_acq")
        sizePolicy5.setHeightForWidth(self.pushButton_stop_acq.sizePolicy().hasHeightForWidth())
        self.pushButton_stop_acq.setSizePolicy(sizePolicy5)
        palette14 = QPalette()
        self.pushButton_stop_acq.setPalette(palette14)
        self.pushButton_stop_acq.setFont(font)
        self.pushButton_stop_acq.setStyleSheet(u"")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.pushButton_stop_acq)

        self.label_7 = QLabel(self.Acquisition)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.pushButton_takePicture = QPushButton(self.Acquisition)
        self.pushButton_takePicture.setObjectName(u"pushButton_takePicture")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.pushButton_takePicture)


        self.BottomHorizontal.addWidget(self.Acquisition)

        self.Averaging = QGroupBox(self.centralwidget)
        self.Averaging.setObjectName(u"Averaging")
        self.Averaging.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.Averaging.sizePolicy().hasHeightForWidth())
        self.Averaging.setSizePolicy(sizePolicy4)
        self.Averaging.setFont(font)
        self.Averaging.setCheckable(True)
        self.pushButton_clear_crosshair = QPushButton(self.Averaging)
        self.pushButton_clear_crosshair.setObjectName(u"pushButton_clear_crosshair")
        self.pushButton_clear_crosshair.setGeometry(QRect(0, 60, 349, 35))
        sizePolicy5.setHeightForWidth(self.pushButton_clear_crosshair.sizePolicy().hasHeightForWidth())
        self.pushButton_clear_crosshair.setSizePolicy(sizePolicy5)
        palette15 = QPalette()
        self.pushButton_clear_crosshair.setPalette(palette15)
        self.pushButton_clear_crosshair.setFont(font)
        self.pushButton_clear_crosshair.setStyleSheet(u"")
        self.pushButton_disarm = QPushButton(self.Averaging)
        self.pushButton_disarm.setObjectName(u"pushButton_disarm")
        self.pushButton_disarm.setEnabled(False)
        self.pushButton_disarm.setGeometry(QRect(160, 90, 103, 25))
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton_disarm.sizePolicy().hasHeightForWidth())
        self.pushButton_disarm.setSizePolicy(sizePolicy6)
        self.pushButton_disarm.setMinimumSize(QSize(0, 0))
        self.pushButton_disarm.setMaximumSize(QSize(16777215, 25))
        palette16 = QPalette()
        self.pushButton_disarm.setPalette(palette16)
        self.pushButton_disarm.setFont(font)
        self.pushButton_disarm.setStyleSheet(u"")
        self.pushButtonArm = QPushButton(self.Averaging)
        self.pushButtonArm.setObjectName(u"pushButtonArm")
        self.pushButtonArm.setGeometry(QRect(290, 110, 61, 25))
        sizePolicy6.setHeightForWidth(self.pushButtonArm.sizePolicy().hasHeightForWidth())
        self.pushButtonArm.setSizePolicy(sizePolicy6)
        self.pushButtonArm.setMaximumSize(QSize(16777215, 25))
        palette17 = QPalette()
        self.pushButtonArm.setPalette(palette17)
        self.pushButtonArm.setFont(font)
        self.pushButtonArm.setStyleSheet(u"")
        self.pushButton_setROI = QPushButton(self.Averaging)
        self.pushButton_setROI.setObjectName(u"pushButton_setROI")
        self.pushButton_setROI.setGeometry(QRect(20, 90, 122, 35))
        sizePolicy5.setHeightForWidth(self.pushButton_setROI.sizePolicy().hasHeightForWidth())
        self.pushButton_setROI.setSizePolicy(sizePolicy5)
        palette18 = QPalette()
        self.pushButton_setROI.setPalette(palette18)
        self.pushButton_setROI.setFont(font)
        self.pushButton_setROI.setStyleSheet(u"")
        self.pushButton_clear_ROI = QPushButton(self.Averaging)
        self.pushButton_clear_ROI.setObjectName(u"pushButton_clear_ROI")
        self.pushButton_clear_ROI.setGeometry(QRect(30, 140, 101, 21))
        sizePolicy5.setHeightForWidth(self.pushButton_clear_ROI.sizePolicy().hasHeightForWidth())
        self.pushButton_clear_ROI.setSizePolicy(sizePolicy5)
        palette19 = QPalette()
        self.pushButton_clear_ROI.setPalette(palette19)
        self.pushButton_clear_ROI.setFont(font)
        self.pushButton_clear_ROI.setStyleSheet(u"")
        self.pushButton_apply_ROI = QPushButton(self.Averaging)
        self.pushButton_apply_ROI.setObjectName(u"pushButton_apply_ROI")
        self.pushButton_apply_ROI.setGeometry(QRect(10, 180, 141, 31))
        sizePolicy5.setHeightForWidth(self.pushButton_apply_ROI.sizePolicy().hasHeightForWidth())
        self.pushButton_apply_ROI.setSizePolicy(sizePolicy5)
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush8 = QBrush(QColor(40, 40, 40, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush8)
        brush9 = QBrush(QColor(72, 72, 72, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette20.setBrush(QPalette.Active, QPalette.Light, brush9)
        brush10 = QBrush(QColor(60, 60, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette20.setBrush(QPalette.Active, QPalette.Midlight, brush10)
        brush11 = QBrush(QColor(24, 24, 24, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette20.setBrush(QPalette.Active, QPalette.Dark, brush11)
        brush12 = QBrush(QColor(32, 32, 32, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette20.setBrush(QPalette.Active, QPalette.Mid, brush12)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush)
        palette20.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush8)
        brush13 = QBrush(QColor(0, 0, 0, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette20.setBrush(QPalette.Active, QPalette.Shadow, brush13)
        palette20.setBrush(QPalette.Active, QPalette.AlternateBase, brush11)
        brush14 = QBrush(QColor(255, 255, 220, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette20.setBrush(QPalette.Active, QPalette.ToolTipBase, brush14)
        palette20.setBrush(QPalette.Active, QPalette.ToolTipText, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette20.setBrush(QPalette.Inactive, QPalette.Light, brush9)
        palette20.setBrush(QPalette.Inactive, QPalette.Midlight, brush10)
        palette20.setBrush(QPalette.Inactive, QPalette.Dark, brush11)
        palette20.setBrush(QPalette.Inactive, QPalette.Mid, brush12)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette20.setBrush(QPalette.Inactive, QPalette.Shadow, brush13)
        palette20.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush11)
        palette20.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush14)
        palette20.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette20.setBrush(QPalette.Disabled, QPalette.Light, brush9)
        palette20.setBrush(QPalette.Disabled, QPalette.Midlight, brush10)
        palette20.setBrush(QPalette.Disabled, QPalette.Dark, brush11)
        palette20.setBrush(QPalette.Disabled, QPalette.Mid, brush12)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        palette20.setBrush(QPalette.Disabled, QPalette.Shadow, brush13)
        brush15 = QBrush(QColor(48, 48, 48, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette20.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush15)
        palette20.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush14)
        palette20.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.pushButton_apply_ROI.setPalette(palette20)
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.pushButton_apply_ROI.setFont(font2)
        self.pushButton_apply_ROI.setStyleSheet(u"")

        self.BottomHorizontal.addWidget(self.Averaging)

        self.BatchProcessing = QGroupBox(self.centralwidget)
        self.BatchProcessing.setObjectName(u"BatchProcessing")
        self.BatchProcessing.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.BatchProcessing.sizePolicy().hasHeightForWidth())
        self.BatchProcessing.setSizePolicy(sizePolicy4)
        self.BatchProcessing.setFont(font)
        self.BatchProcessing.setCheckable(True)

        self.BottomHorizontal.addWidget(self.BatchProcessing)


        self.MainVerticalLayout.addLayout(self.BottomHorizontal)


        self.gridLayout.addLayout(self.MainVerticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Andor GUI", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Optical density", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Number of atoms", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Bright image", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Dark image", None))

#if QT_CONFIG(tooltip)
        self.toolButton_7.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Set Region of Interest (ROI)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_7.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_6.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Default colormap", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Hot", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Magma", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Jet", None))

        self.MinLabel.setText(QCoreApplication.translate("MainWindow", u"Min.", None))
        self.MaxLabel.setText(QCoreApplication.translate("MainWindow", u"Max.", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Number of atoms", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"1.03 x 10\u2078", None))
        self.FitPanel.setTitle(QCoreApplication.translate("MainWindow", u"Fit", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Work in progress", None))
        self.CameraSettings.setTitle(QCoreApplication.translate("MainWindow", u"Camera settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Camera :", None))
        self.comboBox_camchoice.setItemText(0, QCoreApplication.translate("MainWindow", u"Detection 1", None))
        self.comboBox_camchoice.setItemText(1, QCoreApplication.translate("MainWindow", u"Detection 2", None))
        self.comboBox_camchoice.setItemText(2, QCoreApplication.translate("MainWindow", u"Detection 3", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Exposure time (ms) :", None))
        self.label_6.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Pixel size (\u00b5m) :", None))
        self.checkBo_ignoreTimeout.setText(QCoreApplication.translate("MainWindow", u"Ignore Timeout", None))
        self.checkBox_trigOn.setText(QCoreApplication.translate("MainWindow", u"Trigger On", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Trigger type :", None))
        self.comboBox_TrigType.setItemText(0, QCoreApplication.translate("MainWindow", u"InputLines", None))
        self.comboBox_TrigType.setItemText(1, QCoreApplication.translate("MainWindow", u"Software", None))

        self.Acquisition.setTitle(QCoreApplication.translate("MainWindow", u"Acquisition", None))
        self.pushButton_start_acq.setText(QCoreApplication.translate("MainWindow", u"Start acquisition", None))
        self.pushButton_stop_acq.setText(QCoreApplication.translate("MainWindow", u"Stop acquisition", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Take picture now :", None))
        self.pushButton_takePicture.setText(QCoreApplication.translate("MainWindow", u"Take Picture !", None))
        self.Averaging.setTitle(QCoreApplication.translate("MainWindow", u"Averaging", None))
        self.pushButton_clear_crosshair.setText(QCoreApplication.translate("MainWindow", u"Clear crosshair", None))
        self.pushButton_disarm.setText(QCoreApplication.translate("MainWindow", u"Disarm", None))
        self.pushButtonArm.setText(QCoreApplication.translate("MainWindow", u"Arm", None))
        self.pushButton_setROI.setText(QCoreApplication.translate("MainWindow", u"Set ROI", None))
        self.pushButton_clear_ROI.setText(QCoreApplication.translate("MainWindow", u"Clear ROI", None))
        self.pushButton_apply_ROI.setText(QCoreApplication.translate("MainWindow", u"Apply ROI", None))
        self.BatchProcessing.setTitle(QCoreApplication.translate("MainWindow", u"Batch processing", None))
    # retranslateUi

