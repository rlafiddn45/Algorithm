# from typing import List
#
#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         dic = {}
#         for i in range(len(nums)):
#             dic[i] = nums[i]
#         for key in dic:
#             if target - dic[key] in dic.values():
#                 idx = nums.index(target - dic[key])
#                 if idx != key:
#                     return [key, idx]
#
#
# sol = Solution()
# print(sol.twoSum(nums=[3, 3], target=6))


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]], i]
            else:
                dic[target - nums[i]] = i


sol = Solution()
print(sol.twoSum(nums=[3, 3], target=6))


