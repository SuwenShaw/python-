# 20210618
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数
# 中位数: 一组已排序样本中最中间的那个数，如果样本有奇数个，取最中间的那个值，如果样本有偶数个，取最中间的两个数的均值
# 解题思路: 合并 --> 排序 --> 求中值


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        temp_list = nums1[:]
        temp_list.extend(nums2)
        new_list = sorted(temp_list)
        length = len(temp_list)
        half = length // 2
        return new_list[half] if length % 2 == 1 else (new_list[half] + new_list[half - 1]) / 2


instance = Solution()
result = instance.findMedianSortedArrays([1, 2, 3, 4, 8], [2, 3, 7, 9])
print(result)
