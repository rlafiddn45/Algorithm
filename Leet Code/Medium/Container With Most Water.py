from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        s, e = 0, len(height) - 1
        while s < e:
            water = (e - s) * min(height[s], height[e])
            answer = max(answer, water)
            if height[s] < height[e]:
                s += 1
            else:
                e -= 1
        return answer


