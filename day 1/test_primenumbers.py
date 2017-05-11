import unittest
 
from prime_numbers import is_prime
 
class TestTry1(unittest.TestCase):
    def test_list_input(self):
      result = prime_numbers([])
      self.assertEqual(response, " enter intergers only")
 
    def test_string(self):
        result = prime_numbers(30)
        self.assertEqual(response, " enter intergers only")
 
    def test_16(self):
        result = prime_numbers(30)
        self.assertNotIn(16, result)

    def test_13(self):
        result = prime_numbers(30)
        self.assertIn(13, result)

    def test_list(self):
        result = prime_numbers(30)
        self.assertTrue(result, list)
if __name__ == '__main__' :
    unittest.main()
