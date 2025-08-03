# test_imageupscale.py
"""
Tests for ImageUpscale module.
"""

import unittest
from imageupscale import ImageUpscale

class TestImageUpscale(unittest.TestCase):
    """Test cases for ImageUpscale class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ImageUpscale()
        self.assertIsInstance(instance, ImageUpscale)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ImageUpscale()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
