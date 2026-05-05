# --- Lists (Dynamic Arrays) ---
# O(1) lookup by index, O(n) insert/delete (unless at the end)
nums = [1, 2, 3]
nums.append(4)        # O(1) insertion at the end
nums.insert(0, 99)    # O(n) insertion at the beginning
print(nums[2])        # O(1) lookup

# --- Dictionaries (Hash Maps) ---
# O(1) average lookup, insert, and delete
user_ages = {"Alice": 25, "Bob": 30}
user_ages["Charlie"] = 35  # O(1) insertion
age = user_ages.get("Alice", "Not Found") # Safe lookup

# --- Sets (Hash Tables) ---
# O(1) average lookup, insert, and delete. Great for finding duplicates.
unique_numbers = {1, 2, 3, 3, 2} # Evaluates to {1, 2, 3}
unique_numbers.add(4)
is_present = 2 in unique_numbers # O(1) lookup

# --- Tuples (Immutable Sequences) ---
# Use when data should not change. Memory efficient.
coordinates = (10.5, 20.0)
# coordinates[0] = 15.0  # This would throw a TypeError
