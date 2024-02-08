"""The Bowling Game Scorer."""

# Standard Library

# 3rd Party Library

# Project Library


# -----------------------------------------------------------------------------
class BowlingFrame:
    """Keeping the record of each bowling frame."""

    def __init__(self, max_roll = 2):
        """Construct a frame."""
        self.pins = [0]*max_roll
        self.max_roll = max_roll
        self.next_roll = 0

    def roll(self, pins: int):
        """Roll the ball swipe pins"""
        if self.next_roll < self.max_roll:
            self.pins[self.next_roll] = pins
            self.next_roll = self.next_roll + 1

    def score(self):
        """Score of each frame."""
        total = 0
        for index in range(self.max_roll):
            total = total + self.pins[index]
        return total


# -----------------------------------------------------------------------------
class BowlingFrame10(BowlingFrame):
    """Keeping the record of the 10th bowling frame."""

    def __init__(self):
        """Construct a frame."""
        super().__init__(3)


# -----------------------------------------------------------------------------
class BowlingGame:
    """The Bowling Game."""

    GAME_COMPLETE = -1

    def __init__(self):
        """Construct a BowlingGame object."""
        self.frames = []
        for _ in range(9):
            self.frames.append(BowlingFrame())

        self.frames.append(BowlingFrame10)
        self.cur_frame = 0      # current frame index
        self.cur_roll = 1       # current roll in frame

    def roll(self, num_of_pins: int):
        """Roll a bowling ball.

        Args:
            num_of_pins: The number of knocked-down pins

        Returns:
            None

        """
        index = self.cur_frame
        self.frames[index].roll(num_of_pins)
        if self.cur_roll == 1:
            self.cur_roll = self.cur_roll + 1
        elif self.cur_roll == 2 and index != 9:
            self.cur_frame = index + 1
            self.cur_roll = 1
        elif self.cur_roll == 2 and index == 9:
            self.cur_roll = self.cur_roll + 1
        elif self.cur_roll == 3:
            self.cur_roll = self.cur_roll + 1
        else:
            # Error
            print("Error")

    def score(self):
        """Get the current score.

        Returns:
            The current score.

        """
        bonus = 0

        # Handle spare
        total = 0
        for index in range(self.cur_frame + 1):
            total = total + self.frames[index].score()

        return total + bonus
