# The initial screen for setting the sites which the user would like to block

from PyQt5 import QtCore, QtGui, QtWidgets
from survey_screen import UIWindow
import sys
import settings

class Ui_MainWindow(object):
    """ The Block Site window """
    def __init__(self):
        """ Initializes the Ui_MainWindow """
        self.MainWindow = None

        # Starting row
        self.row = 6

        # Site
        self.siteNum = 1
        self.sites = []
        self.siteIndex = 0

        # Delete Button
        self.dbNum = 1
        self.deleteButton = []
        self.dbIndex = 0
        
        # Checkbox
        self.cbNum = 1
        self.checkBox = []
        self.cbIndex = 0
        
        # Time
        self.hour = 0
        self.minute = 0
        
        # Website List
        self.website_list = []
        
        # List From Data
        temp_list = readFile("data.csv")
        try:
            int(temp_list[-1][0])
            self.website_list = temp_list[:-1]
        except IndexError: 
            self.website_list = []
        except ValueError:
            self.website_list = temp_list
        
        # Settings List
        self.settingsList = []

    def switch_screens(self):
        """ Switches the screens from MainWindow to SurveyWindow """
        self.shownWindow = QtWidgets.QMainWindow()
        self.surveyWindow = UIWindow()
        self.surveyWindow.setupUi(self.shownWindow)
        self.surveyWindow.connectActions(self.shownWindow)
        self.surveyWindow.setHour(int(self.surveyWindow.duration_hour))
        self.surveyWindow.setMinute(int(self.surveyWindow.duration_minute))
        self.shownWindow.show()

    def setupUi(self, MainWindow):
        """ Setup Elements in the MainWindow
        
        Args:
            MainWindow(QMainWindow): the main window
        """
        # Window set up
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(settings.block_window_size[0], settings.block_window_size[1])
        window_width = int(self.MainWindow.frameGeometry().width())
        window_height = int(self.MainWindow.frameGeometry().height())
        MainWindow.setStyleSheet("background-color: #1961b2\n")

        # Central Widget -> Widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Set Duration Label (change this to move "Set Duration" label) -> Widget
        self.setDurationLabel = QtWidgets.QLabel(self.centralwidget)
        self.setDurationLabel.setGeometry(QtCore.QRect((window_width / 2) - 70, (window_height / 2) + 50, 140, 30))
        self.setDurationLabel.setStyleSheet("color: #95bfe7")
        self.setDurationLabel.setObjectName("setDurationLabel")
        
        # Grid Layout for Sites (change this to move hour/minute text fields) -> Widget
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect((window_width / 2) - 133, (window_height / 2) + 50, 266, 64))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        
        # Grid Layout for Duration -> GridLayout
        self.durationGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.durationGridLayout.setContentsMargins(0, 0, 0, 0)
        self.durationGridLayout.setObjectName("durationGridLayout")
        
        # Minutes Text Field -> TextEdit
        self.minutesField = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.minutesField.setMaximumSize(QtCore.QSize(150, 30))
        self.minutesField.setStyleSheet("background-color: #c8daf2")
        self.minutesField.setObjectName("minutesField")
        self.durationGridLayout.addWidget(self.minutesField, 1, 1, 1, 1)
        
        # Minutes Label -> Label
        self.minutesLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.minutesLabel.setStyleSheet("color: #95bfe7")
        self.minutesLabel.setObjectName("minutesLabel")
        self.durationGridLayout.addWidget(self.minutesLabel, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        
        # Hours Text Field -> TextEdit
        self.hoursField = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.hoursField.setMaximumSize(QtCore.QSize(150, 25))
        self.hoursField.setStyleSheet("background-color: #c8daf2")
        self.hoursField.setObjectName("hoursField")
        self.durationGridLayout.addWidget(self.hoursField, 1, 0, 1, 1)
        
        # Hours Label -> Label
        self.hoursLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.hoursLabel.setStyleSheet("color:     #95bfe7")
        self.hoursLabel.setObjectName("hoursLabel")
        self.durationGridLayout.addWidget(self.hoursLabel, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        
        # Title Label: "Web Blocker" -> Label
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect((window_width / 2) - 120, (window_height / 2) - 270, 240, 50))
        self.titleLabel.setStyleSheet("color:     #95bfe7")
        self.titleLabel.setObjectName("titleLabel")
        
        # Save Button (change this to move the Save button) -> Button
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect((window_width / 2) - 55, (window_height / 2) + 140, 110, 31))
        self.saveButton.setStyleSheet("background-color: #173364; color:     #c8daf2")
        self.saveButton.setObjectName("saveButton")
        
        # Scroll Area for Sites (change this to move sites box) -> ScrollArea
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect((window_width / 2) - 288, (window_height / 2) - 200, 576, 200))  # size for scroll area
        self.scrollArea.setMaximumSize(QtCore.QSize(576, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 559, 136))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        # Grid Layout -> GridLayout
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")

        # Creates a check and delete button for every row
        try:
            if len(self.website_list) > 0:
                rows = 4
                for websiteToggle in self.website_list[1:]:
                    self.createSite(rows)
                    self.createCheckBoxButton(rows)
                    self.createDelButton(rows)
                    self.sites[self.siteIndex - 1].setPlainText(websiteToggle[0])
                    self.checkBox[self.cbIndex - 1].setChecked(websiteToggle[1].strip() == "True")
                    rows += 1
        except AttributeError:
            for i in range(4, 6):
                self.createSite(i)
                self.createCheckBoxButton(i)
                self.createDelButton(i)

        # Blocked -> Label
        self.blockedLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.blockedLabel.setStyleSheet("color:     #95bfe7")
        self.blockedLabel.setObjectName("blockedLabel")
        self.gridLayout.addWidget(self.blockedLabel, 2, 1, 1, 1)

        # Add New -> Button
        self.addNewButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.addNewButton.setStyleSheet("color:     #95bfe7")
        self.addNewButton.setObjectName("addNewButton")
        self.gridLayout.addWidget(self.addNewButton, 2, 2, 1, 1)
        
        # Block Sites -> Label
        self.blockedSitesLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.blockedSitesLabel.setStyleSheet("color:     #95bfe7")
        self.blockedSitesLabel.setObjectName("blockedSitesLabel")
        self.gridLayout.addWidget(self.blockedSitesLabel, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.saveButton.clicked.connect(self.switch_screens)
        self.saveButton.clicked.connect(MainWindow.hide)
    
    def retranslateUi(self, MainWindow):
        """ Formats elements in the MainWindow
        
        Args:
            MainWindow(QMainWindow): the main window
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.setDurationLabel.setText(_translate("MainWindow",
                                                 "<html><head/><body><p align=\"center\"><span style=\" "
                                                 "font-size:24pt;\">Set Duration</span></p></body></html>"))
        self.minutesField.setHtml(_translate("MainWindow",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                             "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta "
                                             "charset=\"utf-8\" /><style type=\"text/css\">\n "
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; "
                                             "font-size:13pt; font-weight:400; font-style:normal;\">\n "
                                             "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                             "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                             "-qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.minutesLabel.setText(_translate("MainWindow",
                                             "<html><head/><body><p align=\"center\"><span style=\" "
                                             "font-size:18pt;\">Minutes</span></p></body></html>"))
        self.hoursField.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                           "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta "
                                           "charset=\"utf-8\" /><style type=\"text/css\">\n "
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; "
                                           "font-size:15pt; font-weight:400; font-style:normal;\">\n "
                                           "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                           "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                           "text-indent:0px;\"><br /></p></body></html>"))
        self.hoursLabel.setText(_translate("MainWindow",
                                           "<html><head/><body><p align=\"center\"><span style=\" "
                                           "font-size:18pt;\">Hours</span></p></body></html>"))
        self.titleLabel.setText(_translate("MainWindow",
                                           "<html><head/><body><p align=\"center\"><span style=\" "
                                           "font-size:36pt;\">Web Blocker</span></p></body></html>"))
        self.saveButton.setText(_translate("MainWindow", "Save"))

        for button in self.deleteButton:
            button.setText(_translate("MainWindow", "Delete"))

        self.blockedLabel.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" "
                                             "font-size:18pt;\">Blocked</span></p></body></html>"))
        self.addNewButton.setText(_translate("MainWindow", "Add New"))
        self.blockedSitesLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" "
                                                                "font-size:18pt;\">Blocked "
                                                                "Sites</span></p></body></html>"))

    def connectActions(self):
        """ Connect click events in the MainWindow """
        # Save Button is Clicked
        self.saveButton.clicked.connect(self.saveClicked)

        # Add New Row is Clicked
        self.addNewButton.clicked.connect(self.newRow)

        # Delete Row is Clicked
        for button in self.deleteButton:
            if button.clicked:
                row = self.deleteButton.index(button)
                self.deleteButton[row].clicked.connect(self.deleteRow)

    def websiteBlocker(self, hostsPath, websiteList):
        """ This function blocks the websites with inputed hour
        and min. Once the new hour and min duration is over, the
        funcion blocks the websites

        Args:
            hostsPath(str): Directory to the hosts file
            websiteList(list): A list of blocked website url
            hour(int): How many hours are blocked
            mins(int): How many minutes are blocked
        """
        # Redirect to hosts file
        redirect = "127.0.0.1"

        # Then redirect the blocked websites
        try:
            with open(hostsPath, 'r+') as hostsfile:
                host_content = hostsfile.read()
                for site in websiteList:
                    if site not in host_content:
                        hostsfile.write(redirect + " " + site + "\n")
            print("Successfully Blocked")
        except FileNotFoundError:
            print("Error: hosts file not found")
    
    def saveClicked(self):
        """ Whenever save button is clicked, it reads text from the text box
        and stores them into 'data.csv' for use in the survey window. """
        # If both 'Hours' text field and 'Minutes' text field are filled
        if self.hoursField.toPlainText().strip() != "" and self.minutesField.toPlainText().strip() != "":
            self.duration_hour = self.hoursField.toPlainText().strip()
            self.duration_minute = self.minutesField.toPlainText().strip()
        # If only 'Hours' text field is filled
        elif self.hoursField.toPlainText().strip() != "" and self.minutesField.toPlainText().strip() == "":
            self.minute = 0
            self.duration_hour = self.hoursField.toPlainText().strip()
        # If only 'Minutes' text field is filled
        elif self.hoursField.toPlainText().strip() == "" and self.minutesField.toPlainText().strip() != "":
            self.duration_hour = 0
            self.minute = self.minutesField.toPlainText().strip()
        self.update_settingsList()
        site_list = self.site_list()
        self.surveyWindow.setHour(int(self.hour))
        self.surveyWindow.setMinute(int(self.minute))
        self.websiteBlocker(settings.hostPath, site_list)
        writeFile(self.settingsList, "data.csv")
        self.set_countdown_time()
        
    def update_settingsList(self):
        """ Updates the settingList, with time and non-empty sites """
        self.settingsList.append([self.hour, self.minute])
        # Checking if sites-box is not empty
        for i in range(len(self.sites)):
            link = str(self.sites[i].toPlainText())
            checked = self.checkBox[i].isChecked()
            if link != "":
                self.settingsList.append([link, checked])
    
    def site_list(self):
        """ Creates a list of websites as strings, which will be blocked
        
        Returns:
            websites(list): list of websites as strings, to be blocked
        """
        websites = []
        for i in range(1, len(self.settingsList)):
            sites = self.settingsList[i]
            if sites[1]:
                link = sites[0]
                websites.append(link)
        return websites
        
    def set_countdown_time(self):
        """ This Function stores the time for the survey-screen also accounts for empty hour/minute  """
        dur_hour = self.hoursField.toPlainText().strip()
        dur_min = self.minutesField.toPlainText().strip()
        if dur_hour == "":
            self.surveyWindow.duration_hour = 0
        else:
            self.surveyWindow.duration_hour = int(dur_hour)
        
        if dur_min == "":
            self.surveyWindow.duration_minute = 0
        else:
            self.surveyWindow.duration_minute = int(dur_min)
    
    def deleteRow(self):
        """ This function deletes a single row from the MainWindow """
        self.deleteButton.pop(0)
        self.gridLayout.itemAt(0).widget().deleteLater()
        self.gridLayout.itemAt(1).widget().deleteLater()
        self.gridLayout.itemAt(2).widget().deleteLater()

    def newRow(self):
        """ This function adds a single new row to the MainWindow """
        # Create Delete Button
        self.createDelButton(self.row)
        # Create CheckBox
        self.createCheckBoxButton(self.row)
        # Create Site
        self.createSite(self.row)
        self.row += 1

    def createSite(self, row):
        """ This function creates a new-site(text-box) to MainWindow
        
        Args:
            row(int): the index of the next row to be added
        """
        self.sites.append(QtWidgets.QTextEdit(self.scrollAreaWidgetContents))
        self.sites[self.siteIndex].setMinimumSize(QtCore.QSize(351, 31))
        self.sites[self.siteIndex].setMaximumSize(QtCore.QSize(351, 31))
        self.sites[self.siteIndex].setStyleSheet("background-color: #c8daf2")
        self.sites[self.siteIndex].setObjectName("site" + str(self.siteNum))
        self.gridLayout.addWidget(self.sites[self.siteIndex], row, 0, 1, 1)
        self.siteNum += 1
        self.siteIndex += 1
        self.row += 1

    def createCheckBoxButton(self, row):
        """ This function creates a new CheckBox to the MainWindow 
        
        Args:
            row(int): the index of the next row to be added
        """
        self.checkBox.append(QtWidgets.QCheckBox(self.scrollAreaWidgetContents))
        self.checkBox[self.cbIndex].setText("")
        self.checkBox[self.cbIndex].setStyleSheet("background-color: #173364")
        self.checkBox[self.cbIndex].setObjectName("checkBox1")
        self.gridLayout.addWidget(self.checkBox[self.cbIndex], row, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.checkBox[self.cbIndex].setChecked(True)
        self.cbIndex += 1
        self.cbNum += 1

    def createDelButton(self, row):
        """ This function creates a new Delete-Button to the MainWindow
        
        Args:
            row(int): the index of the next row to be added
        """
        _translate = QtCore.QCoreApplication.translate
        self.deleteButton.append(QtWidgets.QPushButton(self.scrollAreaWidgetContents))
        self.deleteButton[self.dbIndex].setStyleSheet("background-color: #173364; color: #c8daf2")
        self.deleteButton[self.dbIndex].setObjectName("deleteButton" + str(self.dbNum))
        self.deleteButton[self.dbIndex].setText(_translate("MainWindow", "Delete"))
        self.gridLayout.addWidget(self.deleteButton[self.dbIndex], row, 2, 1, 1)
        self.dbIndex += 1
        self.dbNum += 1
    
def readFile(fileName):
    """ This function reads the contents of the data.csv file
    
    Arguments:
        fileName(string): the name of the data file
    Returns:
        websites(list): the list of websites of format ['url'(str),'if checked'(str)]
    """
    websites = []
    try:
        websites_file = open(fileName, "r")
        for line in websites_file:
            line = line.split(",")
            settings = [line[0], line[1]]
            websites.append(settings)
        websites_file.close()
    except FileNotFoundError:
        pass
    return websites

def writeFile(settings, fileName):
    """ This function writes the contents into the data.csv file 
    
    Arguments:
        fileName(string): the name of the data file
    """
    output = open(fileName, "w")
    for setting in settings:
        output.write(str(setting[0]) + "," + str(setting[1]) + "\n")
    output.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    surveyWindow = Ui_MainWindow()
    surveyWindow.setupUi(MainWindow)
    surveyWindow.connectActions()
    MainWindow.show()
    sys.exit(app.exec_())
