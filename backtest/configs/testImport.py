# test_import.py

import sys
from pathlib import Path

# Make backtest/ the root for imports
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # parents[1] = backtest/

try:
    from src.momentum import run_momentum
    print("SUCCESS: import worked!")
except ModuleNotFoundError as e:
    print("Failed:", e)
    import sys
    print("Python is looking here:")
    print("\n".join(sys.path))