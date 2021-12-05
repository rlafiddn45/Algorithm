def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridges, weights, idx, out = [], 0, 0, 0
    while idx < len(truck_weights):
        answer += 1  # 시간은 흐른다
        now = truck_weights[idx]  # 다리에 들어갈 차례가 된 트럭
        if weights + now <= weight and len(bridges) < bridge_length:  # 이번 트럭과 현재 다리 위 트럭의 무게들을 합했을 때 버틸 수 있다면
            bridges.append(0)  # 트럭이 있던 시간 추가
            weights += truck_weights[idx]
            idx += 1
        for i in range(len(bridges)):  # 시간이 흐른다
            bridges[i] += 1
        if bridges[0] == bridge_length:
            bridges.pop(0)
            weights -= truck_weights[out]
            out += 1
    return answer + bridge_length


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))


# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     bridge = [0] * bridge_length
#     idx = 0
#     bridge_sum = 0
#     while idx < len(truck_weights):
#         answer += 1
#         temp = idx
#         bridge_sum -= bridge.pop()
#         bridge = [0] + bridge
#         if (idx - temp + 1) <= bridge_length and truck_weights[idx] + bridge_sum <= weight:
#             bridge[0] = truck_weights[idx]
#             bridge_sum += truck_weights[idx]
#             idx += 1
#     answer += bridge_length
#     return answer