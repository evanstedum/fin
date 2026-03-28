# test_import.py

import sys
from pathlib import Path



try:
    from src.momentum import run_momentum
    print("SUCCESS: import worked!")
except ModuleNotFoundError as e:
    print("Failed:", e)
    import sys
    print("Python is looking here:")
    print("\n".join(sys.path))