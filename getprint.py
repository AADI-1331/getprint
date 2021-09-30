# Hints:
#Use __init__ method to construct some parameters


class InputOutString(object):
    def __init__(self,word):
        self.word = ""

    def getString(self):
        self.word = raw_input()

    def printString(self):
        print self.word.upper()

strObj = InputOutString()
strObj.getString()
strObj.printString()
