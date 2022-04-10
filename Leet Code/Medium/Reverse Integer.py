class Solution:
    def reverse(self, x: int) -> int:
        result = ''
        x = str(x)
        for i in range(len(x) - 1, -1, -1):
            if x[i] == '-':
                result = '-' + result
            else:
                result += x[i]
        result = int(result)
        if result > pow(2, 31) or result < -1 * pow(2, 31):
            result = 0
        return result
