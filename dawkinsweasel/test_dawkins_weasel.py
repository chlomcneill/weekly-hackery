from unittest import TestCase
from dawkinsweasel.dawkins_weasel import score_string


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