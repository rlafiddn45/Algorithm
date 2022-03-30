# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         num = str(x)
#         if num == num[::-1]:
#             return True
#         else:
#             return False
#
#
# sol = Solution()
# res = sol.isPalindrome(101)
# print(res)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            arr, temp_num = [], x
            print('temp_num :', temp_num)
            while temp_num:
                arr.append(temp_num % 10)
                temp_num //= 10
            print('arr :', arr)
            num = 0
            for i in range(len(arr)):
                num += pow(10, i) * arr[len(arr) - i - 1]
            print('arr, num :', arr, num)
            if num == x:
                return True
            else:
                return False



sol = Solution()
res = sol.isPalindrome(10)
print(res)

