board = list(range(1, 10))


# wins_line = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (7, 5, 3)]


def draw_board():
    print("_____________")
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
    print("_____________")


def take_input(player_token):
    while True:
        value = input("Куда поставить? " + player_token)
        if not (value in "123456789"):
            print("Ошибка значения. Повторите ввод ячейки")
            continue
        value = int(value)
        if str(board[value - 1]) in "X0":
            print("Клетка занята")
            continue
        board[value - 1] = player_token
        break


def check_win():
    wins_line = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (7, 5, 3)]
    for each in wins_line:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1]
    return False


def main():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("0")
        if counter > 3:
            winner = check_win()
            if winner:
                draw_board()
                print(winner, "Выйграл")
                break
        counter += 1
        if counter > 8:
            draw_board()
            print("Ничья")




check_win()





main()
