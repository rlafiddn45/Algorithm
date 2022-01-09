def change_to_list(string):
    res = []
    for char in string:
        if char != '#':
            res.append(char)
        else:
            res[-1] = res[-1] + '#'
    return res


def cal_time(start, end):
    s_h, s_m = map(int, start.split(':'))
    e_h, e_m = map(int, end.split(':'))
    return (e_h - s_h) * 60 + e_m - s_m


def solution(m, musicinfos):
    answer, t = '(None)', 0
    music = change_to_list(m)
    for musicinfo in musicinfos:
        start_time, end_time, title, keys = musicinfo.split(',')
        time = cal_time(start_time, end_time)
        plays = change_to_list(keys)
        plays = (plays * (time // len(plays) + 1))[:time]
        for i in range(len(plays) - len(music) + 1):
            if plays[i:i + len(music)] == music:
                if t < time:
                    t = time
                    answer = title
    return answer


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("ABC#", ["12:00,12:06,HELLO,ABCABC#"]))
