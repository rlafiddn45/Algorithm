def solution(files):
    answer = []
    names = []
    for file in files:
        idx = 0
        head, number, tail = '', '', ''
        while not file[idx].isnumeric():
            head += file[idx]
            idx += 1
        while idx < len(file) and file[idx].isnumeric():
            number += file[idx]
            idx += 1
        while idx < len(file):
            tail += file[idx]
            idx += 1
        names.append([head, number, tail])
    for i in range(len(names)):
        idx = i
        while idx > 0:
            h1, n1, t1 = names[idx]
            h2, n2, t2 = names[idx - 1]
            if h1.lower() < h2.lower():
                names[idx], names[idx - 1] = names[idx - 1], names[idx]
            elif h1.lower() == h2.lower():
                if int(n1) < int(n2):
                    names[idx], names[idx - 1] = names[idx - 1], names[idx]
            idx -= 1
    answer = [''.join([name[0], name[1], name[2]]) for name in names]
    return answer


print(solution(["abc123.txt", "aa123.txt", "abc00123.txt"]))
print(solution(["abc12.txt", "ABC13.txt", "AAB12.txt", "AAB012.txt", "AAB013.txt"]))
print(solution(["muzi1.txt", "MUZI1.txt", "muzi001.txt", "muzi1.TXT"]))
print(solution(["img1", "img2"]))
print(solution(["ver-10.zip", "ver-9.zip"]))
print(solution(["muzi1.txt", "muzi-1.temp"]))
print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
