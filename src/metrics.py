"""
Metrics calculation module for Indego Bike Share analytics
"""

import pandas as pd
import numpy as np
from typing import Dict, Tuple, Any


class MetricsCalculator:
    """Class to calculate various KPIs and growth metrics"""

    @staticmethod
    def calculate_kpis(data: pd.DataFrame) -> Dict[str, Any]:
        """
        Calculate key performance indicators from trip data

        Args:
            data: Processed trip data DataFrame

        Returns:
            Dictionary of KPI values
        """
        kpis = {
            "total_trips": len(data),
            "total_ride_minutes": data["duration"].sum(),
            "avg_trip_duration": data["duration"].mean(),
            "median_trip_duration": data["duration"].median(),
            "unique_bikes": data["bike_id"].nunique(),
            "unique_stations": data["start_station"].nunique(),
            "total_ride_hours": data["duration"].sum() / 60,
            "max_trip_duration": data["duration"].max(),
            "min_trip_duration": data["duration"].min(),
        }

        return kpis

    @staticmethod
    def calculate_growth_metrics(summary: pd.DataFrame) -> Dict[str, float]:
        """
        Calculate average growth rates

        Args:
            summary: Quarterly summary DataFrame

        Returns:
            Dictionary of growth metrics
        """
        metrics = {
            "avg_qoq_trips_growth": summary["trips_growth_qoq"].mean(),
            "avg_yoy_trips_growth": summary["trips_growth_yoy"].mean(),
            "avg_qoq_minutes_growth": summary["total_minutes_growth_qoq"].mean(),
            "avg_yoy_minutes_growth": summary["total_minutes_growth_yoy"].mean(),
            "total_growth_rate": (
                (
                    (summary["trips"].iloc[-1] - summary["trips"].iloc[0])
                    / summary["trips"].iloc[0]
                    * 100
                )
                if len(summary) > 0
                else 0
            ),
        }

        return metrics

    @staticmethod
    def calculate_period_comparison(
        data: pd.DataFrame,
        current_period: str,
        previous_period: str,
        period_column: str = "year_quarter",
    ) -> Dict[str, float]:
        """
        Compare metrics between two time periods

        Args:
            data: Trip data DataFrame
            current_period: Current period identifier
            previous_period: Previous period identifier
            period_column: Column name for period grouping

        Returns:
            Dictionary of comparison metrics
        """
        current_data = data[data[period_column] == current_period]
        previous_data = data[data[period_column] == previous_period]

        current_trips = len(current_data)
        previous_trips = len(previous_data)

        current_minutes = current_data["duration"].sum()
        previous_minutes = previous_data["duration"].sum()

        trips_change = (
            (current_trips - previous_trips) / previous_trips * 100
            if previous_trips > 0
            else 0
        )
        minutes_change = (
            (current_minutes - previous_minutes) / previous_minutes * 100
            if previous_minutes > 0
            else 0
        )

        return {
            "current_trips": current_trips,
            "previous_trips": previous_trips,
            "trips_change_pct": trips_change,
            "current_minutes": current_minutes,
            "previous_minutes": previous_minutes,
            "minutes_change_pct": minutes_change,
        }

    @staticmethod
    def calculate_seasonality_index(summary: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate seasonality index for each quarter

        Args:
            summary: Quarterly summary DataFrame

        Returns:
            DataFrame with seasonality indices
        """
        # Extract quarter number
        summary_copy = summary.copy()
        summary_copy["quarter_num"] = summary_copy["year_quarter"].apply(
            lambda x: int(x.split("-Q")[1])
        )

        # Calculate average trips per quarter across all years
        avg_by_quarter = summary_copy.groupby("quarter_num")["trips"].mean()
        overall_avg = summary_copy["trips"].mean()

        # Calculate seasonality index
        seasonality = (avg_by_quarter / overall_avg * 100).to_dict()

        return seasonality

    @staticmethod
    def calculate_utilization_metrics(data: pd.DataFrame) -> Dict[str, Any]:
        """
        Calculate bike and station utilization metrics

        Args:
            data: Processed trip data DataFrame

        Returns:
            Dictionary of utilization metrics
        """
        # Trips per bike
        bike_usage = data.groupby("bike_id").size()

        # Trips per station
        station_usage = data.groupby("start_station").size()

        metrics = {
            "avg_trips_per_bike": bike_usage.mean(),
            "median_trips_per_bike": bike_usage.median(),
            "max_trips_per_bike": bike_usage.max(),
            "min_trips_per_bike": bike_usage.min(),
            "avg_trips_per_station": station_usage.mean(),
            "median_trips_per_station": station_usage.median(),
            "max_trips_per_station": station_usage.max(),
            "min_trips_per_station": station_usage.min(),
        }

        return metrics

    @staticmethod
    def calculate_peak_times(data: pd.DataFrame) -> Dict[str, Any]:
        """
        Identify peak usage times

        Args:
            data: Processed trip data DataFrame

        Returns:
            Dictionary of peak time information
        """
        hourly_trips = data.groupby("hour").size()
        daily_trips = data.groupby("day_name").size()
        monthly_trips = data.groupby("month").size()

        peak_info = {
            "peak_hour": hourly_trips.idxmax(),
            "peak_hour_trips": hourly_trips.max(),
            "peak_day": daily_trips.idxmax(),
            "peak_day_trips": daily_trips.max(),
            "peak_month": monthly_trips.idxmax(),
            "peak_month_trips": monthly_trips.max(),
            "off_peak_hour": hourly_trips.idxmin(),
            "off_peak_hour_trips": hourly_trips.min(),
        }

        return peak_info

    @staticmethod
    def calculate_retention_proxy(data: pd.DataFrame) -> Dict[str, Any]:
        """
        Calculate proxy metrics for user retention

        Args:
            data: Processed trip data DataFrame

        Returns:
            Dictionary of retention proxy metrics
        """
        # Calculate trips by user type if available
        if "passholder_type" in data.columns:
            user_type_dist = data["passholder_type"].value_counts()

            return {
                "user_type_distribution": user_type_dist.to_dict(),
                "member_percentage": (
                    (
                        user_type_dist.get("Indego30", 0)
                        + user_type_dist.get("Indego365", 0)
                    )
                    / len(data)
                    * 100
                    if len(data) > 0
                    else 0
                ),
            }
        else:
            return {"user_type_distribution": {}, "member_percentage": 0}

    @staticmethod
    def format_number(num: float, decimal_places: int = 2) -> str:
        """
        Format numbers for display with commas and decimals

        Args:
            num: Number to format
            decimal_places: Number of decimal places

        Returns:
            Formatted string
        """
        if num >= 1_000_000:
            return f"{num / 1_000_000:.{decimal_places}f}M"
        elif num >= 1_000:
            return f"{num / 1_000:.{decimal_places}f}K"
        else:
            return f"{num:.{decimal_places}f}"

    @staticmethod
    def format_duration(minutes: float) -> str:
        """
        Format duration in minutes to readable string

        Args:
            minutes: Duration in minutes

        Returns:
            Formatted duration string
        """
        if minutes < 60:
            return f"{minutes:.1f} min"
        elif minutes < 1440:
            hours = minutes / 60
            return f"{hours:.1f} hrs"
        else:
            days = minutes / 1440
            return f"{days:.1f} days"
