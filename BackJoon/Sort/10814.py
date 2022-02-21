N = int(input())
people = []
for _ in range(N):
    age, name = input().split()
    people.append([int(age), name])

people.sort(key=lambda x: x[0])

for person in people:
    age = str(person[0])
    name = person[1]
    print(age + ' ' + name)
