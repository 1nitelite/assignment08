class Point:
    x = 0
    y = 0

    # this is what python does on its own
    # def __int__(self, inputX, inputY):
    #     self.x = 0
    #     self.y = 0

    # two underscores prefix and suffix is for python special construct aka dunder aka special method
    # self is an instance of this object
    def __init__(self, inputX, inputY):
        self.x = inputX
        self.y = inputY

if __name__ == '__main__':
    p0 = Point(0, 0)
    print(p0.x)
    print(p0.y)

    # () means to call a method, called Point aka initializer
    # p0 = Point()
    # p0.x = 123
    # p0.y = 87654
    # p1 = Point()
    # p1.x = -123
    # p1.y = -5748
    # print(p1.x)
    # print(p1.y)
    # print(p0.x)
    # print(p0.y)
    #
    # print(id(p0))
    # print(id(p1))
