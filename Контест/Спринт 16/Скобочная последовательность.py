def is_correct_bracket_seq(check_string):
    if not len(check_string):
        return True
    if len(check_string) % 2:
        return False
    etalon = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    stack = []
    for i in check_string:
        if i in etalon.values():
            stack.append(i)
            continue
        if len(stack) and etalon[i] == stack[-1]:
            stack.pop()
            continue
        return False
    if not len(stack):
        return True
    return False

check_string = input()
print(is_correct_bracket_seq(check_string))