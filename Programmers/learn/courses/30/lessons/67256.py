def solution(numbers, hand):
    answer = ''
    keypads = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2), 0: (3, 1)}
    l, r = (3, 0), (3, 2)
    for number in numbers:
        if number in (1, 4, 7):
            l = keypads[number]
            answer += 'L'
        elif number in (3, 6, 9):
            r = keypads[number]
            answer += 'R'
        else:
            x, y = keypads[number]
            diff_l, diff_r = abs(x - l[0]) + abs(y - l[1]), abs(x - r[0]) + abs(y - r[1])
            if diff_l < diff_r:
                answer += 'L'
                l = keypads[number]
            elif diff_l > diff_r:
                answer += 'R'
                r = keypads[number]
            else:
                if hand == 'right':
                    answer += 'R'
                    r = keypads[number]
                else:
                    answer += 'L'
                    l = keypads[number]
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
