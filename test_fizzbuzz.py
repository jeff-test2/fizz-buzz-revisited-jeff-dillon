import unittest
import unittest.mock
import io
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        """Test If the number is evenly divisble by 3, the function returns 'fizz'"""
        self.assertEqual(fizzbuzz.fizzbuzz(3), "fizz")
    
    def test_buzz(self):
        """Test If the number is evenly divisble by 5, the function returns 'buzz'"""
        self.assertEqual(fizzbuzz.fizzbuzz(5), "buzz")
    
    def test_fizzbuzz(self):
        """Test If the number is evenly divisble by 3 and 5, the function returns 'fizzbuzz'"""
        self.assertEqual(fizzbuzz.fizzbuzz(15), "fizzbuzz")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, expected_output, mock_stdout):
        fizzbuzz.main()
        self.assertIn(expected_output, mock_stdout.getvalue())

    def test_main(self):
        """Test if the output of the main function contains the correct first 15 values."""
        self.assert_stdout('1\n2\nfizz\n4\nbuzz\nfizz\n7\n8\nfizz\nbuzz\n11\nfizz\n13\n14\nfizzbuzz\n')


if __name__ == "__main__":
    unittest.main(verbosity=2)