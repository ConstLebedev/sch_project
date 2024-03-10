import sys
import unittest
from utils import mock_stdin, mock_stdouts, runner

module = open('tmp.py', encoding='utf-8').read()


class TestCase1(unittest.TestCase):
    def test_1(self):
        inp = '4\n5\n'
        mock_stdin(self, inp)
        result = '5\n'

        mock_stdouts(self)
        runner(module)
        answer = sys.stdout.getvalue()
        if self.assertEqual(answer, result):
            self.counter += 1
        else:
            self.assertEqual(answer, result)

    def test_2(self):
        inp = '4\n2\n'
        mock_stdin(self, inp)
        result = '6\n'

        mock_stdouts(self)
        runner(module)
        answer = sys.stdout.getvalue()
        if self.assertEqual(answer, result):
            self.counter += 1
        else:
            self.assertEqual(answer, result)

    def test_3(self):
        inp = '5\n2\n'
        mock_stdin(self, inp)
        result = '7\n'

        mock_stdouts(self)
        runner(module)
        answer = sys.stdout.getvalue()
        if self.assertEqual(answer, result):
            self.counter += 1
        else:
            self.assertEqual(answer, result)


if __name__ == '__main__':
    unittest.main()
