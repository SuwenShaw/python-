# 20210616 两逆序数相加
l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]

# 1.位数少的用0补位
n = max(len(l1), len(l2))
if len(l1) < n:
    for i in range(len(l1), n):
        l1.append(0)
if len(l2) < n:
    for i in range(len(l2), n):
        l2.append(0)
print(l1)
print(l2)

# 2.求和
sum1 = 0
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


# 整合答案
def two_reverse_sum(l1, l2):
    # 1.位数少的用0补位
    n = max(len(l1), len(l2))
    if len(l1) < n:
        for i in range(len(l1), n):
            l1.append(0)
    if len(l2) < n:
        for i in range(len(l2), n):
            l2.append(0)

    # 2.求和
    sum1 = 0
    for i in range(0, n):
        sum1 = sum1 + l1[i] * (10 ** i) + l2[i] * (10 ** i)

    # 3.将和转为列表
    result = [int(x) for x in str(sum1)]

    # 4.将列表逆序
    result.reverse()
    return result


l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
print(two_reverse_sum(l1, l2))


# 20210617 无重复字符的最长字串
def longest_substring_length(s):
    # 特解
    if len(s) <= 1:
        return len(s)

    # 初始化左指针, 子串最大长度
    left, max_len = 0, 0

    # 创立一个字典用来跟踪每一个重复字符的位置
    dictionary = {}  # {'a':0, 'b':1}

    # 不断移动右指针
    for right in range(len(s)):
        # cur_char表示当前字符
        cur_char = s[right]
        # 如果当前字符之前重复过(重复位置为hashtable[cur_char])
        if cur_char in dictionary:
            # 在确保左指针不往反方向移动时将左指针移到重复位置 + 1
            if dictionary[cur_char] + 1 >= left:
                left = dictionary[cur_char] + 1
        # 更新当前字符最新重复位置为当前右指针位置
        dictionary[cur_char] = right
        # 在移动右指针的过程中，不断维护一个最大长度值
        max_len = max(max_len, right - left + 1)
    # 返回最大长度
    return max_len


s = 'abcadcf'
print(longest_substring_length(s))


# 20210618 两个正序数组的中位数
def two_sequence_median(nums1, nums2):
    # 合并两个有序数组：插入排序，短数组插入长数组里面去
    if len(nums2) <= len(nums1):
        nums = nums1 + nums2
        for i in range(len(nums1), len(nums)):
            j = i - 1
            key = nums[i]
            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j = j - 1
            nums[j + 1] = key
    else:
        nums = nums2 + nums1
        for i in range(len(nums2), len(nums)):
            j = i - 1
            key = nums[i]
            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j = j - 1
            nums[j + 1] = key

    # 合并后的数组nums中寻找中位数
    # 奇数个
    if len(nums) % 2 == 1:
        median_index = len(nums) // 2 + 1
        median = nums[median_index - 1]
        return median
    # 偶数个
    if len(nums) % 2 == 0:
        median_index1 = len(nums) // 2
        median_index2 = len(nums) // 2 + 1
        median = (nums[median_index1 - 1] + nums[median_index2 - 1]) / 2
        return median


nums1 = [1, 2, 5, 6]
nums2 = [1, 2, 3, 4]
print(two_sequence_median(nums1, nums2))
