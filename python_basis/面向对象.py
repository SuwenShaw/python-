# 面向对象是根据职责确定不同的对象，在对象内部封装不同的方法
# 类是模板，对象是根据类创建出来的，对象可以有多个

# 类的三要素：类名、属性（特征）、方法（行为）

# 类的命名遵循大驼峰命名法
# 每一个单词的首字母大写
# 单词与单词之间没有下划线

# 由哪一个对象调用的方法，方法内的self就是哪一个对象的引用

# 初始化方法内部定义属性，同时可以设置初始值
# __int__专门用来定义一个类具有哪些属性
# 在 __init__ 方法内部使用 self.属性名 = 属性的初始值 就可以定义属性


class Cat:

    def __init__(self, name):
        # 设置初始值
        print("这是一个初始化方法")

        # 在方法内部使用 self.属性 = 形参 接收外部传递的参数
        self.name = name

    def eat(self):
        print("%s 爱吃鱼" % self.name)


# 使用类名()创建对象的时候，会自动调用初始化方法 __init__
tom = Cat('Tom')
tom.eat()

lazy_cat = Cat("大懒猫")
lazy_cat.eat()

# __del__ 方法:对象被从内存中销毁前，会被自动调用
# 如果希望在对象被销毁前，再做一些事情，可以考虑一下 __del__ 方法
# 一个对象的 __del__ 方法一旦被调用，生命周期结束


class Cat:

    def __init__(self, new_name):

        self.name = new_name

        print("%s 来了" % self.name)

    def __del__(self):

        print("%s 走了" % self.name)


# tom 是一个全局变量
tom = Cat("Tom")
print(tom.name)

# del 关键字可以删除一个对象
del tom

print("-" * 50)

# __str__方法:返回对象的描述信息，print 函数输出使用，必须返回一个字符串
# 在Python中，使用print输出对象变量，默认情况下，会输出这个变量引用的对象，是由哪一个类创建的对象，以及在内存中的地址（十六进制表示）


class Cat:

    def __init__(self, new_name):

        self.name = new_name

        print("%s 来了" % self.name)


tom = Cat("Tom")
print(tom)

# 如果在开发中，希望使用print输出对象变量时，能够打印自定义的内容，就可以利用 __str__ 这个内置方法了


class Cat:

    def __init__(self, new_name):

        self.name = new_name

        print("%s 来了" % self.name)

    def __str__(self):
        return "我是小猫：%s" % self.name


tom = Cat("Tom")
print(tom)

# 摆放家具
# 需求
# 房子(House) 有 户型、总面积 和 家具名称列表
# 新房子没有任何的家具
# 家具(HouseItem) 有 名字 和 占地面积，其中
# 席梦思(bed) 占地 4 平米
# 衣柜(chest) 占地 2 平米
# 餐桌(table) 占地 1.5 平米
# 将以上三件 家具 添加 到 房子 中
# 打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表


class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s占地%d平米" % (self.name, self.area)


# 创建家具
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

print(bed)
print(chest)
print(table)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area

        # 剩余面积初始值默认和总面积一致
        self.free_area = area
        # 新房默认没有任何的家具
        self.item_list = []

    def __str__(self):
        # Python 能够自动的将一对括号内部的代码连接在一起
        return ("户型：%s\n总面积：%.2f[剩余面积：%.2f]\n家具：%s"
                % (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):
        print("要添加%s" % item)
        # 1. 判断家具面积是否大于剩余面积
        if item.area > self.free_area:
            # print("%s面积过大，不能添加到房子中" % item.name)
            print("{}面积过大，不能添加到房子中".format(item.name))

        # 2. 将家具的名称追加到名称列表中
        self.item_list.append(item.name)

        # 3. 计算剩余面积
        self.free_area -= item.area


# 创建房子对象
my_home = House("两室一厅", 60)

my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)

# 一个对象的 属性 可以是 另外一个类创建的对象
# 士兵突击
# 需求
# 士兵 许三多 有一把 AK47
# 士兵 可以 开火
# 枪 能够 发射 子弹
# 枪 装填 装填子弹 —— 增加子弹数量


class Gun:
    def __init__(self, model):
        self.model = model

        # 初始子弹数为0
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 判断是否还有子弹，没有子弹return结束
        if self.bullet_count == 0:
            print("没有子弹了")
            return

        # 发射一颗子弹
        self.bullet_count -= 1
        print("{0}发射一颗子弹【子弹剩余{1}】".format(self.model, self.bullet_count))


# 创建枪对象
ak47 = Gun("AK47")
# ak47.add_bullet(50)
# ak47.shoot()


