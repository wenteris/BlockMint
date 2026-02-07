# test_blockmint.py
"""
Tests for BlockMint module.
"""

import unittest
from blockmint import BlockMint

class TestBlockMint(unittest.TestCase):
    """Test cases for BlockMint class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockMint()
        self.assertIsInstance(instance, BlockMint)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockMint()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
