# 数据结构
# 用列表实现堆栈（后进先出）
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.pop()
stack.pop()
print(stack)

# 用列表实现队列（先进先出）
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
queue.popleft()
print(queue)

# 创建平方值的列表
squares = []
for x in range(10):
    squares.append(x ** 2)

print(squares)

squares = list(map(lambda x: x ** 2, range(10)))
print(squares)

squares = [x ** 2 for x in range(10)]
print(squares)

# 列表推导式
print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))

print(combs)

# 列表详解
vec = [-4, -2, 0, 2, 4]
# 两倍vec
print([x * 2 for x in vec])
# 去掉负数
print([x for x in vec if x >= 0])
# 取绝对值
print([abs(x) for x in vec])
# 去掉空字符
freshfruit = ['    banana', '    loganberry   ', '  passion fruit   ']
print([weapon.strip() for weapon in freshfruit])
# 创建一个列表,类似于(number,square)
print([(x, x ** 2) for x in range(6)])
# 用两个for把列表展开
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])
# pi取小数点后几位,并改成字符型格式
from math import pi

print([round(pi, i) for i in range(1, 6)])
print([str(round(pi, i)) for i in range(1, 6)])
# 矩阵行列转置
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print([[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

print(list(zip(matrix)))
print(list(zip(*matrix)))

# 元组
t = 12345, 54321, 'hello!'
print(t)
t = (12345, 54321, 'hello!')
print(t)
print(t[0])
# 元组可以嵌套,不能更改
u = t, (1, 2, 3, 4, 5)
print(u)
# 0个元素的元组
empty = ()
print(len(empty))
# 1个元素的元组
singleton = 'hello',
print(len(singleton))
print(singleton)

# 集合
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('crabgrass' in basket)

# 集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
# a有b没有,即a-ab
print(a - b)
# 并集
print(a | b)
# 交集
print(a & b)
# a和b独有的元素,即a+b-ab
print(a ^ b)

# 集合推导式
a = {x for x in 'abracadabra' if x in 'abc'}
print(a)
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

# 字典
tel = {'jack': 4098, 'sape': 4139}
print(tel)
print(tel['jack'])
# 增加
tel['guido'] = 4127
print(tel)
tel['irv'] = 4127
print(tel)
# 删除
del tel['sape']
print(tel)
# 键列表
print(list(tel))
# 排序,按插入顺序排列
sorted(tel)
# 检查键是否存在
print('guido' in tel)
print('guido' not in tel)
# 创建字典
print(dict((('sape', 4139), ('guido', 4127), ('jack', 4098))))
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

print(dict(sape=4139, guido=4127, jack=4098))
print(dict(sape=4139, guido=4127, jack=4098))
# 字典推导式
print({x: x ** 2 for x in (2, 4, 6)})

# 循环的技巧
# 字典 items()返回键与值
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
# 序列 enumerate()返回索引与值
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i,v)
# 多个序列 zip()匹配元素
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))
# 逆向循环 reversed()
for i in range(1, 10, 2):
    print(i)
for i in reversed(range(1, 10, 2)):
    print(i)
# 指定顺序循环 sorted()
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
# 序列去重
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(set(basket)):
    print(i)
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in set(sorted(basket)):  # 结果不一样，排序错误
    print(i)
# 创建新列表
import math
raw_data = [56.2, float('NaN'), 51.7, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)
# 深入条件控制
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)
string1, string2, string3 = '', 'Hammer Dance', 'Trondheim'
non_null = string1 or string2 or string3
print(non_null)
# 序列与其他类型的比较
print((1, 2, 3)<(1, 2, 4))
print([1, 2, 3]<[1, 2, 4])
print('ABC'<'C'<'Pascal'<'Python')
print((1, 2, 3, 4)<(1, 2, 4))
print((1, 2)<(1, 2, -1))
print((1, 2, 3)==(1.0, 2.00, 3.000))
print((1, 2, ('aa', 'ab'))<(1, 2,('abc', 'a'), 4))