class Soldier:
    def __init__(self, name):
        self.name = name
        # 士兵初始没有枪 None 关键字表示什么都没有
        self.gun = None

    def fire(self):
        # 1. 判断士兵是否有枪
        if self.gun is None:
            print("{}还没有枪".format(self.name))
        # 2. 让枪装填子弹
        self.gun.add_bullet(50)
        # 3. 让枪发射子弹
        self.gun.shoot()


xusanduo = Soldier("许三多")
xusanduo.gun = ak47
xusanduo.fire()

# 私有属性和私有方法
# 对象的某些属性或方法可能只希望在对象的内部被使用，而不希望在外部被访问到

# 面向对象三大特性
# 封装：根据 职责 将 属性 和 方法 封装 到一个抽象的 类 中
# 继承：实现代码的重用，相同的代码不需要重复的编写
# 多态：不同的对象调用相同的方法，产生不同的执行结果，增加代码的灵活度

# 单继承
# 覆盖
# 如果在开发中，父类的方法实现 和 子类的方法实现，完全不同，就可以使用 覆盖 的方式
# 具体的实现方式，就相当于在 子类中 定义了一个 和父类同名的方法并且实现

# 扩展
# 如果在开发中，子类的方法实现中包含 父类的方法实现，就可以使用 扩展 的方式，在子类中 重写 父类的方法
# 在需要的位置使用 super().父类方法 来调用父类方法的执行，代码其他的位置针对子类的需求，编写 子类特有的代码实现

# 多继承（如果 父类之间 存在 同名的属性或者方法，应该 尽量避免 使用多继承）


class A:
    pass


class B:
    pass


class C(A, B):
    pass


# __mro__（方法搜索顺序）主要用于 在多继承时判断 方法、属性 的调用 路径
print(C.__mro__)

# 多态
# 以 继承 和 重写父类方法 为前提，不同的 子类对象 调用相同的 父类方法，产生不同的执行结果


class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍..." % self.name)


class XiaoTianDog(Dog):

    def game(self):
        print("%s 飞到天上去玩耍..." % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍..." % (self.name, dog.name))

        # 让狗玩耍
        dog.game()


# 1. 创建一个狗对象
# wangcai = Dog("旺财")
wangcai = XiaoTianDog("飞天旺财")

# 2. 创建一个小明对象
xiaoming = Person("小明")

# 3. 让小明调用和狗玩的方法
xiaoming.game_with_dog(wangcai)

# 创建出来的 对象 叫做 类 的 实例
# 创建对象的 动作 叫做 实例化
# 对象的属性 叫做 实例属性
# 对象调用的方法 叫做 实例方法

# 类属性


class Tool(object):

    # 使用赋值语句，定义类属性，记录创建工具对象的总数
    count = 0

    def __init__(self, name):
        self.name = name

        # 针对类属性做一个计数+1
        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("铁锹")

# 知道使用 Tool 类到底创建了多少个对象?
print("现在创建了 %d 个工具" % Tool.count)

# 类方法
# 定义一个 工具类
# 每件工具都有自己的 name
# 需求：在 类 封装一个 show_tool_count 的类方法，输出使用当前这个类，创建的对象个数


class Tool(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    @classmethod
    def show_tool_count(cls):
        print("工具对象的总数:{}".format(cls.count))


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("铁锹")

# 知道使用 Tool 类到底创建了多少个对象?
Tool.show_tool_count()

# 静态方法
# 既 不需要 访问 实例属性 或者调用 实例方法
# 也 不需要 访问 类属性 或者调用 类方法
# @staticmethod
# def 静态方法名():
#     pass


# 方法综合案例
# 需求
#
# 设计一个 Game 类
# 属性：
# 定义一个 类属性 top_score 记录游戏的 历史最高分
# 定义一个 实例属性 player_name 记录 当前游戏的玩家姓名
# 方法：
# 静态方法 show_help 显示游戏帮助信息
# 类方法 show_top_score 显示历史最高分
# 实例方法 start_game 开始当前玩家的游戏
# 主程序步骤
# 1) 查看帮助信息
# 2) 查看历史最高分
# 3) 创建游戏对象，开始游戏


class Game(object):
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息...")

    @classmethod
    def show_top_score(cls):
        print("游戏最高分：{}".format(cls.top_score))

    def start_game(self):
        print("玩家{}开始游戏".format(self.player_name))

        Game.top_score = 999


# 1. 查看游戏帮助
Game.show_help()

# 2. 查看游戏最高分
Game.show_top_score()

# 3. 创建游戏对象，开始游戏
game = Game("小明")

game.start_game()

# 4. 游戏结束，查看游戏最高分
Game.show_top_score()

#