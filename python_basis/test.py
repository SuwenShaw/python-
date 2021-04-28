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
from math import pi
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
