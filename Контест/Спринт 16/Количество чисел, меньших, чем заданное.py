import sys 


def find_lower_numbers():
	array = list(map(int, sys.stdin.readline().rstrip().split(' ')))
	result = ''
	for i in range(len(array)):
		count = 0
		for j in range(len(array)):
			if array[j] < array[i]:
				count += 1
		result += str(count) + " "
	print(result.strip())


if __name__ == '__main__':
	find_lower_numbers()