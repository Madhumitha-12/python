def print_board(b):
    for r in b: print(" ".join(r))

def win(b, p):
    return any(all(c == p for c in r) for r in b) or \
           any(all(r[c] == p for r in b) for c in range(3)) or \
           all(b[i][i] == p for i in range(3)) or \
           all(b[i][2 - i] == p for i in range(3))

def draw(b):
    return all(c != ' ' for r in b for c in r)

def tic_tac_toe():
    b = [[' ']*3 for _ in range(3)]
    players = 'XO'
    turn = 0
    while True:
        print_board(b)
        p = players[turn % 2]
        row, col = map(int, input(f"Player {p}, enter row and column (0-2): ").split())
        if b[row][col] == ' ':
            b[row][col] = p
            if win(b, p):
                print_board(b)
                print(f"Player {p} wins!")
                break
            if draw(b):
                print_board(b)
                print("It's a draw!")
                break
            turn += 1
        else:
            print("Cell is already occupied, try again.")

tic_tac_toe()
