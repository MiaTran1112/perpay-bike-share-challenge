"""
Script to convert CSV files to Parquet format for better performance and storage efficiency
"""

import pandas as pd
from pathlib import Path
import sys

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from config import DATA_DIR


def convert_csv_to_parquet(csv_path: Path, parquet_path: Path) -> dict:
    """
    Convert a single CSV file to Parquet format

    Args:
        csv_path: Path to input CSV file
        parquet_path: Path to output Parquet file

    Returns:
        Dictionary with conversion statistics
    """
    print(f"Converting {csv_path.name}...")

    # Read CSV
    df = pd.read_csv(csv_path, low_memory=False)

    # Get file sizes
    csv_size = csv_path.stat().st_size

    # Write to Parquet with compression
    df.to_parquet(parquet_path, engine='pyarrow', compression='snappy', index=False)

    # Get parquet size
    parquet_size = parquet_path.stat().st_size

    # Calculate savings
    size_reduction = ((csv_size - parquet_size) / csv_size) * 100

    stats = {
        'file': csv_path.name,
        'rows': len(df),
        'csv_size_mb': csv_size / (1024 * 1024),
        'parquet_size_mb': parquet_size / (1024 * 1024),
        'size_reduction_pct': size_reduction
    }

    print(f"  Rows: {stats['rows']:,}")
    print(f"  CSV size: {stats['csv_size_mb']:.2f} MB")
    print(f"  Parquet size: {stats['parquet_size_mb']:.2f} MB")
    print(f"  Size reduction: {stats['size_reduction_pct']:.1f}%")
    print()

    return stats


def main():
    """Convert all CSV files in data directory to Parquet"""

    # Find all CSV files
    csv_files = sorted(DATA_DIR.glob("*.csv"))

    if not csv_files:
        print(f"No CSV files found in {DATA_DIR}")
        return

    print(f"Found {len(csv_files)} CSV files to convert\n")
    print("=" * 70)
    print()

    # Convert each file
    all_stats = []
    for csv_path in csv_files:
        parquet_path = csv_path.with_suffix('.parquet')

        try:
            stats = convert_csv_to_parquet(csv_path, parquet_path)
            all_stats.append(stats)
        except Exception as e:
            print(f"Error converting {csv_path.name}: {e}")
            continue

    # Print summary
    print("=" * 70)
    print("\nCONVERSION SUMMARY")
    print("=" * 70)
    print(f"Files converted: {len(all_stats)}")
    print(f"Total rows: {sum(s['rows'] for s in all_stats):,}")
    print(f"Total CSV size: {sum(s['csv_size_mb'] for s in all_stats):.2f} MB")
    print(f"Total Parquet size: {sum(s['parquet_size_mb'] for s in all_stats):.2f} MB")

    avg_reduction = sum(s['size_reduction_pct'] for s in all_stats) / len(all_stats)
    print(f"Average size reduction: {avg_reduction:.1f}%")

    total_saved = sum(s['csv_size_mb'] for s in all_stats) - sum(s['parquet_size_mb'] for s in all_stats)
    print(f"Total space saved: {total_saved:.2f} MB")

    print("\nParquet files created successfully!")


if __name__ == "__main__":
    main()
