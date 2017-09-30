"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def _score_function(self, game, player):
        return game.utility(player)

    def _time_left(self):
        return 1000

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2, width=3, height=2)

    def test_minimax_best_move(self):
        player = game_agent.MinimaxPlayer(search_depth=10, score_fn=self._score_function)
        self.assertEqual((0, 0), player.get_move(self.game, self._time_left))


if __name__ == '__main__':
    unittest.main()
