def solution(genres, plays):
    answer = []
    musics = {}
    for i in range(len(genres)):
        genre, play = genres[i], plays[i]
        if genre in musics:
            if play not in musics[genre]:
                musics[genre][play] = [i]
            else:
                musics[genre][play].append(i)
        else:
            musics[genre] = {}
            musics[genre][play] = [i]

    counts = []
    for music in musics:
        temp = 0
        count = musics[music]
        for c in count:
            temp += c * len(count[c])
        counts.append([temp, music])
    counts.sort(reverse=True)

    for count in counts:
        genre = count[1]
        arr = musics[genre]  # 장르별 노래 재생 횟수 리스트
        arr_cnt = [[a, arr[a]] for a in arr]
        arr_cnt.sort(reverse=True)
        temp = []
        for ac in arr_cnt:
            temp.extend(ac[1])
        if len(temp) == 1:
            answer.append(temp[0])
        else:
            answer.extend(temp[:2])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 500, 500, 500, 500]))
