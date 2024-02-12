def fibonachchi(index: int) -> int:
    if index <= 1:
        return 1
    return fibonachchi(index - 1) + fibonachchi(index - 2)


if __name__ == '__main__':
    index = int(input())
    print(str(fibonachchi(index)))