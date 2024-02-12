def logistics(n, data, m, arr):
    sorted_data = []
    for i in arr:
        if i in data:
            sorted_data.extend([i] * data.count(i))
            data = [x for x in data if x != i]
    if n > m:
        sorted_data.extend(sorted(data))
    return sorted_data


if __name__ == '__main__':
    n = int(input())
    data = [int(element) for element in input().split()]
    m = int(input())
    arr = [int(element) for element in input().split()]
    print(*logistics(n, data, m, arr))