"""
Title: lab08_d.py
Desc: Lab D - Working with classes
Change Log: (Who, When, What)
NToulas, 2022-Jun-14, Created file
"""

class TrackInfo:
    """
        Tracks CD info
    """

    # -- Fields -- #
    position = 0
    title = ''
    length = ''

    # -- Constructor -- #
    def __init__(self, pos, name, num):
        # -- Attributes -- #
        self.position = pos
        self.title = name
        self.length = num

    # -- Properties -- #
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if str(value).isalpha():
            raise Exception('The position can\'t be alphabetic')
        else:
            self.__position = value

    @property
    def title(self):
        return self.__message.title()

    @title.setter
    def title(self, value):
        if str(value).isnumeric():
            raise Exception('The title can\'t be numeric')
        else:
            self.__message = value

    @property
    def length(self):
        return self.__length.title()

    @length.setter
    def length(self, value):
        if str(value).isnumeric():
            raise Exception('The length can\'t be numeric')
        else:
            self.__length = value

    # -- Methods -- #

try:
    cd_info = TrackInfo('1234', 1234, 5)
except Exception as e:
    print(e)
