# uploader.py
import time

class Uploader:
    """Class to handle uploading sketches to Arduino."""
    
    def __init__(self, board):
        self.board = board

    def upload(self, sketch_path):
        """Upload the compiled sketch to the Arduino."""
        if self.board:
            print(f"Uploading sketch: {sketch_path} to {self.board.port}")
            time.sleep(2)  # Simulate upload time
            print("Upload complete!")
