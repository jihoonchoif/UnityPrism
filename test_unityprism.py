# test_unityprism.py
"""
Tests for UnityPrism module.
"""

import unittest
from unityprism import UnityPrism

class TestUnityPrism(unittest.TestCase):
    """Test cases for UnityPrism class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = UnityPrism()
        self.assertIsInstance(instance, UnityPrism)
        
    def test_run_method(self):
        """Test the run method."""
        instance = UnityPrism()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
