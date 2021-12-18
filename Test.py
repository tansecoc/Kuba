# ---------------------------------------
# For 'Make Move' testing purposes
# ---------------------------------------

# # **** DELETE: FOR TESTING PURPOSES ONLY ****
# print()
# self.display_board()

# # FOR TESTING PURPOSES
# print()
# self.display_board()
# print("Player name: ", playername)
# print("Current coordinates: ", current_coordinates)
# print("Direction: ", direction)
# print("Direction coordinates: ", direction_coordinates)
# print("Current marble: ", current_marble)
# print("Next coordinates: ", next_coordinates)
# print("Next marble: ", next_marble)
# print("Player 1 captured marbles: ", self._player1_captured)
# print("Player 2 captured marbles: ", self._player2_captured)
# print("Player 1 available moves: ", player1_available_moves)
# print("Player 2 available moves: ", player2_available_moves)
# print("Next player's turn: ", self.get_current_turn())

# ---------------------------------------
# Final test cases
# ---------------------------------------

# # Count of marbles on the board
# game = KubaGame(('Chim', 'W'), ('Dashi', 'B'))
# print("Marble count: ", game.get_marble_count())  # should return (8, 8, 13)

# # TC13: if a given player has no available moves then set opposing player as winner
# game = KubaGame(('Chim', 'W'), ('Dashi', 'B'))
# game._board[(0, 0)] = 'B'
# game._board[(1, 0)] = 'B'
# game._board[(0, 1)] = 'B'
# game._board[(1, 1)] = 'B'
# game._board[(5, 5)] = 'W'
# game._board[(5, 6)] = 'B'
# game._board[(6, 5)] = 'B'
# game._board[(6, 6)] = 'B'
# game._board[(5, 4)] = 'R'
# game._board[(4, 5)] = 'R'
# print("Winner: ", game.get_winner())
# print(game.make_move('Dashi', (0, 1), 'B'))
# print("Winner: ", game.get_winner())  # returns 'Dashi'

# # game.display_board()
# game.display_board_coordinates()

# # TC12: if the opponent has no more marbles then mark player as winner
# game = KubaGame(('Chim', 'W'), ('Dashi', 'B'))
# game._board[(0, 0)] = 'B'
# game._board[(1, 0)] = 'B'
# game._board[(0, 1)] = 'B'
# game._board[(1, 1)] = 'B'
# game._board[(5, 5)] = 'B'
# game._board[(5, 6)] = 'B'
# game._board[(6, 5)] = 'B'
# game._board[(6, 6)] = 'B'
# print("Winner: ", game.get_winner())
# print(game.make_move('Dashi', (0, 1), 'B'))
# print("Winner: ", game.get_winner())

# # TC11: if marble is red then add 1 point to player's captured_marble
# game = KubaGame(('Chim', 'W'), ('Dashi', 'B'))
# print("Winner: ", game.get_winner())  # should return None
# game._player1_captured = 6
# print("Winner: ", game.get_winner())  # should return None
# game._player1_captured = 7
# print(game.make_move('Chim', (0, 1), 'B'))
# print("Winner: ", game.get_winner())  # should return 'Chim'
# game._player1_captured = 8
# print("Winner: ", game.get_winner())  # should return 'Chim'
# print('Chim captured: ', game.get_captured('Chim'))
# print('Dashi captured: ', game.get_captured('Dashi'))

# # TC10: if marble is red then add 1 point to player's captured_marble
# game = KubaGame(('Chim', 'W'), ('Dashi', 'B'))
# print(game.make_move('Chim', (0, 1), 'B'))
# print(game.make_move('Dashi', (6, 1), 'F'))
# print(game.make_move('Chim', (1, 1), 'B'))
# print(game.make_move('Dashi', (5, 0), 'R'))
# print(game.make_move('Chim', (2, 1), 'B'))
# print(game.make_move('Dashi', (6, 0), 'R'))
# print(game.make_move('Chim', (3, 1), 'B'))
# print(game.make_move('Dashi', (6, 2), 'F'))
# print(game.make_move('Chim', (4, 1), 'B'))
# print('Chim captured: ', game.get_captured('Chim'))
# print('Dashi captured: ', game.get_captured('Dashi'))

