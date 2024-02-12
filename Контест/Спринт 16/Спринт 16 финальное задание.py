# 106159695

from collections.abc import Iterable


def min_platform_count(cargos: Iterable[int], weight_limit: int) -> int:
    cargos = sorted(cargos)
    lightest_cargo_index, heaviest_cargo_index = 0, len(cargos) - 1
    platforms = 0

    while lightest_cargo_index <= heaviest_cargo_index:
        if (cargos[lightest_cargo_index]
                + cargos[heaviest_cargo_index] <= weight_limit):
            lightest_cargo_index += 1
        heaviest_cargo_index -= 1
        platforms += 1

    return platforms


if __name__ == '__main__':
    print(min_platform_count(
        cargos=list(
            map(
                int, input().split(' ')
            )
        ),
        weight_limit=int(input())
    ))
