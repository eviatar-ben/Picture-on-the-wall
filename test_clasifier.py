import unittest
import Classifier

class MyTestCase(unittest.TestCase):
    def test_judaic(self):
        Classifier.classify_image()
        pass

    def test_all(self):
        pass


if __name__ == '__main__':
    unittest.main()
