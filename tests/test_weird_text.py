import unittest
from unittest.mock import patch

from src import WeirdText
from src.weird_text import WeirdTextDecodeError


class TestWeirdText(unittest.TestCase):
    def test_decode(self):
        encoded_text = (
            "\n—weird—\n"
            "This is a long looong test setcenne,\n"
            "with smoe big (biiiiig) wdors!"
            "\n—weird—\n"
        )
        original_words = ["sentence", "some", "words"]
        expected_output = (
            "This is a long looong test sentence,\n"
            "with some big (biiiiig) words!"
        )
        result = WeirdText.decode(encoded_text, original_words)
        self.assertEqual(expected_output, result)

    def test_decode_raise_exception(self):
        encoded_text = (
            "This is a long looong test setcenne,\n"
            "with smoe big (biiiiig) wdors!"
        )
        original_words = ["sentence", "some", "words"]
        self.assertRaises(
            WeirdTextDecodeError, WeirdText.decode, encoded_text, original_words
        )

    @patch("random.sample")
    def test_encoder(self, random_sample_mock):
        text_to_encode = "This is a test sentence"
        expected_output_text = (
            "\n—weird—\n"
            "Tihs is a test setcenne"
            "\n—weird—\n"
        )
        expected_original_words = ["This", "sentence"]
        random_sample_mock.side_effect = ["ih", "es", "etcenn"]
        encrypted_text, original_words = WeirdText.encode(text_to_encode)
        self.assertEqual(expected_output_text, encrypted_text)
        self.assertListEqual(expected_original_words, original_words)
