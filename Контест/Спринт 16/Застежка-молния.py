import sys

def zipper():
    length = int(sys.stdin.readline().rstrip())
    array1 = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    array2 = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    result = []
    i = 0
    while i < length:
        result.append(array1[i])
        result.append(array2[i])
        i += 1
    print(' '.join(list(map(str, result))))

if __name__ == '__main__':
	zipper()