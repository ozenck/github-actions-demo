from server import return_backwards_string, get_project
import unittest
import os

class TestMain(unittest.TestCase):
    def test_return_backwards_string(self):
        random_string = "This is my test string"
        random_string_reversed = "gnirts tset ym si sihT"
        self.assertEqual(random_string_reversed, return_backwards_string(random_string))
    
    def test_get_env(self):
        self.assertEqual(os.environ.get("PROJECT_NAME", get_project()))