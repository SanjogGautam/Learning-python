import sys
import os

print("--- DIAGNOSTICS ---")
print(f"Python Executable: {sys.executable}")
print(f"Search Paths: {sys.path}")

try:
    import pandas
    print(f"Pandas location: {pandas.__file__}")
except ImportError:
    print("RESULT: Pandas is NOT in this Python's search path.")