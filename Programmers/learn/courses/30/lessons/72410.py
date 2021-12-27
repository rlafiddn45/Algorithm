def step1(string):
    return string.lower()


def step2(string):
    for s in string:
        if not s.isalnum() and s not in ('-', '_', '.'):
            string = string.replace(s, '')
    return string


def step3(string):
    while '..' in string:
        string = string.replace('..', '.')
    return string


def step4(string):
    if string == '.':
        return ''
    if len(string) > 1:
        if string[0] == '.':
            string = string[1:]
        if string[-1] == '.':
            string = string[:-1]
    return string


def step5(string):
    if string == '':
        return 'a'
    return string


def step6(string):
    if len(string) > 15:
        string = string[:15]
    if string[-1] == '.':
        string = string[:-1]
    return string


def step7(string):
    if len(string) <= 2:
        while len(string) < 3:
            string += string[-1]
    return string


def solution(new_id):
    new_id = step1(new_id)  # 1단계
    new_id = step2(new_id)  # 2단계
    new_id = step3(new_id)  # 3단계
    new_id = step4(new_id)  # 4단계
    new_id = step5(new_id)  # 5단계
    new_id = step6(new_id)  # 6단계
    new_id = step7(new_id)  # 7단계
    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution(	"=.="))
