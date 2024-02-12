def max_blocks(length, array):
    blocks = 0
    for end_position in range(length):
        if max(array[:end_position+1]) == end_position:
            blocks += 1
    return blocks


if __name__ == '__main__':
    length = int(input())
    array = list(map(int, input().split(' ')))
    print(str(max_blocks(length, array)))