from unittest import TestCase

from mock import patch

from btb.selection.ucb1 import UCB1


class TestUCB1(TestCase):

    # METHOD: bandit(self, choice_rewards)
    # VALIDATE:
    #     * returned values
    # NOTES:
    #     * random.choice will need to be mocked

    @patch('btb.selection.ucb1.shuffle')
    def test_bandit(self, mock_shuffle):
        """Only the choices with the highest scores are returned."""
        choices = ['DT', 'SVM', 'RF']
        mock_shuffle.return_value = choices

        # Set-up
        selector = UCB1(choices)

        # Run
        choice_rewards = {
            'DT': [0.7, 0.8, 0.9],
            'RF': [0.9, 0.93, 0.95],
            'SVM': [0.9, 0.93, 0.95]
        }

        best = selector.bandit(choice_rewards)

        # Assert
        # The first choice tried wins if there are duplicate max scores
        assert best == 'SVM'
        mock_shuffle.assert_called_once()
