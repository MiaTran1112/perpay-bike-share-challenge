"""
Visualization module for Indego Bike Share dashboard
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from typing import Optional, Tuple
from config import CHART_STYLE, CHART_FONT_SCALE, DEFAULT_FIGURE_SIZE, COLOR_PALETTE


# Set default style
sns.set(style=CHART_STYLE, font_scale=CHART_FONT_SCALE)


class Visualizer:
    """Class containing visualization methods for bike share data"""

    @staticmethod
    def plot_trips_per_quarter(
        summary: pd.DataFrame, figsize: Tuple[int, int] = DEFAULT_FIGURE_SIZE
    ) -> plt.Figure:
        """
        Create line plot of total trips per quarter

        Args:
            summary: Quarterly summary DataFrame
            figsize: Figure size tuple

        Returns:
            Matplotlib figure
        """
        fig, ax = plt.subplots(figsize=figsize)

        sns.lineplot(
            data=summary,
            x="year_quarter",
            y="trips",
            marker="o",
            color=COLOR_PALETTE["primary"],
            linewidth=2.5,
            markersize=8,
            ax=ax,
        )

        ax.set_title(
            "Total Trips per Quarter (2020-2025)",
            fontsize=16,
            fontweight="bold",
            pad=20,
        )
        ax.set_xlabel("Year-Quarter", fontsize=12, fontweight="bold")
        ax.set_ylabel("Number of Trips", fontsize=12, fontweight="bold")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        return fig

    @staticmethod
    def plot_ride_minutes_per_quarter(
        summary: pd.DataFrame, figsize: Tuple[int, int] = DEFAULT_FIGURE_SIZE
    ) -> plt.Figure:
        """
        Create line plot of total ride minutes per quarter

        Args:
            summary: Quarterly summary DataFrame
            figsize: Figure size tuple

        Returns:
            Matplotlib figure
        """
        fig, ax = plt.subplots(figsize=figsize)

        sns.lineplot(
            data=summary,
            x="year_quarter",
            y="total_minutes",
            marker="o",
            color=COLOR_PALETTE["secondary"],
            linewidth=2.5,
            markersize=8,
            ax=ax,
        )

        ax.set_title(
            "Total Ride Minutes per Quarter", fontsize=16, fontweight="bold", pad=20
        )
        ax.set_xlabel("Year-Quarter", fontsize=12, fontweight="bold")
        ax.set_ylabel("Total Minutes", fontsize=12, fontweight="bold")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        return fig

    @staticmethod
    def plot_avg_duration_per_quarter(
        summary: pd.DataFrame, figsize: Tuple[int, int] = DEFAULT_FIGURE_SIZE
    ) -> plt.Figure:
        """
        Create line plot of average trip duration per quarter

        Args:
            summary: Quarterly summary DataFrame
            figsize: Figure size tuple

        Returns:
            Matplotlib figure
        """
        fig, ax = plt.subplots(figsize=figsize)

        sns.lineplot(
            data=summary,
            x="year_quarter",
            y="avg_duration",
            marker="o",
            color=COLOR_PALETTE["success"],
            linewidth=2.5,
            markersize=8,
            ax=ax,
        )

        ax.set_title(
            "Average Trip Duration per Quarter", fontsize=16, fontweight="bold", pad=20
        )
        ax.set_xlabel("Year-Quarter", fontsize=12, fontweight="bold")
        ax.set_ylabel("Minutes", fontsize=12, fontweight="bold")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        return fig

    @staticmethod
    def plot_rolling_12month(
        summary: pd.DataFrame, figsize: Tuple[int, int] = DEFAULT_FIGURE_SIZE
    ) -> plt.Figure:
        """
        Create line plot of rolling 12-month total trips

        Args:
            summary: Quarterly summary DataFrame
            figsize: Figure size tuple

        Returns:
            Matplotlib figure
        """
        fig, ax = plt.subplots(figsize=figsize)

        sns.lineplot(
            data=summary,
            x="year_quarter",
            y="rolling_year_trips",
            marker="o",
            color=COLOR_PALETTE["info"],
            linewidth=2.5,
            markersize=8,
            ax=ax,
        )

        ax.set_title(
            "Rolling 12-Month Total Trips", fontsize=16, fontweight="bold", pad=20
        )
        ax.set_xlabel("Year-Quarter", fontsize=12, fontweight="bold")
        ax.set_ylabel("Trips (sum of last 4 quarters)", fontsize=12, fontweight="bold")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        return fig

    @staticmethod
    def plot_growth_rates(
        summary: pd.DataFrame, figsize: Tuple[int, int] = (12, 8)
    ) -> plt.Figure:
        """
        Create subplot showing QoQ and YoY growth rates

        Args:
            summary: Quarterly summary DataFrame
            figsize: Figure size tuple

        Returns:
            Matplotlib figure
        """
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=figsize)

        # QoQ Growth
        sns.lineplot(
            data=summary,
            x="year_quarter",
            y="trips_growth_qoq",
            marker="o",
            color=COLOR_PALETTE["primary"],
            linewidth=2,
            ax=ax1,
        )
        ax1.axhline(y=0, color="red", linestyle="--", alpha=0.5)
        ax1.set_title(
            "Quarter-over-Quarter Growth Rate", fontsize=14, fontweight="bold"
        )
        ax1.set_xlabel("")
        ax1.set_ylabel("Growth (%)", fontsize=11, fontweight="bold")
        ax1.tick_params(axis="x", rotation=45)

        # YoY Growth
        sns.lineplot(
            data=summary,
            x="year_quarter",
            y="trips_growth_yoy",
            marker="o",
            color=COLOR_PALETTE["success"],
            linewidth=2,
            ax=ax2,
        )
        ax2.axhline(y=0, color="red", linestyle="--", alpha=0.5)
        ax2.set_title("Year-over-Year Growth Rate", fontsize=14, fontweight="bold")
        ax2.set_xlabel("Year-Quarter", fontsize=11, fontweight="bold")
        ax2.set_ylabel("Growth (%)", fontsize=11, fontweight="bold")
        plt.xticks(rotation=45, ha="right")

        plt.tight_layout()
        return fig

    @staticmethod
    def plot_hourly_patterns(
        hourly_data: pd.DataFrame, figsize: Tuple[int, int] = DEFAULT_FIGURE_SIZE
    ) -> plt.Figure:
        """
        Create visualization of trip patterns by hour of day

        Args:
            hourly_data: Hourly pattern DataFrame
            figsize: Figure size tuple

        Returns:
            Matplotlib figure
        """
        fig, ax = plt.subplots(figsize=figsize)

        sns.lineplot(
            data=hourly_data,
            x="hour",
            y="trips",
            hue="day_type",
            marker="o",
            linewidth=2.5,
            markersize=8,
            ax=ax,
        )

        ax.set_title(
            "Trip Patterns by Hour of Day", fontsize=16, fontweight="bold", pad=20
        )
        ax.set_xlabel("Hour of Day", fontsize=12, fontweight="bold")
        ax.set_ylabel("Number of Trips", fontsize=12, fontweight="bold")
        ax.set_xticks(range(0, 24))
        ax.legend(title="Day Type", fontsize=10)
        plt.tight_layout()

        return fig

    @staticmethod
    def plot_daily_patterns(
        daily_data: pd.DataFrame, figsize: Tuple[int, int] = DEFAULT_FIGURE_SIZE
    ) -> plt.Figure:
        """
        Create bar plot of trip patterns by day of week

        Args:
            daily_data: Daily pattern DataFrame
            figsize: Figure size tuple

        Returns:
            Matplotlib figure
        """
        fig, ax = plt.subplots(figsize=figsize)

        sns.barplot(data=daily_data, x="day_name", y="trips", palette="viridis", ax=ax)

        ax.set_title(
            "Trip Patterns by Day of Week", fontsize=16, fontweight="bold", pad=20
        )
        ax.set_xlabel("Day of Week", fontsize=12, fontweight="bold")
        ax.set_ylabel("Number of Trips", fontsize=12, fontweight="bold")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        return fig

    @staticmethod
    def plot_top_stations(
        station_data: pd.DataFrame,
        top_n: int = 15,
        figsize: Tuple[int, int] = DEFAULT_FIGURE_SIZE,
    ) -> plt.Figure:
        """
        Create horizontal bar plot of top stations by activity

        Args:
            station_data: Station summary DataFrame
            top_n: Number of top stations to display
            figsize: Figure size tuple

        Returns:
            Matplotlib figure
        """
        fig, ax = plt.subplots(figsize=figsize)

        top_stations = station_data.nlargest(top_n, "total_activity")

        sns.barplot(
            data=top_stations,
            y="start_station",
            x="total_activity",
            palette="rocket",
            ax=ax,
        )

        ax.set_title(
            f"Top {top_n} Stations by Total Activity",
            fontsize=16,
            fontweight="bold",
            pad=20,
        )
        ax.set_xlabel(
            "Total Activity (Departures + Arrivals)", fontsize=12, fontweight="bold"
        )
        ax.set_ylabel("Station", fontsize=12, fontweight="bold")
        plt.tight_layout()

        return fig

    @staticmethod
    def plot_duration_distribution(
        data: pd.DataFrame, figsize: Tuple[int, int] = DEFAULT_FIGURE_SIZE
    ) -> plt.Figure:
        """
        Create histogram of trip duration distribution

        Args:
            data: Trip data DataFrame
            figsize: Figure size tuple

        Returns:
            Matplotlib figure
        """
        fig, ax = plt.subplots(figsize=figsize)

        # Plot distribution (limiting to 60 minutes for better visualization)
        duration_sample = data[data["duration"] <= 60]["duration"]

        sns.histplot(
            duration_sample, bins=60, color=COLOR_PALETTE["primary"], alpha=0.7, ax=ax
        )

        ax.set_title(
            "Trip Duration Distribution (0-60 minutes)",
            fontsize=16,
            fontweight="bold",
            pad=20,
        )
        ax.set_xlabel("Duration (minutes)", fontsize=12, fontweight="bold")
        ax.set_ylabel("Frequency", fontsize=12, fontweight="bold")
        plt.tight_layout()

        return fig

    @staticmethod
    def plot_monthly_heatmap(
        data: pd.DataFrame, figsize: Tuple[int, int] = (14, 8)
    ) -> plt.Figure:
        """
        Create heatmap of trips by month and year

        Args:
            data: Trip data DataFrame
            figsize: Figure size tuple

        Returns:
            Matplotlib figure
        """
        # Create pivot table for heatmap
        monthly_pivot = data.groupby(["year", "month"]).size().reset_index(name="trips")
        pivot_table = monthly_pivot.pivot(index="month", columns="year", values="trips")

        fig, ax = plt.subplots(figsize=figsize)

        sns.heatmap(
            pivot_table,
            annot=True,
            fmt=".0f",
            cmap="YlOrRd",
            cbar_kws={"label": "Number of Trips"},
            ax=ax,
        )

        ax.set_title(
            "Monthly Trip Volume Heatmap", fontsize=16, fontweight="bold", pad=20
        )
        ax.set_xlabel("Year", fontsize=12, fontweight="bold")
        ax.set_ylabel("Month", fontsize=12, fontweight="bold")
        ax.set_yticklabels(
            [
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun",
                "Jul",
                "Aug",
                "Sep",
                "Oct",
                "Nov",
                "Dec",
            ],
            rotation=0,
        )
        plt.tight_layout()

        return fig

    @staticmethod
    def plot_metrics_comparison(
        summary: pd.DataFrame, figsize: Tuple[int, int] = (14, 10)
    ) -> plt.Figure:
        """
        Create multi-panel comparison of key metrics

        Args:
            summary: Quarterly summary DataFrame
            figsize: Figure size tuple

        Returns:
            Matplotlib figure
        """
        fig, axes = plt.subplots(2, 2, figsize=figsize)

        # Trips
        sns.lineplot(
            data=summary,
            x="year_quarter",
            y="trips",
            marker="o",
            color=COLOR_PALETTE["primary"],
            ax=axes[0, 0],
        )
        axes[0, 0].set_title("Total Trips", fontweight="bold")
        axes[0, 0].tick_params(axis="x", rotation=45)
        axes[0, 0].set_xlabel("")

        # Total Minutes
        sns.lineplot(
            data=summary,
            x="year_quarter",
            y="total_minutes",
            marker="o",
            color=COLOR_PALETTE["secondary"],
            ax=axes[0, 1],
        )
        axes[0, 1].set_title("Total Ride Minutes", fontweight="bold")
        axes[0, 1].tick_params(axis="x", rotation=45)
        axes[0, 1].set_xlabel("")

        # Unique Bikes
        sns.lineplot(
            data=summary,
            x="year_quarter",
            y="unique_bikes",
            marker="o",
            color=COLOR_PALETTE["success"],
            ax=axes[1, 0],
        )
        axes[1, 0].set_title("Unique Bikes in Use", fontweight="bold")
        axes[1, 0].tick_params(axis="x", rotation=45)

        # Active Stations
        sns.lineplot(
            data=summary,
            x="year_quarter",
            y="active_stations",
            marker="o",
            color=COLOR_PALETTE["info"],
            ax=axes[1, 1],
        )
        axes[1, 1].set_title("Active Stations", fontweight="bold")
        axes[1, 1].tick_params(axis="x", rotation=45)

        plt.tight_layout()
        return fig
