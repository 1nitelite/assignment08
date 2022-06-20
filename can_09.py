"""
Title: can_07.py
Desc: Can on a string - demo class 7
Change Log: (Who, When, What)
DBiesinger, 2030-Jan-01, created file
NToulas, 2022-Jun-19, Modified file
"""

class CanOnAString():

    # -- Fields -- #
    _numCans = 0
    # -- Constructor -- #
    def __init__(self, msg):
        # -- Attributes -- #
        self._message = msg
        CanOnAString._incrementCount()

    # -- Properties -- #
    @property
    def message(self):
        return self._message.title()

    @message.setter
    def message(self, value):
        if str(value).isnumeric():
            raise Exception('The message can\'t be cryptic')
        else:
            self._message = value

    # -- Methods -- #
    @staticmethod
    def connected():
        return '\nThere are {} cans connected to the string.'.format(CanOnAString._numCans)

    @staticmethod
    def _incrementCount():
        CanOnAString._numCans += 1

    def noAnswer(self):
        return 'I know Kung Fu'

    def __str__(self):
        return self.noAnswer()

print('Connecting some cans')
objCan1 = CanOnAString('There is no spoon')
objCan2 = CanOnAString('Live long and prosper')
objCan3 = CanOnAString('Sometimes your whole life boils down to one insane move')

print(CanOnAString.connected())