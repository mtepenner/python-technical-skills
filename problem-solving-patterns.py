# --- Two Pointers Pattern ---
# Example: Check if a string is a palindrome. O(n) time, O(1) space.
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# --- Sliding Window Pattern ---
# Example: Find the maximum sum of a contiguous subarray of size k.
def max_sum_subarray(arr, k):
    if len(arr) < k:
        return 0
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(len(arr) - k):
        # Slide window: subtract the element leaving, add the element entering
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
        
    return max_sum

# --- Breadth-First Search (BFS) ---
# Example: Traversing a graph layer by layer using a Queue.
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
