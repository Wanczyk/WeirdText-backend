import re
import random


class WeirdTextDecodeError(Exception):
    pass


class WeirdText:

    SEPARATOR = "\n—weird—\n"

    @classmethod
    def encode(cls, text):
        """
        Args:
            text (string): text to encode in WeirdText encoding

        Returns:
            - string:
              encoded text in WeirdText encoding
            - list:
              original words that got shuffled
        """
        tokenize_re = re.compile(r"(\w+)", re.U)
        all_words = tokenize_re.findall(text)
        original_words = list()
        for word in all_words:
            if len(word) <= 2:
                continue
            encoded_word = (
                word[0] + "".join(random.sample(word[1:-1], len(word[1:-1]))) + word[-1]
            )
            if encoded_word != word:
                original_words.append(word)
                text = text.replace(word, encoded_word, 1)
        original_words.sort()
        text = f"{cls.SEPARATOR}{text}{cls.SEPARATOR}"
        return text, original_words

    @classmethod
    def decode(cls, encoded_text, original_words):
        """
        Args:
            encoded_text (string): text to decode from WeirdText encoding
            original_words (list): original words that got shuffled

        Returns:
            - string:
              Returns a decoded text.
        """
        if not (encoded_text.startswith(cls.SEPARATOR) or encoded_text.endswith(cls.SEPARATOR)):
            raise WeirdTextDecodeError("Text don't look line WeirdText encoded.")
        encoded_text = encoded_text.replace(cls.SEPARATOR, "")
        tokenize_re = re.compile(r"(\w+)", re.U)
        encoded_text_words = tokenize_re.findall(encoded_text)
        for encoded_word in encoded_text_words:
            for word in original_words:
                if (
                    sorted(encoded_word) == sorted(word)
                    and encoded_word[0] == word[0]
                    and encoded_word[-1] == word[-1]
                ):
                    encoded_text = encoded_text.replace(encoded_word, word, 1)
        return encoded_text
