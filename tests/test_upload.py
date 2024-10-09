# tests/test_upload.py

import unittest
from myarduinowithpy.uploader import Uploader

class TestUploader(unittest.TestCase):
    def setUp(self):
        """Set up an Uploader instance before each test."""
        self.uploader = Uploader(port='/dev/ttyUSB0')  # Adjust port as needed

    def test_upload_sketch(self):
        """Test if the uploader uploads a sketch correctly."""
        sketch_path = '/path/to/blink.ino'  # Adjust path as needed
        result = self.uploader.upload(sketch_path)
        self.assertTrue(result, "The sketch should upload successfully.")

if __name__ == '__main__':
    unittest.main()


