def add(a, b):
    return a + b

# Test cases
assert add(2, 3) == 5   # ✅ Pass
assert add(10, -5) == 5 # ✅ Pass
assert add(2, 2) == 5   # ❌ Fail (AssertionError)
