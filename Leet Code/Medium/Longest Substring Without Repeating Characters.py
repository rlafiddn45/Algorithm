class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        words = []
        idx = 0
        while idx < len(s):
            temp = ''
            i = idx
            while i < len(s) and s[i] not in temp:
                temp += s[i]
                i += 1
            idx += 1
            words.append(temp)
        print('words :', words)
        words.sort(key=lambda x: len(x))
        return len(words[-1])



sol = Solution()
print(sol.lengthOfLongestSubstring(""))
