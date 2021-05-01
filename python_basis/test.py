from math import pi
import collections

# 打印九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(j, '*', i, '=', i*j, end='  ')
    else:
        print(' ')


# 两数之和
nums = [2, 7, 11, 15]
target = 9
for i in range(0, len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])

nums = [2, 7, 3, 6]
target = 9
result = []
for i in range(0, len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            result.append([i, j])
            continue
print(result)

# 20210428
# 1. 请设计一个函数，函数的输入是数字，打印这个数是奇数还是偶数


def odd_or_even(number):
    if number % 2 == 0:
        return '偶数'
    else:
        return '奇数'


print(odd_or_even(5))

# 2. 请设计一个函数，输入是半径，返回值是对应圆的面积


def area_circle(r):
    return pi * (r ** 2)


print(area_circle(2))

# 3. 给到一个列表，请计算列表中所有元素之和
nums = [1, 4, 6, 9, 3.5]
sum = 0
for i in range(0, len(nums)):
    sum = sum + nums[i]

print(sum)

# 4. 给到一个列表，请计算出列表中所有偶数之和
nums = [1, 4, 6, 9, 3.5]
sum_even = 0
for i in range(0, len(nums)):
    if nums[i] % 2 == 0:
        sum_even = sum_even + nums[i]

print(sum_even)

# 5. 给到一个列表，请计算出列表中所有素数之和
nums = [1, 2, 11, 101, 4, 6, 9]
sum_prime = 0
for i in range(0, len(nums)):
    if nums[i] == 1:
        continue
    for j in range(2, nums[i]):
        if nums[i] % j == 0:
            break
    else:
        sum_prime = sum_prime + nums[i]

print(sum_prime)

# 6. 将 3，4，5 封装成函数，函数的输入是列表，函数的返回值为对应的和
nums = [1, 2, 11, 101, 4, 6, 9]


def sum(nums):
    sum = 0
    for i in range(0, len(nums)):
        sum = sum + nums[i]
    if i == len(nums) - 1:
        return sum


print(sum(nums))


def sum(nums):
    sum = 0
    for i in range(0, len(nums)):
        sum = sum + nums[i]
        if i == len(nums) - 1:
            return sum


print(sum(nums))


def sum_even(nums):
    sum_even = 0
    for i in range(0, len(nums)):
        if nums[i] % 2 == 0:
            sum_even = sum_even + nums[i]
    if i == len(nums) - 1:
        return sum_even


print(sum_even(nums))


def sum_prime(nums):
    sum_prime = 0
    for i in range(0, len(nums)):
        if nums[i] == 1:
            continue
        for j in range(2, nums[i]):
            if nums[i] % j == 0:
                break
        else:
            sum_prime = sum_prime + nums[i]
    if i == len(nums) - 1:
        return sum_prime


print(sum_prime(nums))

# 7. 请打印出 1-100 之间所有的素数
for i in range(1, 101):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)

for i in range(1, 101):
    if i == 1:
        continue
    for j in range(2, i//2+1):
        if i % j == 0:
            break
    else:
        print(i)

# 8. 打印指定范围的素数
a = 9
b = 50
for i in range(a, b):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)

# 9. 请设计一个函数，输入是一个范围，返回这个范围内的所有素数


def range_prime(a, b):
    nums = []
    for i in range(a, b+1):
        if i == 1:
            continue
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            nums.append(i)
        if i == b:
            return nums


a = 9
b = 50
print(range_prime(a, b))

# 20210430
# 1. 请使用冒泡排序对列表中的元素进行排序
list1 = [22, 85, 19, 98, 8, 24, 5, 23, 3, 11, 2]
for i in range(len(list1) - 1):  # 设置冒泡排序次数
    for j in range(0, len(list1) - i - 1):  # 设置每一次冒泡排序需要的排序次数
        if list1[j] > list1[j + 1]:
            list1[j], list1[j + 1] = list1[j + 1], list1[j]  # 将较小的数排在前面

print(list1)

# 2. 请使用选择排序对列表中的元素进行排序
# 每一次遍历的时候，一选到小的就交换，直到遍历结束i位置上就是所有的最小值
list1 = [22, 85, 19, 98, 8, 24, 5, 23, 3, 11, 2]
for i in range(0, len(list1)):  # 设置选择排序次数
    for j in range(i + 1, len(list1)):  # i之后的所有数与i比较大小
        min_index = i  # 迭代得出最小值的索引(j每增加一次就在与前面的最小值对比)
        if list1[j] < list1[min_index]:
            min_index = j
        list1[i], list1[min_index] = list1[min_index], list1[i]  # 每比较一次就将最小值放在i位置上

print(list1)

list1 = [22, 85, 19, 98, 8, 24, 5, 23, 3, 11, 2]
for i in range(0, len(list1)):  # 设置选择排序次数
    for j in range(i + 1, len(list1)):  # i之后的所有数与i比较大小
        if list1[j] < list1[i]:
            list1[i], list1[j] = list1[j], list1[i]  # 每比较一次就将最小值放在i位置上

print(list1)

# 每一次遍历后选出最小值与i交换位置
list1 = [22, 85, 19, 98, 8, 24, 5, 23, 3, 11, 2]
for i in range(0, len(list1)):  # 设置选择排序次数
    min_index = i
    for j in range(i + 1, len(list1)):  # i之后的所有数与i比较大小
        if list1[j] < list1[min_index]:
            min_index = j
    list1[i], list1[min_index] = list1[min_index], list1[i]

print(list1)


# 20210501
# 1.请设计一个函数，查找列表中的最小的元素
def min_factor(l):
    for i in range(1, len(l)):
        if l[i] < l[0]:
            l[0], l[i] = l[i], l[0]
    return l[0]


list1 = [22, 85, 19, 98, 8, 24, 5, 23, 3, 11, 2]
print(min_factor(list1))


# 2.现在有一个字典，key的类型为字符串，value类型为int，请设计一个函数，求所有的value之和
# 字典
def sum_value(d):
    sum_value = 0
    for i in d:  # 重点
        sum_value = sum_value + d[i]
    return sum_value


d = {'xsw': 10, 'lyj': 60, 'zd': 120}
print(sum_value(d))


# 列表
def sum_value(l):
    sum_value = 0
    for i in range(len(l)):  # 与字典的区别
        sum_value = sum_value + l[i]
    return sum_value


l = [10, 60, 120]
print(sum_value(l))


# 3.现在有一个排好序的列表，请设计一个函数:
#   函数的输入是一个元素
#   函数内部使用二分查找查找该元素
#   如果查找成功，则返回该元素对应的索引
#   如果列表中不存在该元素，则返回None


def binary_search(arr, l, r, x):  # arr为排好序的列表，l为列表最左的下标，r为最右的下标，x为要查找的元素
    if r >= l:
        mid = l + (r - l) // 2
        if x == arr[mid]:
            return mid
        if x < arr[mid]:
            return binary_search(arr, l, mid - 1, x)  # 递归
        if x > arr[mid]:
            return binary_search(arr, mid + 1, r, x)  # 递归
        else:
            return None


arr = [1, 3, 6, 8, 10, 15, 17, 20]
print(binary_search(arr, 0, len(arr) - 1, 15))
print(binary_search(arr, 0, len(arr) - 1, 2))

# 4.现在给到一个列表，请统计列表中各元素的个数
list2 = [2, 5, 19, 8, 5, 24, 5, 2, 3, 11, 2]
c = collections.Counter(list2)  # c.subtract可以从计数结果中减去个数，c.update可以增加元素统计
print(c)
dict_c = dict(c)
print(dict_c)
