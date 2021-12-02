# def solution(genres, plays):
#     answer = []
#     musics = {}
#     for i in range(len(genres)):
#         genre, play = genres[i], plays[i]
#         if genre not in musics:
#             musics[genre] = []
#         if len(musics[genre]) == 0:
#             musics[genre] = [i]
#         elif len(musics[genre]) == 1:
#             m, n = plays[musics[genre][0]], play
#             if m > n:
#                 musics[genre] = [musics[genre][0], i]
#             else:
#                 musics[genre] = [i, musics[genre][0]]
#         else:
#             l, m, n = plays[musics[genre][0]], plays[musics[genre][1]], play
#             if n > l:
#                 musics[genre] = [i, musics[genre][0]]
#             elif m < n < l:
#                 musics[genre] = [musics[genre][0], i]
#     cnt = {}
#     for i in range(len(genres)):
#         genre, play = genres[i], plays[i]
#         if genre not in cnt:
#             cnt[genre] = play
#         else:
#             cnt[genre] += play
#     cnt_list = [[cnt[c], c] for c in cnt]
#     cnt_list.sort(reverse=True)
#     for c in cnt_list:
#         answer.extend(musics[c[1]])
#     return answer
#
#
# print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

def solution(genres, plays):
    answer = []
    hash_genres = {}
    hash_plays = {}

    for i in range(len(genres)):
        genre, play = genres[i], plays[i]
        if genre not in hash_genres:
            hash_genres[genre] = [play]
        else:
            hash_genres[genre].append(play)
        if play not in hash_plays:
            hash_plays[play] = i

    for hg in hash_genres:
        hash_genres[hg].sort(reverse=True)

    cnt = {}
    for i in range(len(genres)):
        genre, play = genres[i], plays[i]
        if genre not in cnt:
            cnt[genre] = play
        else:
            cnt[genre] += play
    cnt_list = [[cnt[c], c] for c in cnt]
    cnt_list.sort(reverse=True)

    for c in cnt_list:
        n = hash_genres[c[1]]
        if len(n) == 1:
            answer.append(hash_plays[n[0]])
        else:
            answer.append(hash_plays[n[0]])
            answer.append(hash_plays[n[1]])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print(solution(["classic1", "pop1", "classic2", "classic3", "pop1"], [500, 600, 150, 800, 2500]))