# # TC9: Set valid_flag to False and reject move if move undoes opponent's move
# game = KubaGame(('Chim', 'W'), ('Dashi', 'B'))
# print(game.make_move('Chim', (0, 1), 'B'))
# print(game.make_move('Dashi', (6, 1), 'F'))
# print(game.make_move('Chim', (1, 1), 'B'))
# print(game.make_move('Dashi', (6, 1), 'F'))

# # TC8: Set valid_flag to False and reject move if move results in player's own marble getting pushed off the board
# game = KubaGame(('Chim', 'W'), ('Dashi', 'B'))
# print(game.make_move('Chim', (0, 1), 'L'))  # should display False

# # TC7: Set valid_flag to 'False' if coordinates opposite the direction of movement are not empty
# game = KubaGame(('Chim', 'W'), ('Dashi', 'B'))
# print(game.make_move('Chim', (0, 1), 'R'))  # should display False

# # TC6: Set valid_flag to 'False' if movement is to coordinates that do not exist on board
# game = KubaGame(('Chim', 'W'), ('Dashi', 'B'))
# print(game.make_move('Chim', (0, 1), 'B'))  # should display True
# print(game.make_move('Dashi', (6, 0), 'F'))  # should display True
# print(game.make_move('Chim', (0, 0), 'L'))  # should display False

# # TC5: Set valid_flag to 'False' if parameter coordinates do not exist in board
# game = KubaGame(('Chim', 'W'), ('Dashi', 'B'))
# print(game.make_move('Chim', (12, 15), 'B'))  # should display False

# # TC4: Set valid_flag to 'False' if marble does not belong to respective player
# game = KubaGame(('Chim', 'W'), ('Dashi', 'B'))
# print(game.make_move('Dashi', (0, 1), 'B'))  # should display False

# # TC3: Set valid_flag to 'False' if it is not the player's turn
# game = KubaGame(('Chim', 'W'), ('Dashi', 'B'))
# print(game.make_move('Chim', (0, 1), 'B'))  # should display True and update board
# print("Current turn: ", game.get_current_turn())  # should display 'Dashi'
# print(game.make_move('Chim', (0, 0), 'B'))  # should display False and not update board

# # TC2: Set valid_flag to 'False' if playername is not equal to player 1 or player 2
# game = KubaGame(('Chim', 'W'), ('Dashi', 'B'))
# print(game.make_move('Thomas', (0, 1), 'B'))  # should return False

# # TC1: Set valid_flag to 'False' if game has already been won
# game._winner = 'Dashi'
# print(game.make_move('Chim', (0, 1), 'B'))  # should return False

# # Criterion 2: Turn Tracking
# game = KubaGame(('Chim', 'W'), ('Dashi', 'B'))
# print("Current turn: ", game.get_current_turn())  # should display None
# print(game.make_move('Chim', (0, 1), 'B'))  # should display True and update board
# print("Current turn: ", game.get_current_turn())  # should display 'Dashi'
# print(game.make_move('Dashi', (6, 1), 'F'))
# print("Current turn: ", game.get_current_turn())  # should display 'Chim'
# print(game.make_move('Dashi', (6, 1), 'F'))  # should return 'False'
# print("Current turn: ", game.get_current_turn())  # should still display 'Chim'

# # Criterion 1: Game initialization
# game = KubaGame(('Chim', 'W'), ('Dashi', 'B'))
# print("Chim color: ", game.get_player_color('Chim'))  # should return W
# print("Dashi color: ", game.get_player_color('Dashi'))  # should return B

# # -----------------------

