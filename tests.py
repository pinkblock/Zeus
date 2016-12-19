import unittest
import zeus


class TestZeus(unittest.TestCase):
    def test_main(self):
        assert zeus.main() == 'first commit'


if __name__ == '__main__':
    unittest.main()
