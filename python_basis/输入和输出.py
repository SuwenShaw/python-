# https://www.runoob.com/python3/python3-inputoutput.html
# 输出格式美化
# 如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现
# str()： 函数返回一个用户易读的表达形式
# repr()： 产生一个解释器易读的表达形式
# 输出一个平方与立方的表
for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3), end=' ')  # rjust() 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
    print(repr(x*x*x).rjust(4))

for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3), repr(x*x*x).rjust(4))

for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# 如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值


# 读和写文件
# 打开一个文件
f = open("/tmp/foo.txt", "w")
f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")  # 写
f.flush()  # 刷新，将缓冲区的内容写入文件
string = f.read()  # 读
print(string)

# 关闭打开的文件
f.close()

# f.readline()从文件中读取单独的一行，包含换行符'\n'
# f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行
with open("/Users/xiaoshuwen/Desktop/Python Doc/测试/city.txt", "r") as file:
    while True:
        str = file.readline()
        if str == "":
            break
        print(str)

# f.readlines()返回该文件中包含的所有行
