# 2048 Game

## Overview

This is a terminal-based implementation of the classic 2048 game using Python and the `curses` library. The objective of the game is to combine tiles with the same number to reach the 2048 tile. The game continues until there are no valid moves left or the 2048 tile is achieved.

## Features

- 4x4 game board.
- Randomly generated starting tiles.
- Ability to move tiles up, down, left, or right.
- Merging tiles of the same value.
- Win condition when reaching the 2048 tile.
- Game over condition when no more moves are possible.

## Requirements

- Python 3.x
- `curses` library (usually included with Python on Unix-like systems)

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Ensure you have Python 3.x installed.** You can download it from [python.org](https://www.python.org/downloads/).

3. **Install any necessary packages** (if not already installed):

   ```bash
   pip install -r requirements.txt
   ```

   (Note: This project does not have external dependencies beyond Python's standard library.)

## Usage

1. **Run the game:**

   ```bash
   python 2048_game.py
   ```

2. **Game Controls:**

   - **Move Up:** `w`
   - **Move Down:** `s`
   - **Move Left:** `a`
   - **Move Right:** `d`
   - **Quit Game:** `q`

3. **Game Play:**

   - Use the `w`, `a`, `s`, and `d` keys to move the tiles in the desired direction.
   - Tiles with the same number will merge when they collide, doubling their value.
   - A new tile (either 2 or 4) will be added to the board after each move.
   - The game is won when a tile with the number 2048 is created.
   - The game ends when there are no valid moves left.

## Code Overview

- `initialize_board()`: Sets up a new game board with two starting tiles.
- `add_random_tile(board)`: Adds a new tile (2 or 4) to an empty position on the board.
- `merge_left(board)`: Merges tiles on the board to the left.
- `rotate_board(board, times=1)`: Rotates the board 90 degrees clockwise.
- `move(board, direction)`: Moves and merges tiles based on the direction (up, down, left, right).
- `is_winning(board)`: Checks if the 2048 tile is on the board.
- `is_game_over(board)`: Checks if the game is over (no valid moves left).
- `draw_board(stdscr, board)`: Draws the board on the terminal screen.
- `main(stdscr)`: The main game loop that handles input, updates the board, and manages game state.

## Troubleshooting

- **No visible board:** Ensure your terminal screen size is large enough to display the game board.
- **Controls not working:** Make sure your terminal supports `curses` and is configured to accept key inputs.

## Contributing

Feel free to contribute improvements or report issues by submitting a pull request or opening an issue on the repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


