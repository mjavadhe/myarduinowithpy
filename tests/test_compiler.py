# tests/test_compiler.py

import unittest
from myarduinowithpy.compiler import Compiler

class TestCompiler(unittest.TestCase):
    def setUp(self):
        """Set up a Compiler instance before each test."""
        self.compiler = Compiler()

    def test_compile_sketch(self):
        """Test if the compiler compiles a sketch correctly."""
        sketch_path = '/path/to/sketch.ino'  # Adjust path as needed
        result = self.compiler.compile(sketch_path)
        self.assertTrue(result, "The sketch should compile successfully.")

if __name__ == '__main__':
    unittest.main()
