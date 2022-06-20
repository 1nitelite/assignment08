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

    # -- Constructor -- #
    def __init__(self, pos, name, num):
        # -- Attributes -- #
        self._position = pos
        self._message = name
        self._length = num

    # -- Properties -- #
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if str(value).isalpha():
            raise Exception('The position can\'t be alphabetic')
        else:
            self._position = value

    @property
    def message(self):
        return self._message.title()

    @message.setter
    def message(self, value):
        if str(value).isnumeric():
            raise Exception('The title can\'t be numeric')
        else:
            self._message = value

    @property
    def length(self):
        return self._length.title()

    @length.setter
    def length(self, value):
        if str(value).isnumeric():
            raise Exception('The length can\'t be numeric')
        else:
            self._length = value

    # -- Methods -- #
    def __str__(self):
        return f'{self._position}, {self._message}, {self._length}'

cd_info = TrackInfo(345, 'title', 'name')

print(cd_info)
