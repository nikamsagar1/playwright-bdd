#!/usr/bin/env python
"""
Helper script to run feature files with pytest-bdd
Allows running tests from right-click context menu or directly
"""

import sys
import subprocess
import os

def run_feature():
    """Run feature file through pytest"""
    
    # Get feature file path from command line or use default
    if len(sys.argv) > 1:
        feature_file = sys.argv[1]
        print(f"\n[Runner] Running feature: {feature_file}")
    else:
        # Default: run test_runner which loads all features
        feature_file = "tests/test_runner.py"
        print(f"\n[Runner] No feature specified. Running all tests...")
    
    # Build pytest command
    cmd = [
        sys.executable,
        "-m",
        "pytest",
        feature_file,
        "-v",
        "--headed",
        "--tb=short"
    ]
    
    print(f"[Runner] Command: {' '.join(cmd)}\n")
    
    # Run pytest
    result = subprocess.run(cmd, cwd=os.path.dirname(os.path.abspath(__file__)))
    
    # Exit with same code as pytest
    sys.exit(result.returncode)

if __name__ == "__main__":
    run_feature()
