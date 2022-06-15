"""
Title: lab08_c.py
Desc: Lab C - Working with classes
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
    # -- Methods -- #

cd_info = TrackInfo(1234, 'title', 'five')

print('position: {}'.format(TrackInfo.position))
print('title: {}'.format(TrackInfo.title))
print('length: {}'.format(TrackInfo.length))

print('position: {}'.format(cd_info.position))
print('title: {}'.format(cd_info.title))
print('length: {}'.format(cd_info.length))
