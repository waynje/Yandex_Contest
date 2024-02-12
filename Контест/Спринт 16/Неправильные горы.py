import sys


def valid_mountain_array(array):
    array_len = len(array)
    max_height = max(array)
    max_height_index = array.index(max_height)
    if max_height_index == 0 or max_height_index == array_len-1:
        return False

    for index, item in enumerate(array):
        if index != 0:
            if (((index < max_height_index) and (item <= array[index - 1]))
                    or ((index > max_height_index) and (item >= array[index - 1]))):
                return False
    return True


def main():
    array = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    print(valid_mountain_array(array))


if __name__ == '__main__':
    main()
