# 20210615
# https://leetcode-cn.com/problems/add-two-numbers/
# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 注意要点:
#   直接相加结果会溢出，所以不能通过直接相加得到
#   利用相加的特性，从个位开始加，遇到 10 进位，结果的余数为该位的值

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        header = ListNode()
        next = header
        carry_flag = False  # 进位标记

        while l1 is not None or l2 is not None:
            # 计算
            value1 = 0
            value2 = 0
            if l1 is not None:
                value1 = l1.val
                l1 = l1.next
            if l2 is not None:
                value2 = l2.val
                l2 = l2.next
            if carry_flag:
                result_tmp = value1 + value2 + 1
            else:
                result_tmp = value1 + value2
            carry_flag = False
            if result_tmp > 9:
                result_tmp = result_tmp % 10
                carry_flag = True
            next.next = ListNode(val=result_tmp)
            next = next.next

        # 最后是否有进位，如果有需要加进去
        if carry_flag:
            next.next = ListNode(val=1)
        return header.next


node1 = ListNode(val=9)
node2 = ListNode(val=9)
node3 = ListNode(val=9)
node4 = ListNode(val=9)
node5 = ListNode(val=9)
node6 = ListNode(val=9)
node7 = ListNode(val=9)

node8 = ListNode(val=9)
node9 = ListNode(val=9)
node10 = ListNode(val=9)
node11 = ListNode(val=9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

node8.next = node9
node9.next = node10
node10.next = node11

solution = Solution()

result = solution.addTwoNumbers(node1, node8)

# 查看结果
while result is not None:
    value = result.val
    print(value)
    result = result.next
