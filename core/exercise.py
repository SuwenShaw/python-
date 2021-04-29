import math


# python 命名规则

# 1. 模块命名
#   模块推荐使用小写命名，
#   除非有很多字母，尽量不要用下划线

# 2. 类命名
#   类名使用驼峰(CamelCase)命名风格，首字母大写
#   私有类可用一个下划线开头

# 3. 函数命名
#   函数名一律小写，如有多个单词，用下划线隔开
#   类内部函数命名，用单下划线(_)开头（该函数可被继承访问）
#   类内私有函数命名，用双下划线(__)开头（该函数不可被继承访问）

# 4. 变量命令
#   变量名推荐小写，如有多个单词，用下划线隔开
#   类内部变量命名，用单下划线(_)开头（该变量可被继承访问）
#   类内私有变量命名，用双下划线(__)开头（该变量不可被继承访问）

# 5. 常量命令
#   使用下划线分割大些字母命名

# date: 20210428
# 1. 请设计一个函数，函数的输入是数字，打印这个数是奇数还是偶数


def judge(num: int):
    print(str(num) + "是奇数") if num % 2 == 0 else print(str(num) + "是偶数")


# 2. 请设计一个函数，输入是半径，返回值是对应圆的面积


def circle_area(radius: int):
    return radius * radius * math.pi


# 3. 给到一个列表，请计算列表中所有元素之和

def list_sum(source):
    result = 0
    for num in source:
        result += num
    return result


# 4. 给到一个列表，请计算出列表中所有偶数之和

def list_even_sum(source):
    result = 0
    for num in source:
        if num % 2 == 0:
            result += num
    return result


# 5. 给到一个列表，请计算出列表中所有素数之和

# 判断数字是否为素数,设计为一个函数是因为下面还要使用
def judge_prime(num):
    if num <= 1:
        return False
    half_num = num // 2
    for i in range(2, half_num + 1):
        if num % i == 0:
            return False
    return True


def list_prime_sum(source):
    result = 0
    for num in source:
        if judge_prime(num):
            result += num
    return result


# 6. 将 3，4，5 封装成函数，函数的输入是列表，函数的返回值为对应的和
# 7. 请打印出 1-100 之间所有的素数


# 8. 请设计一个函数，打印指定范围的素数
def print_prime(start, end):
    for i in range(start, end):
        if judge_prime(i):
            print(i)


# 9. 请设计一个函数，输入是一个范围，返回时这个范围内的所有素数
def get_prime(start, end):
    result = []
    for i in range(start, end):
        if judge_prime(i):
            result.append(i)

