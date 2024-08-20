import random
import curses

# Constants for game settings
BOARD_SIZE = 4
STARTING_TILES = 2
WINNING_TILE = 2048
UP = 'w'
DOWN = 's'
LEFT = 'a'
RIGHT = 'd'
QUIT = 'q'

def initialize_board():
    """Initializes a 4x4 board with two starting tiles."""
    board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    for _ in range(STARTING_TILES):
        add_random_tile(board)
    return board

def add_random_tile(board):
    """Adds a random tile (2 or 4) to an empty position on the board."""
    empty_positions = [(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if board[r][c] == 0]
    if empty_positions:
        r, c = random.choice(empty_positions)
        board[r][c] = random.choice([2, 4])

def merge_left(board):
    """Merges the tiles on the board to the left."""
    new_board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    for r in range(BOARD_SIZE):
        new_row = [tile for tile in board[r] if tile != 0]
        new_row_merged = []
        skip = False
        for i in range(len(new_row)):
            if skip:
                skip = False
                continue
            if i + 1 < len(new_row) and new_row[i] == new_row[i + 1]:
                new_row_merged.append(new_row[i] * 2)
                skip = True
            else:
                new_row_merged.append(new_row[i])
        new_row_merged.extend([0] * (BOARD_SIZE - len(new_row_merged)))
        new_board[r] = new_row_merged
    return new_board

def rotate_board(board, times=1):
    """Rotates the board 90 degrees clockwise 'times' times."""
    for _ in range(times):
        board = list(zip(*board[::-1]))
    return [list(row) for row in board]

def move(board, direction):
    """Moves and merges the board tiles in the given direction."""
    moved = False
    if direction == LEFT:
        new_board = merge_left(board)
    elif direction == RIGHT:
        new_board = merge_left([row[::-1] for row in board])
        new_board = [row[::-1] for row in new_board]
    elif direction == UP:
        new_board = rotate_board(board, 3)
        new_board = merge_left(new_board)
        new_board = rotate_board(new_board, 1)
    elif direction == DOWN:
        new_board = rotate_board(board, 1)
        new_board = merge_left(new_board)
        new_board = rotate_board(new_board, 3)
    else:
        return board, moved
    
    if new_board != board:
        moved = True
    return new_board, moved

def is_winning(board):
    """Checks if there is a winning tile on the board."""
    return any(WINNING_TILE in row for row in board)

def is_game_over(board):
    """Checks if the game is over (no moves left)."""
    for direction in [LEFT, RIGHT, UP, DOWN]:
        new_board, _ = move(board, direction)
        if new_board != board:
            return False
    return True

def draw_board(stdscr, board):
    """Draws the board on the terminal screen."""
    stdscr.clear()
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            stdscr.addstr(r * 2, c * 4, f"{board[r][c]:4}" if board[r][c] != 0 else "    ")
        stdscr.addstr((r + 1) * 2, 0, '-' * (BOARD_SIZE * 4))
    stdscr.refresh()

def main(stdscr):
    """Main game loop."""
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    
    board = initialize_board()
    draw_board(stdscr, board)

    while True:
        key = stdscr.getch()
        if key == ord(QUIT):
            break

        direction = None
        if key == ord(UP):
            direction = UP
        elif key == ord(DOWN):
            direction = DOWN
        elif key == ord(LEFT):
            direction = LEFT
        elif key == ord(RIGHT):
            direction = RIGHT

        if direction:
            new_board, moved = move(board, direction)
            if moved:
                add_random_tile(new_board)
                board = new_board
                draw_board(stdscr, board)
                if is_winning(board):
                    stdscr.addstr(0, 0, "You win!")
                    stdscr.refresh()
                    stdscr.getch()
                    break
                if is_game_over(board):
                    stdscr.addstr(0, 0, "Game over!")
                    stdscr.refresh()
                    stdscr.getch()
                    break

if __name__ == "__main__":
    curses.wrapper(main)
