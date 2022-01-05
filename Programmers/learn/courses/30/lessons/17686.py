def solution(files):
    answer = []
    texts = []
    for file in files:
        s, e = 0, 0
        idx = 0
        head, number, tail = '', '', ''
        while not file[idx].isnumeric():
            head += file[idx]
            idx += 1
        while idx < len(file) and file[idx].isnumeric():
            number += file[idx]
            idx += 1
        tail = file[idx:]
        texts.append([head, number, tail])
    for i in range(len(texts)):
        h1, n1, t1 = texts[i]
        for j in range(len(texts)):
            h2, n2, t2 = texts[j]
            if h1.lower() < h2.lower():
                texts[i], texts[j] = texts[j], texts[i]
            elif h1.lower() == h2.lower():
                if int(n1) < int(n2):
                    texts[i], texts[j] = texts[j], texts[i]
    for text in texts:
        answer.append(''.join(text))
    return answer


print(solution(["abc123.txt", "aa123.txt", "abc00123.txt"]))
# print(solution(["abc12.txt", "ABC13.txt", "AAB12.txt", "AAB012.txt", "AAB013.txt"]))
# print(solution(["muzi1.txt", "MUZI1.txt", "muzi001.txt", "muzi1.TXT"]))
# print(solution(["img1", "img2"]))
# print(solution(["ver-10.zip", "ver-9.zip"]))
# print(solution(["muzi1.txt", "muzi-1.temp"]))
print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
