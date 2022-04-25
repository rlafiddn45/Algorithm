def check(source, target):
    for s in source:
        if s not in target:
            return False
    return True


def solution(orders, course):
    answer = []
    sets = {}

    def track(set_menu, k, n):  # 세트메뉴, 인덱스, 선택개수
        if n in course:
            cnt = 0
            for order in orders:
                if check(set_menu, order):
                    cnt += 1
            key = ''.join(sorted(set_menu))
            sets[key] = cnt
        if k == len(menus):
            return
        else:
            track(set_menu, k + 1, n)  # 선택하지 않고 다음 것으로 넘어감
            track(set_menu + [menus[k]], k + 1, n + 1)  # 선택하고 다음 것으로 넘어감

    for order in orders:
        menus = list(order)
        track([], 0, 0)

    # print(sets)

    for c in course:
        arr = []  # 각 order 에 대한 임시 리스트
        max_cnt = 2
        for key, value in sets.items():
            # print('key, value :', key, value)
            if len(key) == c:
                if value > max_cnt:
                    max_cnt = value
                    arr = [key]
                elif value == max_cnt:
                    arr.append(key)
        answer += arr

    answer.sort()
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))


'''
메뉴를 새로 구성하려 한다.
단품으로만 제공하던 메뉴를 조합해서 코스요리 형태로 재구성해 새로운 메뉴를 제공하기로 결정했다.
각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성하기로 했다.
코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성하려고 한다.
최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 메뉴 후보에 올린다.

스카피가 새로 추가하기 될 코스요리의 메뉴 구성을 문자열 형태로 배열에 담아 return 한다.

조건
1. 개수가 맞아야 한다
2. 최소 2명 이상의 손님으로부터 주문되어야 한다
최대 100만개인데 그냥 combination 쓰면 된다
'''