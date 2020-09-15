#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 方法一 哈希方法
        import collections
        # num1 = collections.Counter(nums1)
        # num2 = collections.Counter(nums2)
        # print("nums1 = ", nums1)
        # print("nums2 = ", nums2)
        # 值得注意的一点是counter 的& 与 运算
        # num = num1 & num2
        # return num.elements()

        # counts = collections.Counter(nums1)
        # res = []

        # for num in nums2:
        #     if counts[num] > 0:
        #         res += num,
        #         counts[num] -= 1
        # print('res = ', res)
        # return res
        # 方法二， 排序法
        nums1, nums2 = sorted(nums1), sorted(nums2)
        pt1 = pt2 = 0
        res = []

        while True:
            try:
                if nums1[pt1] > nums2[pt2]:
                    pt2 += 1
                elif nums1[pt1] < nums2[pt2]:
                    pt1 += 1
                else:
                    res.append(nums1[pt1])
                    pt1 += 1
                    pt2 += 1
            except IndexError:
                break

        return res
     
         


            
        
# @lc code=end

