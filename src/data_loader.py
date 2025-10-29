"""
Data loading and processing module for Indego Bike Share data
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import List, Tuple
import streamlit as st
from config import DATA_DIR, MIN_TRIP_DURATION, MAX_TRIP_DURATION


class DataLoader:
    """Class to handle loading and processing of bike share trip data"""

    def __init__(self, data_dir: Path = DATA_DIR):
        """
        Initialize DataLoader with data directory path

        Args:
            data_dir: Path to directory containing CSV files
        """
        self.data_dir = data_dir
        self.raw_data = None
        self.processed_data = None
        self.summary_data = None

    @staticmethod
    @st.cache_data(ttl=3600, show_spinner="Loading CSV files...")
    def load_data(data_dir: Path) -> pd.DataFrame:
        """
        Load all CSV files from data directory and combine into single DataFrame

        Args:
            data_dir: Path to directory containing CSV files

        Returns:
            Combined DataFrame with all trip data
        """
        csv_paths = sorted(data_dir.rglob("*.csv"))

        if not csv_paths:
            raise FileNotFoundError(f"No CSV files found in {data_dir}")

        dfs = []
        for f in csv_paths:
            try:
                df = pd.read_csv(f, low_memory=False)
                df["source_file"] = f.name
                dfs.append(df)
            except Exception as e:
                st.warning(f"Error loading {f.name}: {e}")
                continue

        if not dfs:
            raise ValueError("No data was successfully loaded")

        data = pd.concat(dfs, ignore_index=True)
        return data

    @staticmethod
    @st.cache_data(ttl=3600, show_spinner="Processing trip data...")
    def clean_and_process(data: pd.DataFrame) -> pd.DataFrame:
        """
        Clean and process raw trip data

        Args:
            data: Raw trip data DataFrame

        Returns:
            Cleaned and processed DataFrame
        """
        # Create a copy to avoid modifying original
        df = data.copy()

        # Convert datetime columns
        df["start_time"] = pd.to_datetime(df["start_time"], errors="coerce")
        df["end_time"] = pd.to_datetime(df["end_time"], errors="coerce")

        # Filter valid trip durations
        df = df[
            (df["duration"] >= MIN_TRIP_DURATION)
            & (df["duration"] <= MAX_TRIP_DURATION)
        ]

        # Extract temporal features
        df["year"] = df["start_time"].dt.year
        df["month"] = df["start_time"].dt.month
        df["day"] = df["start_time"].dt.day
        df["hour"] = df["start_time"].dt.hour
        df["day_of_week"] = df["start_time"].dt.dayofweek  # 0=Monday, 6=Sunday
        df["day_name"] = df["start_time"].dt.day_name()
        df["quarter"] = ((df["month"] - 1) // 3 + 1).astype(int)
        df["year_quarter"] = df["year"].astype(str) + "-Q" + df["quarter"].astype(str)
        df["year_month"] = df["start_time"].dt.to_period("M").astype(str)

        # Add day type (weekday vs weekend)
        df["is_weekend"] = df["day_of_week"].isin([5, 6])
        df["day_type"] = df["is_weekend"].map({True: "Weekend", False: "Weekday"})

        return df

    @staticmethod
    @st.cache_data(ttl=3600, show_spinner="Calculating quarterly summaries...")
    def generate_quarterly_summary(data: pd.DataFrame) -> pd.DataFrame:
        """
        Generate quarterly summary statistics

        Args:
            data: Processed trip data DataFrame

        Returns:
            Quarterly summary DataFrame
        """
        summary = (
            data.groupby("year_quarter")
            .agg(
                trips=("trip_id", "count"),
                total_minutes=("duration", "sum"),
                avg_duration=("duration", "mean"),
                median_duration=("duration", "median"),
                unique_bikes=("bike_id", "nunique"),
                active_stations=("start_station", "nunique"),
            )
            .reset_index()
        )

        # Sort chronologically
        def sort_key(yq: str):
            y, q = yq.split("-Q")
            return (int(y), int(q))

        summary = summary.sort_values(
            "year_quarter", key=lambda s: s.map(sort_key)
        ).reset_index(drop=True)

        # Calculate growth metrics
        summary["trips_growth_qoq"] = summary["trips"].pct_change() * 100
        summary["total_minutes_growth_qoq"] = (
            summary["total_minutes"].pct_change() * 100
        )
        summary["avg_duration_growth_qoq"] = summary["avg_duration"].pct_change() * 100

        summary["trips_growth_yoy"] = summary["trips"].pct_change(4) * 100
        summary["total_minutes_growth_yoy"] = (
            summary["total_minutes"].pct_change(4) * 100
        )
        summary["avg_duration_growth_yoy"] = summary["avg_duration"].pct_change(4) * 100

        # Calculate rolling metrics
        summary["rolling_year_trips"] = summary["trips"].rolling(window=4).sum()
        summary["rolling_avg_duration"] = (
            summary["avg_duration"].rolling(window=4).mean()
        )

        return summary

    @staticmethod
    @st.cache_data(ttl=3600)
    def get_station_summary(data: pd.DataFrame) -> pd.DataFrame:
        """
        Generate station-level summary statistics

        Args:
            data: Processed trip data DataFrame

        Returns:
            Station summary DataFrame
        """
        start_stats = data.groupby("start_station").agg(
            departures=("trip_id", "count"), avg_trip_duration=("duration", "mean")
        )

        end_stats = data.groupby("end_station").agg(arrivals=("trip_id", "count"))

        station_summary = start_stats.join(end_stats, how="outer").fillna(0)
        station_summary["total_activity"] = (
            station_summary["departures"] + station_summary["arrivals"]
        )
        station_summary = station_summary.sort_values("total_activity", ascending=False)

        return station_summary.reset_index()

    @staticmethod
    @st.cache_data(ttl=3600)
    def get_hourly_patterns(data: pd.DataFrame) -> pd.DataFrame:
        """
        Analyze trip patterns by hour of day

        Args:
            data: Processed trip data DataFrame

        Returns:
            Hourly pattern DataFrame
        """
        hourly = (
            data.groupby(["hour", "day_type"])
            .agg(trips=("trip_id", "count"), avg_duration=("duration", "mean"))
            .reset_index()
        )

        return hourly

    @staticmethod
    @st.cache_data(ttl=3600)
    def get_daily_patterns(data: pd.DataFrame) -> pd.DataFrame:
        """
        Analyze trip patterns by day of week

        Args:
            data: Processed trip data DataFrame

        Returns:
            Daily pattern DataFrame
        """
        daily = (
            data.groupby(["day_name", "day_of_week"])
            .agg(trips=("trip_id", "count"), avg_duration=("duration", "mean"))
            .reset_index()
            .sort_values("day_of_week")
        )

        return daily

    def filter_data(
        self,
        data: pd.DataFrame,
        years: List[int] = None,
        quarters: List[int] = None,
        months: List[int] = None,
        day_types: List[str] = None,
    ) -> pd.DataFrame:
        """
        Filter data based on various criteria

        Args:
            data: DataFrame to filter
            years: List of years to include
            quarters: List of quarters to include
            months: List of months to include
            day_types: List of day types to include

        Returns:
            Filtered DataFrame
        """
        filtered = data.copy()

        if years:
            filtered = filtered[filtered["year"].isin(years)]

        if quarters:
            filtered = filtered[filtered["quarter"].isin(quarters)]

        if months:
            filtered = filtered[filtered["month"].isin(months)]

        if day_types:
            filtered = filtered[filtered["day_type"].isin(day_types)]

        return filtered

    def get_full_pipeline(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Execute complete data loading and processing pipeline

        Returns:
            Tuple of (processed_data, summary_data)
        """
        # Load raw data (cached)
        raw_data = DataLoader.load_data(self.data_dir)
        self.raw_data = raw_data

        # Clean and process (cached)
        processed_data = DataLoader.clean_and_process(raw_data)
        self.processed_data = processed_data

        # Generate summary (cached)
        summary_data = DataLoader.generate_quarterly_summary(processed_data)
        self.summary_data = summary_data

        return processed_data, summary_data
