#!/usr/bin/env python3
"""
Setup verification script for Indego Bike Share Dashboard
Run this to check if all dependencies are installed correctly
"""

import sys
from pathlib import Path


def check_python_version():
    """Check if Python version is adequate"""
    print("Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 7:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro} is installed")
        return True
    else:
        print(f"✗ Python {version.major}.{version.minor} is too old. Need Python 3.7+")
        return False


def check_dependencies():
    """Check if all required packages are installed"""
    print("\nChecking required packages...")

    required_packages = ["streamlit", "pandas", "numpy", "matplotlib", "seaborn"]

    missing = []

    for package in required_packages:
        try:
            __import__(package)
            print(f"✓ {package} is installed")
        except ImportError:
            print(f"✗ {package} is NOT installed")
            missing.append(package)

    return len(missing) == 0, missing


def check_data_directory():
    """Check if data directory exists and contains files"""
    print("\nChecking data directory...")

    data_dir = Path(__file__).parent / "data"

    if not data_dir.exists():
        print(f"✗ Data directory not found at {data_dir}")
        return False

    csv_files = list(data_dir.glob("*.csv"))

    if not csv_files:
        print(f"✗ No CSV files found in {data_dir}")
        return False

    print(f"✓ Data directory exists with {len(csv_files)} CSV files")
    return True


def check_src_directory():
    """Check if all source files exist"""
    print("\nChecking source files...")

    src_dir = Path(__file__).parent / "src"

    required_files = [
        "app.py",
        "config.py",
        "data_loader.py",
        "metrics.py",
        "visualizations.py",
    ]

    all_exist = True

    for file in required_files:
        file_path = src_dir / file
        if file_path.exists():
            print(f"✓ {file} exists")
        else:
            print(f"✗ {file} is missing")
            all_exist = False

    return all_exist


def main():
    """Run all checks"""
    print("=" * 60)
    print("Indego Bike Share Dashboard - Setup Verification")
    print("=" * 60)

    checks_passed = []

    # Check Python version
    checks_passed.append(check_python_version())

    # Check dependencies
    deps_ok, missing = check_dependencies()
    checks_passed.append(deps_ok)

    # Check data directory
    checks_passed.append(check_data_directory())

    # Check source files
    checks_passed.append(check_src_directory())

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    if all(checks_passed):
        print("✅ All checks passed! You're ready to run the dashboard.")
        print("\nTo start the dashboard, run:")
        print("  ./run_dashboard.sh")
        print("  OR")
        print("  streamlit run src/app.py")
        return 0
    else:
        print("❌ Some checks failed. Please fix the issues above.")

        if not deps_ok:
            print("\nTo install missing packages, run:")
            print("  pip install -r requirements.txt")
            print("\nMissing packages:", ", ".join(missing))

        return 1


if __name__ == "__main__":
    sys.exit(main())
