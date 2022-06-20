"""
Title: can_07.py
Desc: Can on a string - demo class 7
Change Log: (Who, When, What)
DBiesinger, 2030-Jan-01, created file
NToulas, 2022-Jun-19, Modified file
"""

class DemoCan():
    pass

class CanOnAString():

    # -- Fields -- #
    # -- Constructor -- #
    def __init__(self, msg):
        # -- Attributes -- #
        self.__message = msg

    # -- Properties -- #
    @property
    def message(self):
        return self.__message.title()

    @message.setter
    def message(self, value):
        if str(value).isnumeric():
            raise Exception('The message can\'t be cryptic')
        else:
            self.__message = value

    # -- Methods -- #
    def noAnswer(self):
        return 'I know Kung Fu'

    def __str__(self):
        return self.noAnswer()

objCan1 = CanOnAString('There is no spoon')
objCan2 = DemoCan()

print(CanOnAString())
print('#2',objCan2)
r = CanOnAString(123)
s = str(objCan1)
print(s)
print('r',r)
print(objCan1)
print(objCan1.__str__())