# 107225242

def decode_string(s):
    stack: list = []
    number: int = 0
    string: str = ''

    for character in s: 
        if character.isdigit(): 
            number = number * 10 + int(character)
        elif character == '[':
            stack.append((number, string))
            number = 0
            string = '' 
        elif character == ']':
            previous_number, previous_string = stack.pop()
            string = previous_string + string * previous_number
        else:
            string += character
    print(string)


if __name__ == '__main__':
    s = input()
    decode_string(s)
