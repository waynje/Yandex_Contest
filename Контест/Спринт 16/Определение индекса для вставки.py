import sys


def find_index():
    array = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    number = int(sys.stdin.readline().rstrip())
    array_len = len(array)
    max_item = max(array)
    for index, item in enumerate(array):
        if number > max_item:
            print(array_len)
            break
        if item == number or item > number:
            print(index)
            break

if __name__ == '__main__':
	find_index()