# 动物类
class Animal:

    # 初始化方法，在实例化的时候会调用该方法
    def __init__(self, name, color, category):
        self.name = name
        self.__color = color
        self.__category = category

    def eat(self):
        print("A {0} is eating".format(self.__category))


# 鸟类(继承动物类，拥有动物的属性和行为)
class Bird(Animal):

    def __init__(self, name, color):
        Animal.__init__(self, name, color, "Bird")

    # 唱歌
    def sing(self):
        print("A {0} is singing".format(self.name))

    # 飞行
    def fly(self):
        print("A {0} who's color is {1} is flying".format(self.name, self.__color))


bird = Bird("Json", "white")
bird.eat()
