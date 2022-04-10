from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []
        for op in ops:
            if op.isnumeric():
                scores.append(int(op))  # 1번 조건
            else:
                if op[0] == '-':
                    scores.append(int(op))  # 음수인 경우
                elif op == 'C':  # 4번 조건
                    scores.pop()
                elif op == 'D':  # 3번 조건
                    scores.append(2 * int(scores[-1]))
                elif op == '+':  # 2번 조건
                    scores.append(int(scores[-1]) + int(scores[-2]))
        return sum(scores)


'''
야구 규칙
1. 처음엔 0 점으로 시작한다
2. ops 배열이 주어지며, op[i] 는 i 번째 동작을 의미한다
   1) x 는 새로운 x 점을 추가한다
   2) + 는 앞의 2개의 점수를 더한 값을 추가한다
   3) D 는 앞의 1개의 점수를 2배하는 값을 추가한다
   4) C 는 앞의 1개의 점수를 제거하는 것을 말한다
'''