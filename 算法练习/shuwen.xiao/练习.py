# 20210616 两逆序数相加
l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
sum1 = 0
n = max(len(l1), len(l2))

# 1.位数少的用0补位
if len(l1)<n:
    for i in range(len(l1), n):
        l1.append(0)
if len(l2)<n:
    for i in range(len(l2), n):
        l2.append(0)
print(l1)
print(l2)

# 2.求和
for i in range(0, n):
    sum1 = sum1 + l1[i]*(10**i) + l2[i]*(10**i)

print(sum1)

# 3.将和转为列表
# 方法一(转为列表后，元素依然是字符串，不可取)
sum2 = str(sum1)
print(sum2)
sum3 = list(sum2)
print(sum3)

# 方法二(在python3中输出结果为map object，不可取)
print(map(int, str(sum1)))

# 方法三(✅)
result = [int(x) for x in str(sum1)]
print(result)

# 4.将列表逆序
# 方法一：循环
output = []
for i in range(-1, -(len(result) + 1), -1):  # range(start,stop[,step])
    output.append(result[i])

print(output)

# 方法二：列表切片
print(result[::1])   # 正序
print(result[::-1])  # 逆序

# 方法三：反转
result.reverse()
print(result)
