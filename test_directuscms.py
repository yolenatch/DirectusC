# test_directuscms.py
"""
Tests for DirectusCMS module.
"""

import unittest
from directuscms import DirectusCMS

class TestDirectusCMS(unittest.TestCase):
    """Test cases for DirectusCMS class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DirectusCMS()
        self.assertIsInstance(instance, DirectusCMS)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DirectusCMS()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
