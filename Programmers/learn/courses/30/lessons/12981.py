"""
rule
1. 처음 사람부터 마지막까지 말하고, 마지막 사람 뒤에는 다시 처음 사람이 말한다
2. 앞 사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 한다
3. 한 번 사용한 단어는 다시 사용할 수 없다
4. 한 글자는 불가능하다
"""


def solution(n, words):
    answer = [0, 0]
    used, people, last, idx = [], [0] * n, '', 0
    for word in words:
        if last == '':
            last = word
            used.append(word)
        else:
            if last[-1] == word[0] and word not in used:
                last = word
                used.append(word)
            else:
                answer = [idx + 1, people[idx] + 1]
                break
        people[idx], idx = people[idx] + 1, idx + 1
        if idx == n:
            idx -= n
    return answer


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
