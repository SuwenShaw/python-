# 20210616
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度

class Solution:

    # 方法1
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     def recursion(sub_string: str, chr: str):
    #         handled = set()
    #         for str_index in range(len(sub_string)):
    #             if handled.__contains__(sub_string[str_index]) \
    #                     or sub_string[str_index] == chr:
    #                 return str_index + 1
    #             handled.add(sub_string[str_index])
    #         return len(sub_string) + 1
    #
    #     result = 0
    #     for index in range(len(s)):
    #         tmp_result = recursion(s[index + 1:], s[index])
    #         result = tmp_result if tmp_result > result else result
    #
    #     return result

    # 方法二
    def lengthOfLongestSubstring(self, s: str) -> int:

        length = len(s)
        result = 0
        for index in range(length):
            handled = set()
            next_index = index
            handled.add(s[index])
            while next_index + 1 < length:
                if s[next_index + 1] in handled:
                    break
                handled.add(s[next_index + 1])
                next_index += 1
            result = max(next_index - index + 1, result)
        return result


instance = Solution()
print(instance.lengthOfLongestSubstring("bbbb"))