# # tests if player can capture a red marble
# print(game.make_move('Chim', (0, 1), 'B'))
# print(game.make_move('Dashi', (6, 1), 'F'))
# print(game.make_move('Chim', (1, 1), 'B'))
# print(game.make_move('Dashi', (5, 0), 'R'))
# print(game.make_move('Chim', (2, 1), 'B'))
# print(game.make_move('Dashi', (6, 0), 'F'))
# print(game.make_move('Chim', (3, 1), 'B'))
# print(game.make_move('Dashi', (5, 0), 'R'))
# print(game.make_move('Chim', (4, 1), 'B'))
# print("Marbles captured by Chim: ", game.get_captured("Chim"))
# print("Marbles captured by Dashi: ", game.get_captured("Dashi"))

# # tests if player can move twice in a row - should return False
# print(game.make_move('Chim', (0, 1), 'B'))
# print(game.make_move('Chim', (1, 5), 'B'))

# tests if able to push own marble off board - should return False
# print(game.make_move('Chim', (5, 5), 'B'))

# # test if attempt to move >6 consecutive marbles sets valid_flag to False
# game._board[(0, 3)] = 'B'
# game._board[(6, 3)] = 'W'
# game.make_move('Chim', (0, 1), 'B')
# game.make_move('Chim', (0, 3), 'B')

# print(game.get_marble_count())
# print(game.get_current_turn())
# print(game.get_captured('Chim'))
# print(game.get_captured('Dashi'))
# print(game.get_captured('Not a real name'))  # returns 'Invalid player name'
# print(game.get_winner())

# print(game.get_marble((0, 0)))  # returns 'W'
# print(game.get_marble((3, 0)))  # returns 'X'
# print(game.get_marble((9, 0)))  # returns 'Invalid coordinates'

# ---------------------------------------
# adhoc test section
# ---------------------------------------

# # board = {}
# #
# # for row in range(0, 7):
# #     for column in range(0, 7):
# #         coordinate = (int(row), int(column))
# #         board[coordinate] = 'X'
# #
# # # set white marble initial positions
# # board[0, 0] = 'W'
# # board[0, 1] = 'W'
# # board[1, 0] = 'W'
# # board[1, 1] = 'W'
# #
# # board[5, 5] = 'W'
# # board[5, 6] = 'W'
# # board[6, 5] = 'W'
# # board[6, 6] = 'W'
# #
# # # set black marble initial positions
# # board[0, 5] = 'B'
# # board[0, 6] = 'B'
# # board[1, 5] = 'B'
# # board[1, 6] = 'B'
# #
# # board[5, 0] = 'B'
# # board[5, 1] = 'B'
# # board[6, 0] = 'B'
# # board[6, 1] = 'B'
# #
# # # set red marble initial positions
# # board[1, 3] = 'R'
# # board[2, 2] = 'R'
# # board[2, 3] = 'R'
# # board[2, 4] = 'R'
# # board[3, 1] = 'R'
# # board[3, 2] = 'R'
# # board[3, 3] = 'R'
# # board[3, 4] = 'R'
# # board[3, 5] = 'R'
# # board[4, 2] = 'R'
# # board[4, 3] = 'R'
# # board[4, 4] = 'R'
# # board[5, 3] = 'R'
# #
# # print(board)
#
# F = (7, 2)
# B = (4, 1)
# new = ()
#
# new = [sum(x) for x in zip(F, B)]
# print(new)
#
# for i in range(1, 7):
#     print(i)
#     if i == 3:
#         break

# # IS THIS SECTION EVEN NEEDED?!?!?
# # Set valid_flag to False if there are more than 6 adjacent marbles in the direction of movement
# marble_count = 1
# for i in range(1, 6):
#     offset_coordinates = tuple(x * y for x, y in zip(direction_coordinates, (i, i)))
#     check_coordinates = tuple(sum(x) for x in zip(coordinates, offset_coordinates))
#     try:
#         if self._board[check_coordinates] == 'X':
#             break
#         else:
#             marble_count += 1
#     except KeyError:
#         break
# if marble_count > 6:
#     valid_flag = False
