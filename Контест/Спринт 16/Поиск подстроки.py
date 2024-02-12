def find_longest_substr(s):
    max_length = 0
    start = 0
    char_dict = {}

    for end in range(len(s)):
        if s[end] in char_dict:
            start = max(start, char_dict[s[end]] + 1)
        char_dict[s[end]] = end
        max_length = max(max_length, end - start + 1)

    print(max_length)

input_str = input()
find_longest_substr(input_str)