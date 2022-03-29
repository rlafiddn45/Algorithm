N = int(input())
people = list(map(int, input().split()))
sv1, sv2 = map(int, input().split())
answer = 0
for person in people:
    answer += 1
    if person < sv1:
        continue
    if (person - sv1) % sv2:
        answer += (person - sv1) // sv2 + 1
    else:
        answer += (person - sv1) // sv2
print(answer)


'''
반 학생 수
총갑독관 / 부감독관

1. 반 학생수 <= 총감독관 감독 학생 수
-> answer += 1

2. 반 학생 수 > 총감독관 감독 학생 수
-> answer += 1, (반학생수 - 총감독관 감독 학생 수) // 부감독관 감독 학생 수 + 1 또는 나머지가 없으면 그대로
'''