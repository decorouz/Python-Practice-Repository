"""Tic-Tac_Toe.

A game played in a three-by-three board.
This game is used to practice how two-dimensional
array can be used for positional game.
"""


class TicTacToe:
    """Keeps tracks of the moves and declare a winner."""

    def __init__(self) -> None:
        """Start a new game."""
        self._board = [[" "] * 3 for j in range(3)]
        self._player = "X"

    def mark(self, i, j):
        """Put an X or O mark at position (i,j) for next player s turn."""
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError("Invalid board position!")
        if self._board[i][j] != " ":
            raise ValueError("Board position occupied!")

        if self.winner() is not None:
            raise ValueError("Game is already completed")
        self._board[i][j] = self._player
        if self._player == "X":
            self._player = "O"
        else:
            self._player = "X"

    def _is_win(self, mark):
        """Check weather the board configuration is a win for a player."""

        board = self._board
        return (
            mark == board[0][0] == board[0][1] == board[0][2]
            or mark == board[1][0] == board[1][1] == board[1][2]
            or mark == board[2][0] == board[2][1] == board[2][2]
            or mark == board[0][0] == board[1][0] == board[2][0]
            or mark == board[0][1] == board[1][1] == board[2][1]
            or mark == board[0][2] == board[1][2] == board[2][2]
            or mark == board[0][0] == board[1][1] == board[2][2]  # diagonal
            or mark == board[0][2] == board[1][1] == board[2][0]  # rev diag
        )

    def winner(self):
        """Return mark of winning player, None to indicate a tie."""
        for mark in "XO":
            if self._is_win(mark):
                return mark
        return None

    def __str__(self) -> str:
        """Return string representation of current board."""
        rows = ["|".join(self._board[r]) for r in range(3)]
        return "\n-----\n ".join(rows)


# Driver

game = TicTacToe()
game.mark(1, 1)
game.mark(0, 2)
game.mark(2, 2)
game.mark(0, 0)
game.mark(0, 1)
game.mark(2, 1)
game.mark(1, 2)
game.mark(1, 0)
game.mark(2, 0)


print(game)
winner = game.winner()
if winner is None:
    print("Tie")
else:
    print(winner, "wins")
