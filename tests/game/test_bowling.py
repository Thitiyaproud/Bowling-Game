"""Test module for the Bowling Kata."""

# Standard Library

# 3rd Party Library
import pytest

# Project Library
from game.bowling import BowlingGame
from game.bowling import BowlingFrame

# -----------------------------------------------------------------------------
class TestBowlingFrame:
    """Test cases for Bowling Frame."""
    def test_construct_bowling_frame(self):
        """Construct a bowling frame"""
        # Arrange
        # Act
        frame = BowlingFrame()

        # Assert
        assert frame.score() == 0

    @pytest.mark.parametrize(
        "num_pins",
        [
            8, 9, 10
        ]
    )
    def test_one_roll(self, num_pins):
        """Roll."""
        # Arrange
        frame = BowlingFrame()

        # Act
        frame.roll(num_pins)

        # Assert
        assert frame.score() == num_pins

    @pytest.mark.parametrize(
        "num_pins_1, num_pins_2, expected_score",
        [
            (1, 5, 6),
            (3, 7, 10),
            (4, 2, 6)
        ]
    )
    def test_two_rolls(self, num_pins_1, num_pins_2, expected_score):
        """Roll."""
        # Arrange
        frame = BowlingFrame()

        # Act
        frame.roll(num_pins_1)
        frame.roll(num_pins_2)

        # Assert
        assert frame.score() == expected_score

    def test_is_spare(self):
        """Test if the frame is a spare."""
        # Arrange
        frame = BowlingFrame()
        # Act
        frame.roll(5)
        frame.roll(5)  # Spare
        # Assert
        assert frame.is_spare() == True

    def test_is_not_spare(self):
        """Test if the frame is not a spare."""
        # Arrange
        frame = BowlingFrame()
        # Act
        frame.roll(3)
        frame.roll(4)
        # Assert
        assert frame.is_spare() == False

    def test_is_strike(self):
        """Test if the frame is a strike."""
        # Arrange
        frame = BowlingFrame()
        # Act
        frame.roll(10)  # Strike
        # Assert
        assert frame.is_strike() == True

    def test_is_not_strike(self):
        """Test if the frame is not a strike."""
        # Arrange
        frame = BowlingFrame()
        # Act
        frame.roll(7)
        frame.roll(2)
        # Assert
        assert frame.is_strike() == False

# -----------------------------------------------------------------------------
def test_constructor():
    """Construct a BowlingGame object.

    Given: -
    When: Construct a BowlingGame object.
    Then: The initial score must be 0.

    """
    # Arrange
    expected_initial_score = 0

    # Act
    game = BowlingGame()

    # Assert
    result = game.score()
    assert result == expected_initial_score

@pytest.mark.parametrize(
    "list_of_rolls, expected_score",
    [
        # Test cases for spares and strikes
        ([5, 5, 3, 4] + [0]*16, 20),  # Spare, then regular rolls
        ([10, 3, 4] + [0]*17, 24),     # Strike, then regular rolls
        ([10, 10, 10] + [0]*15, 60),   # Three consecutive strikes
        ([9, 1, 5, 5] + [0]*16, 25),   # Spare, then regular rolls
    ]
)
def test_given_rolls_return_score(list_of_rolls, expected_score):
    """Given a list of rolls, return total scores."""
    # Arrange
    game = BowlingGame()
    # Act
    for pins in list_of_rolls:
        game.roll(pins)
    # Assert
    result = game.score()
    assert result == expected_score


# -----------------------------------------------------------------------------
@pytest.mark.parametrize(
    "list_of_rolls, expected_score",
    [
        # No frame roll 10 pins
        ([], 0),
        ([8], 8),
        ([8, 1], 9),
        ([8, 1, 5], 14),
        ([8, 1, 5, 3], 17),
        ([8, 1, 5, 3, 8], 25),
        ([8, 1, 5, 3, 8, 0], 25),
        ([8, 1, 5, 3, 8, 0, 2], 27),
        ([8, 1, 5, 3, 8, 0, 2, 3], 30),
        ([8, 1, 5, 3, 8, 0, 2, 3, 5], 35),
        ([8, 1, 5, 3, 8, 0, 2, 3, 5, 4], 39),

        # # A frame with 10 pins
        # ([2, 4, 3, 7, 7], 30),
    ]
)
def test_given_rolls_return_score(list_of_rolls, expected_score):
    """Given a list of rools, return total scores."""
    # Arrange
    game = BowlingGame()

    for pins in list_of_rolls:
        game.roll(pins)

    # Act
    result = game.score()

    # Assert
    assert result == expected_score
