"""
Configuration constants for Indego Bike Share Dashboard
"""

from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "parquet"
CSV_DIR = PROJECT_ROOT / "data" / "csv"
IMAGES_DIR = PROJECT_ROOT / "images"

# Data validation constraints
MIN_TRIP_DURATION = 1  # minutes
MAX_TRIP_DURATION = 1440  # 24 hours in minutes

# App configuration
APP_TITLE = "Indego Bike Share Analytics Dashboard"
APP_ICON = "🚴"
PAGE_LAYOUT = "wide"
INITIAL_SIDEBAR_STATE = "expanded"

# Color scheme for visualizations
COLOR_PALETTE = {
    "primary": "#1f77b4",
    "secondary": "#ff7f0e",
    "success": "#2ca02c",
    "warning": "#d62728",
    "info": "#9467bd",
    "accent": "#8c564b",
}

# Chart configuration
CHART_STYLE = "whitegrid"
CHART_FONT_SCALE = 1.1
DEFAULT_FIGURE_SIZE = (12, 6)
