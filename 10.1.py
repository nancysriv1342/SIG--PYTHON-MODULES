class Cir():
    def __init__(self, r):
        self.radius = r

    def getArea(self):
        return self.radius ** 2 * 3.14

    def GETCIRCUMFERENCE(self):
        return 2 * self.radius * 3.14


NewCir = Cir(5)
print(NewCir.getArea())
print(NewCir.GETCIRCUMFERENCE())