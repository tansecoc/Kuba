# Author: Cas Tanseco
# Date: 6/9/2021
# Description:  This is a program for the Kuba board game.  It is a fully functional game that allows
#               two players to play the game of Kuba.

import copy


class KubaGame:
    """
    This class represents a fully functional Kuba game. It creates a new Kuba game instance, players,
    manages turns, gets the current turn, and manages moves.  This class also interacts with the Board
    class to obtain marble count, score, and winner data.
    """

    def __init__(self, player1, player2):
        """
        Initializes an instance of the KubaGame class, creates players, creates the game board, creates
        data members to determine turn and winner.
        """
        # player 1 data members
        self._player1_name = player1[0]
        self._player1_color = player1[1]
        self._player1_captured = 0

        # player 2 data members
        self._player2_name = player2[0]
        self._player2_color = player2[1]
        self._player2_captured = 0

        # winner and turn data members
        self._winner = None
        self._turn = None

        # board data members
        board = {}
        self._previous_board = None
        self._interim_board = None
        self._board = board

        for row in range(0, 7):
            for column in range(0, 7):
                coordinate = (int(row), int(column))
                board[coordinate] = 'X'

        # set white marble initial positions
        board[0, 0] = 'W'
        board[0, 1] = 'W'
        board[1, 0] = 'W'
        board[1, 1] = 'W'

        board[5, 5] = 'W'
        board[5, 6] = 'W'
        board[6, 5] = 'W'
        board[6, 6] = 'W'

        # set black marble initial positions
        board[0, 5] = 'B'
        board[0, 6] = 'B'
        board[1, 5] = 'B'
        board[1, 6] = 'B'

        board[5, 0] = 'B'
        board[5, 1] = 'B'
        board[6, 0] = 'B'
        board[6, 1] = 'B'

        # set red marble initial positions
        board[1, 3] = 'R'
        board[2, 2] = 'R'
        board[2, 3] = 'R'
        board[2, 4] = 'R'
        board[3, 1] = 'R'
        board[3, 2] = 'R'
        board[3, 3] = 'R'
        board[3, 4] = 'R'
        board[3, 5] = 'R'
        board[4, 2] = 'R'
        board[4, 3] = 'R'
        board[4, 4] = 'R'
        board[5, 3] = 'R'

    def get_player_color(self, playername):
        """
        Returns color of player's marble.
        """
        if playername == self._player1_name:
            return self._player1_color
        if playername == self._player2_name:
            return self._player2_color

    def display_board(self):
        """
        Displays board with current marble positions.
        """
        for i, key in enumerate(self._board):
            print(self._board[key], end=" ")
            if i % 7 == 6:
                print("\n", end="")

    def display_board_coordinates(self):
        """
        Displays board with coordinates and current marble positions.
        """
        for item, key in enumerate(self._board):
            print(key, self._board[key], end=" ")
            if item % 7 == 6:
                print("\n", end="")

    def get_current_turn(self):
        """
        Returns the name of the player who has the next turn. Returns 'None' if the first move has yet to be made.
        """
        return self._turn

    def make_move(self, playername, coordinates, direction):
        """
        Used for when a player moves a marble on the board.  If move is valid, then board is updated
        per move and 'True' is returned.  If move is invalid, then move is rejected and 'False' is returned.
        This method also determines if there is a winner after a valid move is made.
        """

        # Create coordinates variables for validation checks
        directions_dict = {'F': (-1, 0), 'B': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        direction_coordinates = directions_dict[direction]
        new_coordinates = tuple(sum(x) for x in zip(coordinates, direction_coordinates))
        opposite_direction = tuple(x * y for x, y in zip(direction_coordinates, (-1, -1)))
        opposite_coordinates = tuple(sum(x) for x in zip(coordinates, opposite_direction))

        # -----------------------------------------------------------------
        # Pre-move validation checks.  Checks will set valid_flag to 'False'
        # if move is invalid.
        # -----------------------------------------------------------------

        # Initially set valid_flag to True (valid move = True, invalid move = False)
        valid_flag = True

        # Set valid_flag to 'False' if game has already been won
        if self._winner is not None:
            valid_flag = False

        # Set valid_flag to 'False' if playername is not equal to player 1 or player 2
        if playername != self._player1_name and playername != self._player2_name:
            valid_flag = False

        # Set valid_flag to 'False' if it is not the player's turn
        if playername != self._turn and self._turn is not None:
            valid_flag = False

        # Set valid_flag to 'False' if parameter coordinates do not exist in board
        if coordinates not in self._board:
            valid_flag = False
            return valid_flag  # return valid_flag to prevent KeyError

        # Set valid_flag to 'False' if marble does not belong to respective player
        if playername == self._player1_name and self._board[coordinates] != self._player1_color:
            valid_flag = False
        if playername == self._player2_name and self._board[coordinates] != self._player2_color:
            valid_flag = False

        # Set valid_flag to 'False' if movement is to coordinates that do not exist on board
        if new_coordinates not in self._board:
            valid_flag = False

        # Set valid_flag to 'False' if coordinates opposite the direction of movement are not empty
        try:
            if self._board[opposite_coordinates] != 'X':
                valid_flag = False
        except KeyError:
            pass

        # return "False" if move does not pass the above validation checks
        if not valid_flag:
            return valid_flag

        # -----------------------------------------------------------------
        # If move is valid make move and update the board accordingly.
        # This section also includes additional checks to validate that:
        # 1) the move does not push the player's own marble off the board
        # 2) the move does not undo the opponent's previous move.
        # -----------------------------------------------------------------

        # create deep copies for validations
        self._previous_board = self._interim_board
        self._interim_board = copy.deepcopy(self._board)

        # set current_coordinates and current_marble to parameter coordinates
        current_coordinates = coordinates
        current_marble = self._board[coordinates]

        # set next_coordinates and next_marble to direction_coordinates offset
        next_coordinates = tuple(sum(x) for x in zip(current_coordinates, direction_coordinates))
        next_marble = self._board[next_coordinates]

        # set initial parameter coordinates to empty space: 'X'
        self._board[current_coordinates] = 'X'

        # set captured_marble to None
        captured_marble = None

        # try:
        while current_marble != 'X' and next_marble is not None:
            # set current_coordinates to next_coordinates
            current_coordinates = next_coordinates

            # set next_coordinates to direction_coordinates offset
            if tuple(sum(x) for x in zip(next_coordinates, direction_coordinates)) in self._board:
                next_coordinates = tuple(sum(x) for x in zip(next_coordinates, direction_coordinates))
            else:
                next_coordinates = None

            # place current_marble in current_coordinates
            self._board[current_coordinates] = current_marble

            # set current_marble to next_marble
            current_marble = next_marble

            try:
                # set next_marble to marble at next_coordinates
                next_marble = self._board[next_coordinates]
            except KeyError:
                # capture marble that gets pushed off the board
                captured_marble = next_marble
                next_marble = None

        # Set valid_flag to False and reject move if move results in player's own marble getting pushed off the board
        if captured_marble == self.get_player_color(playername):
            valid_flag = False
            self._board = copy.deepcopy(self._interim_board)

        # Set valid_flag to False and reject move if move undoes opponent's move
        if self._board == self._previous_board:
            self._board = copy.deepcopy(self._interim_board)
            valid_flag = False

        if not valid_flag:
            return valid_flag

        # -----------------------------------------------------------------
        # After successful move:
        # 1) update player score if any red marbles are captured
        # 2) determine if player has won
        # 3) return 'True'
        # -----------------------------------------------------------------

        # if marble is red then add 1 point to player's captured_marble
        if playername == self._player1_name and captured_marble == 'R':
            self._player1_captured += 1
        if playername == self._player2_name and captured_marble == 'R':
            self._player2_captured += 1

        # if player has 7 red marbles then mark player as winner
        if self._player1_captured >= 7:
            self._winner = self._player1_name
        if self._player2_captured >= 7:
            self._winner = self._player2_name

        # if the opponent has no more marbles then mark player as winner
        if self._player1_color not in self._board.values():
            self._winner = playername
        if self._player2_color not in self._board.values():
            self._winner = playername

        # if the opponent's marbles are surrounded and cannot move in any direction then player wins
        # set player available_moves counters to 0
        player1_available_moves = 0
        player2_available_moves = 0

        for key_coordinates in self._board:
            for dict_coordinates in directions_dict.values():

                if self._board[key_coordinates] == self._player1_color:
                    try:
                        adjacent_coordinates = tuple(sum(x) for x in zip(key_coordinates, dict_coordinates))
                        if self._board[adjacent_coordinates] == 'X':
                            player1_available_moves += 1
                    except KeyError:
                        player1_available_moves += 1

                if self._board[key_coordinates] == self._player2_color:

                    try:
                        adjacent_coordinates = tuple(sum(x) for x in zip(key_coordinates, dict_coordinates))
                        if self._board[adjacent_coordinates] == 'X':
                            player2_available_moves += 1
                    except KeyError:
                        player2_available_moves += 1

        # if a given player has no available moves then set opposing player as winner
        if player1_available_moves == 0:
            self._winner = self._player2_name
        if player2_available_moves == 0:
            self._winner = self._player1_color

        if playername == self._player1_name:
            self._turn = self._player2_name
        if playername == self._player2_name:
            self._turn = self._player1_name

        return valid_flag

    def get_winner(self):
        """
        Returns the name of the winning player.
        """
        if self._player1_captured >= 7:
            self._winner = self._player1_name
        if self._player2_captured >= 7:
            self._winner = self._player2_name
        return self._winner

    def get_captured(self, playername):
        """
        Returns the number of Red marbles captured by the player.
        """
        if playername == self._player1_name:
            return self._player1_captured
        elif playername == self._player2_name:
            return self._player2_captured
        else:
            return "Invalid player name"

    def get_marble(self, coordinates):
        """
        Returns the marble at a given set of coordinates.  Returns 'X' if no marble is present at the coordinates.
        """
        try:
            return self._board[coordinates]
        except KeyError:
            return "Invalid coordinates"

    def get_marble_count(self):
        """
        Returns a tuple with the number of White, Black, and Red marbles.
        """
        W = 0
        B = 0
        R = 0

        for item, key in enumerate(self._board):
            if self._board[key] == 'W':
                W += 1
            if self._board[key] == 'B':
                B += 1
            if self._board[key] == 'R':
                R += 1

        marble_count = (W, B, R)
        return marble_count


if __name__ == '__main__':
    pass
