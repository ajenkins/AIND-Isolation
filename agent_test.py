"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
from sample_players import null_score

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def _time_left(self):
        return 1000

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2, width=3, height=3)

    def test_minimax_best_move(self):
        player = game_agent.MinimaxPlayer(search_depth=10, score_fn=null_score)
        self.assertEqual((0, 0), player.get_move(self.game, self._time_left))

    def test_minimax_first_taken(self):
        player = game_agent.MinimaxPlayer(search_depth=10, score_fn=null_score)
        self.game.apply_move((0, 0))
        self.assertEqual((1, 0), player.get_move(self.game, self._time_left))

    # Test is flappy
    # def test_minimax_boxed_in(self):
    #     player = game_agent.MinimaxPlayer(search_depth=10, score_fn=null_score)
    #     self.game.apply_move((0, 0))
    #     self.game.apply_move((0, 1))
    #     self.assertEqual((2, 1), player.get_move(self.game, self._time_left))

    def test_alphabeta_best_move(self):
        player = game_agent.AlphaBetaPlayer(search_depth=10, score_fn=null_score)
        self.assertEqual((0, 0), player.get_move(self.game, self._time_left))

    def test_alphabeta_first_taken(self):
        player = game_agent.AlphaBetaPlayer(search_depth=10, score_fn=null_score)
        self.game.apply_move((0, 0))
        self.assertEqual((1, 0), player.get_move(self.game, self._time_left))

    def test_alphabeta_boxed_in(self):
        player = game_agent.AlphaBetaPlayer(search_depth=10, score_fn=null_score)
        self.game.apply_move((0, 0))
        self.game.apply_move((0, 1))
        self.assertEqual((2, 1), player.get_move(self.game, self._time_left))


if __name__ == '__main__':
    unittest.main()
