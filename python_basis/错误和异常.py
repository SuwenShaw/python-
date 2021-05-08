# https://www.runoob.com/python3/python3-errors-execptions.html
# 异常处理
# try/except
# try:
#     执行代码
# except:
#     发生异常时执行的代码
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())  # strip()用于移除字符串头尾指定的字符（默认为空格）
except OSError as err:  # 操作系统错误
    print("OS error:{0}".format(err))
except ValueError:  # 传入无效的参数
    print("Could not convert data to an integer.")
except:  # 最后一个except子句可以忽略异常的名称，它将被当作通配符使用
    print("Unexpected error:", sys.exc_info()[0])  # 使用 sys 模块中的 exc_info() 方法获得更多的异常信息
    # exc_info()方法会将当前的异常信息以元组的形式返回，该元组中包含3个元素，分别为type、value和traceback
    raise  # 单独一个raise引发当前上下文中捕获的异常（比如在except块中），或默认引发 RuntimeError 异常

# try/except...else
# try:
#     执行代码
# except:
#     发生异常时执行的代码
# else:
#     没有异常时执行的代码
# 在try语句中判断文件是否可以打开，如果打开文件时没有发生异常则执行else部分的语句，读取文件内容：
for arg in sys.argv[1:]:
    # sys.argv[]其实就是一个列表，里边的项为用户输入的参数，这参数是从程序外部输入的
    # 其第一个元素即sys.argv[0]是程序本身，随后才依次是外部给予的参数
    try:
        f = open(arg, 'r')
    except IOError:  # 输入/输出操作失败
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

# 异常处理并不仅仅处理那些直接发生在try子句中的异常，而且还能处理子句中调用的函数（甚至间接调用的函数）里抛出的异常


def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:  # 除(或取模)零 (所有数据类型)int division or modulo by zero
    print('Handling run-time error:', err)

# try-finally 语句
# try:
#     执行代码
# except:
#     发生异常时执行的代码
# else:
#     没有异常时执行的代码
# finally:
#     不管有没有异常都会执行的代码
try:
    runoob()  # name 'runoob' is not defined
except AssertionError as error:  # 断言语句失败
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('这句话，无论异常是否发生都会执行。')

# 触发异常
# raise：单独一个 raise。该语句引发当前上下文中捕获的异常（比如在 except 块中），或默认引发 RuntimeError 异常。
# raise 异常类名称：raise 后带一个异常类名称，表示引发执行类型的异常。
# raise 异常类名称(描述信息)：在引发指定类型的异常的同时，附带异常的描述信息。
x = 10
if x > 5:
    raise Exception('x 不能大于5。x的值为:{}'.format(x))
# 输出结果：Exception: x 不能大于 5。x 的值为: 10

try:
    a = input("输入一个数：")
    if not a.isdigit():
        raise ValueError("a 必须是数字")
except ValueError as e:
    print("引发异常：", repr(e))
    raise

# 用户自定义异常


class MyError(Exception):
    def __init__(self, value):  # 在创建完对象之后会自动调用, 它完成对象的初始化的功能
        self.value = value

    def __str__(self):  # 返回一个对象的描述信息
        return repr(self.value)


try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)

# 定义清理行为


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


divide(2, 1)
divide(2, 0)
divide('2', '1')
# 如果一个异常在try子句里（或者在except和else子句里）被抛出，而又没有任何的except把它截住，那么这个异常会在finally子句执行后被抛出

# 预定义的清理行为
# 一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行
for line in open("myfile.txt"):
    print(line, end="")
# 当执行完毕后，文件会保持打开状态，并没有被关闭

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
# 以上这段代码执行完毕后，就算在处理过程中出问题了，文件f总是会关闭

# 异常链
