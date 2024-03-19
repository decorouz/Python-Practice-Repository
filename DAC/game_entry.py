"""Application for storing a sequence of high score entries for a video game."""


class GameEntry:
    """Represents one entry of a list of high scores"""

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return f"{self._name}, {self._score}"


class ScoreBoard:
    """Fixed-length sequence of high scores in non-decreasing order"""

    def __int__(self, capacity=10):
        """Initial scoreboard with a given max capacity

        All entries are initially None"""
        self._board = [None] * capacity
        self._n = 0  # No. of actual entries

    def __getitem__(self, k):
        """Return entry at k index"""
        return self._board[k]

    def __str__(self):
        """Return string representation of the high score list"""
        return "\n".join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        """Add entry to high score board"""
        score = entry.get_score()
        # Does new entry have higher score
        # Yes, if the board is not full,or score is higher than last entry
        good = self._n < len(self._board) or score > self._board[-1].get_score()
        if good:
            if self._n < len(self._board):  # No score dropped from the list
                self._n += 1  # Overall number increase
        # Shift lower score rightward to make room for new entry
        j = self._n - 1
        while j > 0 and self._board[-1].get_score() < score:
            self._board[j] = self._board[j - 1]
            j -= 1
        self._board[j] = entry
