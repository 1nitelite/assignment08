"""
title: can_05.py
desc: canonastring - demonstrator class
change log: (who, when, what)
ntoulas, 2022-Jun-19, created file
"""

class CanOnAString():
    def __init__(self, msg):
        self._message = msg

    @property
    def message(self):
        return self._message.title()

    @message.setter
    def message(self, value):
        if str(value).isnumeric():
            raise Exception('The message can\'t be cryptic')
        else:
            self._message = value

objCan1 = CanOnAString('There is no spoon')
print('original message: {}'.format(objCan1.message))
objCan1.message = 'Live long and prosper'
print('updated message: {}'.format(objCan1.message))

print('Now lets check the exception: ')
try:
    objCan1.message = 123456
except Exception as e:
    print(e)

print('now lets test direct access')
try:
    print('secret',objCan1._message)
except Exception as e:
    print(e, e.__doc__, sep='\n\n')

print('now lets try assigning to the hidden attribute directly')
objCan1._message = 'Sometimes your whole life boils down to one insane move'
print('should not be done, but python ignores it without throwing an exception')
print('last message: {}'.format(objCan1.message))
try:
    print(objCan1._message)
except Exception as e:
    print(e, e.__doc__, sep= '\n\n')