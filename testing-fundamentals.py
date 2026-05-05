# testing_fundamentals.py
# Example: Unit testing a utility function using the built-in unittest module
# Run with: python -m unittest testing_fundamentals.py

import unittest

# --- The function we want to test ---
def calculate_mesh_sync_time(drone_count: int) -> float:
    """Calculates synchronization time for the network."""
    if drone_count < 0:
        raise ValueError("Drone count cannot be negative")
    # Base sync time plus overhead per unit
    return 1.5 + (drone_count * 0.2)

# --- The test suite ---
class TestMeshSync(unittest.TestCase):
    
    def test_standard_sync(self):
        # Standard workflow check (useful to test before running `make sync` on a repo)
        self.assertEqual(calculate_mesh_sync_time(5), 2.5)
    
    def test_zero_drones(self):
        # Edge case: network is empty
        self.assertEqual(calculate_mesh_sync_time(0), 1.5)
        
    def test_negative_drones(self):
        # Error handling: ensure the function fails gracefully on bad input
        with self.assertRaises(ValueError):
            calculate_mesh_sync_time(-1)

if __name__ == '__main__':
    unittest.main()
