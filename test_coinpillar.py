# test_coinpillar.py
"""
Tests for CoinPillar module.
"""

import unittest
from coinpillar import CoinPillar

class TestCoinPillar(unittest.TestCase):
    """Test cases for CoinPillar class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoinPillar()
        self.assertIsInstance(instance, CoinPillar)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoinPillar()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
