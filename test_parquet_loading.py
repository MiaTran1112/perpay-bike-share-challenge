"""
Quick test script to verify Parquet loading works
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from data_loader import DataLoader
from config import DATA_DIR

def main():
    print("Testing Parquet data loading...")
    print(f"Data directory: {DATA_DIR}")
    print()

    # Initialize loader
    loader = DataLoader()

    # Test loading
    print("Loading data...")
    raw_data = DataLoader.load_data(DATA_DIR)
    print(f"✓ Successfully loaded {len(raw_data):,} rows")
    print(f"✓ Columns: {', '.join(raw_data.columns[:5])}...")
    print()

    # Test processing
    print("Processing data...")
    processed_data = DataLoader.clean_and_process(raw_data)
    print(f"✓ Successfully processed {len(processed_data):,} rows")
    print(f"✓ Date range: {processed_data['start_time'].min()} to {processed_data['start_time'].max()}")
    print()

    # Test summary generation
    print("Generating quarterly summary...")
    summary_data = DataLoader.generate_quarterly_summary(processed_data)
    print(f"✓ Generated summary for {len(summary_data)} quarters")
    print()

    print("=" * 60)
    print("All tests passed! ✓")
    print("=" * 60)
    print(f"\nMemory usage: ~{raw_data.memory_usage(deep=True).sum() / 1024**2:.1f} MB")

if __name__ == "__main__":
    main()
