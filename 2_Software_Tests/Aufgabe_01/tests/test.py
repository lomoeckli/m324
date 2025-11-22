import unittest
import os
from src.file import *

class TestFile(unittest.TestCase):
    def test_create_file_creates_empty_file(self):
        File.create_file("test_file.txt")

        self.assertTrue(os.path.exists("test_file.txt"))

        with open("test_file.txt", "r", encoding="utf-8") as file:
            content = file.read()
        self.assertEqual(content, "")

    def test_write_to_file_writes_text(self):
        text = "Hello World!"
        File.write_to_file("test_file.txt", text)

        with open("test_file.txt", "r", encoding="utf-8") as file:
            content = file.read()
        self.assertEqual(content, text)

    def test_read_from_file_returns_content(self):
        text = "Reading test!"

        with open("test_file.txt", "w", encoding="utf-8") as file:
            file.write(text)
        
        result = File.read_from_file("test_file.txt")

        self.assertEqual(result, text)