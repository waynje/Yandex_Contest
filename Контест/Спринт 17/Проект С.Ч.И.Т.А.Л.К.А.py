def shitalka(P, B):
    players = list(range(1, P+1))
    position = 0

    while len(players) > 1:
        position = (position + B - 1) % len(players)
        players.pop(position)
    return players[0]


def main():
    player_count = int(input('Количество игроков: '))
    beat = int(input('Количество тактов: '))
    print(shitalka(player_count, beat))


if __name__ == '__main__':
    main()
