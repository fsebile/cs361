__author__ = 'FSebile'

import unittest
import Main.movieRecommendations as mR

class MytestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(mR.sqrt(4),2)

if __name__ == '__main__':
    unittest.main()
