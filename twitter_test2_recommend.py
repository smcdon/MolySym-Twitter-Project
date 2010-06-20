import sys, urllib, httplib2
from PyQt4 import QtCore, QtGui
from twitter_client import Ui_twitter_client
from test_request import RecommendedUsers

class Twitter(QtGui.QMainWindow):
    def __init__(self, parent=None):
        # Initialise GUI
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_twitter_client()
        self.ui.setupUi(self)

        # define character limits/status and login info
        self.max = 140
        self.uid = 's_mcdon'
        self.pwd = 'Twitt3rAnon'
        self.updateLabel()

        # set up signals and slots
        QtCore.QObject.connect(self.ui.button_post, QtCore.SIGNAL("clicked()"), self.postTweet)
        QtCore.QObject.connect(self.ui.textEdit, QtCore.SIGNAL("textChanged()"), self.updateLabel)
        QtCore.QObject.connect(self.ui.users_rec, QtCore.SIGNAL("selectionChanged()"), self.rec_user_list)

        # define posting URLs          
        self.twitUpdate = 'http://twitter.com/statuses/update.xml'
        self.twitCloser = 'http://twitter.com/account/end_session'

        # instantiate a class with methods for getting recommended users
        self.rec = RecommendedUsers(self.uid, self.pwd)
        
        

    def postTweet(self):
        # convert text in GUI text box to plain text
        mesg = self.ui.textEdit.toPlainText()
        # convert text into a url-encoded string so it can be used as a POST request
        post = urllib.urlencode({ 'status' : mesg })

        try:
            http = httplib2.Http()

            # override the default (no exceptions, status in response)
            http.force_exception_to_status_code = False

            # provide a name and password for authentication
            http.add_credentials(self.uid, self.pwd)

            # post status update to Twitter page
            (resp, content) = http.request(self.twitUpdate, 'POST', post)

            # if successful, say so
            if resp and resp.status == 200:
                self.ui.status.setText('Twitter updated!')
            # if not, say so
            else:
                raise httplib2.HttpLib2Error, 'No response'
        except httplib2.HttpLib2Error, ex:
            print ex
            self.ui.status.setText(ex.__str__())

        # end Twitter session
        http.request(self.twitCloser)

    # show how many characters are left
    def updateLabel(self):
        len = self.ui.textEdit.toPlainText().size()
        self.ui.status.setText('%d char(s) remaining' % (self.max-len))
        self.ui.button_post.setEnabled(len <= self.max)

    # display list of recommended users when text box is clicked
    def rec_user_list(self):
        self.rec.getRecommendedUsers()
        for names in self.rec.names:
            self.ui.users_rec.append(names)
    
# Start Application
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = Twitter()
	myapp.show()
	sys.exit(app.exec_())

