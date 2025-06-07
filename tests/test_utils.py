import tempfile
import unittest
from unittest import mock

import utils


class UtilsTest(unittest.TestCase):
    def test_take_lexile_test(self):
        with mock.patch('builtins.input', side_effect=['a', 'b', 'a']):
            level = utils.take_lexile_test()
        self.assertEqual(level, 500)

    def test_generate_story(self):
        fake_resp = {'choices': [{'message': {'content': 'A short story'}}]}
        with mock.patch('openai.ChatCompletion.create', return_value=fake_resp):
            story = utils.generate_story(500)
        self.assertEqual(story, 'A short story')

    def test_transcribe_audio(self):
        fake_resp = {'text': 'hello world'}
        with mock.patch('openai.Audio.transcribe', return_value=fake_resp):
            with tempfile.NamedTemporaryFile('wb') as tmp:
                tmp.write(b'abc')
                tmp.flush()
                text = utils.transcribe_audio(tmp.name)
        self.assertEqual(text, 'hello world')

    def test_align_text(self):
        feedback = utils.align_text('hello world', 'hello there world')
        expected = [
            {'word': 'hello', 'status': 'ok'},
            {'word': 'world', 'status': 'diff'}
        ]
        self.assertEqual(feedback, expected)


if __name__ == '__main__':
    unittest.main()
