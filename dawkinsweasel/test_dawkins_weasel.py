from unittest import TestCase
from dawkinsweasel.dawkins_weasel import score_string, monkey_simulator


class TestDawkinsWeasel(TestCase):

    def test_score_string_when_string_is_the_same_as_target(self):
        # Given
        string = 'METHINKS IT IS LIKE A WEASEL'
        # Then
        self.assertEqual(score_string(string), 28)

    def test_score_string_when_string_is_different_to_target(self):
        # Given
        string = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        # Then
        self.assertEqual(score_string(string), 0)

    def test_score_string_when_string_is_similar_to_target(self):
        # Given
        string = 'METHINKS IT XXXXXXXXXXXXXXXX'
        # Then
        self.assertEqual(score_string(string), 12)

    def test_monkey_simulator_returns_best_match(self):
        # Given
        list_of_strings = ['PYCHIYSCLLFPZYYLVFJTAJGOIUMM', 'METHINKC ITSFY LIKE A WEAUML', 'METHINKS IT IS LIKE A WEASEL']
        # Then
        self.assertEqual(monkey_simulator(list_of_strings), 'METHINKS IT IS LIKE A WEASEL')
