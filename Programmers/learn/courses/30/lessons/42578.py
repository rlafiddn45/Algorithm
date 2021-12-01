def solution(clothes):
    answer = 1
    hash_clothes = {}
    for cloth in clothes:
        if cloth[1] in hash_clothes:
            hash_clothes[cloth[1]] += 1
        else:
            hash_clothes[cloth[1]] = 1
    for cloth in hash_clothes:
        answer *= hash_clothes[cloth] + 1
    return answer - 1


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
