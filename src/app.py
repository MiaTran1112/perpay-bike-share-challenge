"""
Indego Bike Share Analytics Dashboard - Main Application
"""

import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Add current directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from config import APP_TITLE, APP_ICON, PAGE_LAYOUT, INITIAL_SIDEBAR_STATE
from data_loader import DataLoader
from metrics import MetricsCalculator
from visualizations import Visualizer


# Page configuration
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout=PAGE_LAYOUT,
    initial_sidebar_state=INITIAL_SIDEBAR_STATE,
)


# Initialize classes
@st.cache_resource
def get_data_loader():
    """Initialize and cache DataLoader instance"""
    return DataLoader()


@st.cache_resource
def get_visualizer():
    """Initialize and cache Visualizer instance"""
    return Visualizer()


def load_and_process_data():
    """Load and process all data"""
    loader = get_data_loader()

    with st.spinner("Loading data..."):
        processed_data, summary_data = loader.get_full_pipeline()

    return loader, processed_data, summary_data


def render_header():
    """Render dashboard header"""
    st.title(f"{APP_ICON} {APP_TITLE}")
    st.markdown(
        """
    ### Comprehensive Analytics Dashboard for Philadelphia's Bike Share Program
    
    This interactive dashboard analyzes **5.9+ million trip records** from 2020 to 2025, 
    providing insights into growth trends, usage patterns, and strategic opportunities 
    for the Indego Bike Share program.
    """
    )
    st.divider()


def render_kpi_cards(kpis: dict, growth_metrics: dict):
    """Render KPI metric cards"""
    st.subheader("Key Performance Indicators")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            label="Total Trips",
            value=MetricsCalculator.format_number(kpis["total_trips"], 1),
            delta=f"{growth_metrics['avg_yoy_trips_growth']:.1f}% YoY",
        )

    with col2:
        st.metric(
            label="Total Ride Hours",
            value=MetricsCalculator.format_number(kpis["total_ride_hours"], 1),
            delta=f"{growth_metrics['avg_yoy_minutes_growth']:.1f}% YoY",
        )

    with col3:
        st.metric(
            label="Avg Trip Duration",
            value=f"{kpis['avg_trip_duration']:.1f} min",
            delta=None,
        )

    with col4:
        st.metric(label="Unique Bikes", value=f"{kpis['unique_bikes']:,}", delta=None)

    with col5:
        st.metric(
            label="Active Stations", value=f"{kpis['unique_stations']:,}", delta=None
        )

    st.divider()


def render_time_series_analysis(summary_data: pd.DataFrame, visualizer: Visualizer):
    """Render time series analysis section"""
    st.header("Time Series Analysis")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Total Trips", "Ride Minutes", "Avg Duration", "Rolling 12-Month"]
    )

    with tab1:
        st.markdown("### Total Trips per Quarter")
        fig = visualizer.plot_trips_per_quarter(summary_data)
        st.pyplot(fig)
        st.markdown(
            """
        **Insight:** The number of bike trips shows strong seasonality, peaking in spring and summer 
        (Q2-Q3) and dipping in colder quarters (Q1, Q4). After initial COVID-related slowdown, 
        Indego experienced steady growth with trips reaching record highs by 2025.
        """
        )

    with tab2:
        st.markdown("### Total Ride Minutes per Quarter")
        fig = visualizer.plot_ride_minutes_per_quarter(summary_data)
        st.pyplot(fig)
        st.markdown(
            """
        **Insight:** Total ride minutes (proxy for revenue) follow similar seasonal patterns. 
        Overall usage has more than tripled since 2020, indicating strong engagement and 
        revenue growth potential.
        """
        )

    with tab3:
        st.markdown("### Average Trip Duration per Quarter")
        fig = visualizer.plot_avg_duration_per_quarter(summary_data)
        st.pyplot(fig)
        st.markdown(
            """
        **Insight:** Average trip duration peaked in early 2020 (likely pandemic leisure rides) 
        and stabilized around 15-20 minutes, suggesting a shift toward shorter, routine trips 
        for commuting or errands.
        """
        )

    with tab4:
        st.markdown("### Rolling 12-Month Total Trips")
        fig = visualizer.plot_rolling_12month(summary_data)
        st.pyplot(fig)
        st.markdown(
            """
        **Insight:** The rolling 12-month trend smooths out seasonal variation and shows 
        continuous growth since 2021. Annual trips nearly doubled by 2025, indicating 
        consistent adoption without signs of decline.
        """
        )

    st.divider()


def render_growth_analysis(summary_data: pd.DataFrame, visualizer: Visualizer):
    """Render growth analysis section"""
    st.header("Growth Analysis")

    st.markdown("### Growth Rates Over Time")
    fig = visualizer.plot_growth_rates(summary_data)
    st.pyplot(fig)

    st.markdown("### Growth Metrics Summary")

    calc = MetricsCalculator()
    growth_metrics = calc.calculate_growth_metrics(summary_data)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            "Avg Quarter-over-Quarter Growth",
            f"{growth_metrics['avg_qoq_trips_growth']:.2f}%",
        )
    with col2:
        st.metric(
            "Avg Year-over-Year Growth",
            f"{growth_metrics['avg_yoy_trips_growth']:.2f}%",
        )
    with col3:
        st.metric(
            "Total Growth (2020-2025)", f"{growth_metrics['total_growth_rate']:.2f}%"
        )

    st.info(
        """
    **Key Findings:**
    - Consistent YoY growth of ~15% demonstrates sustainable expansion
    - QoQ fluctuations reflect seasonal patterns
    - No evidence of overgrowth or stagnation
    """
    )

    st.divider()


def render_usage_patterns(
    processed_data: pd.DataFrame, loader: DataLoader, visualizer: Visualizer
):
    """Render usage patterns analysis section"""
    st.header("Usage Patterns Analysis")

    tab1, tab2, tab3 = st.tabs(["Hourly Patterns", "Daily Patterns", "Monthly Heatmap"])

    with tab1:
        st.markdown("### Trip Patterns by Hour of Day")
        hourly_data = loader.get_hourly_patterns(processed_data)
        fig = visualizer.plot_hourly_patterns(hourly_data)
        st.pyplot(fig)

        peak_times = MetricsCalculator.calculate_peak_times(processed_data)
        st.info(
            f"**Peak Hour:** {peak_times['peak_hour']}:00 with "
            f"{peak_times['peak_hour_trips']:,} trips"
        )

    with tab2:
        st.markdown("### Trip Patterns by Day of Week")
        daily_data = loader.get_daily_patterns(processed_data)
        fig = visualizer.plot_daily_patterns(daily_data)
        st.pyplot(fig)

        peak_times = MetricsCalculator.calculate_peak_times(processed_data)
        st.info(
            f"**Peak Day:** {peak_times['peak_day']} with "
            f"{peak_times['peak_day_trips']:,} trips"
        )

    with tab3:
        st.markdown("### Monthly Trip Volume Heatmap")
        fig = visualizer.plot_monthly_heatmap(processed_data)
        st.pyplot(fig)
        st.markdown(
            """
        **Insight:** Clear seasonal patterns with summer months (June-August) showing 
        highest activity across all years.
        """
        )

    st.divider()


def render_station_analysis(
    processed_data: pd.DataFrame, loader: DataLoader, visualizer: Visualizer
):
    """Render station analysis section"""
    st.header("Station Analysis")

    station_data = loader.get_station_summary(processed_data)

    st.markdown("### Station Statistics")

    utilization = MetricsCalculator.calculate_utilization_metrics(processed_data)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            "Avg Trips per Station", f"{utilization['avg_trips_per_station']:.0f}"
        )
    with col2:
        st.metric(
            "Max Trips per Station", f"{utilization['max_trips_per_station']:,.0f}"
        )
    with col3:
        st.metric(
            "Min Trips per Station", f"{utilization['min_trips_per_station']:,.0f}"
        )

    st.markdown("### Top Stations by Total Activity")
    top_n = st.slider("Number of top stations to display", 5, 30, 15)

    fig = visualizer.plot_top_stations(station_data, top_n=top_n)
    st.pyplot(fig)

    st.markdown("### Top 5 Stations Details")
    top_5 = station_data.head(5)[["start_station", "total_activity"]]
    st.dataframe(top_5, hide_index=True, use_container_width=True)

    st.divider()


def render_advanced_metrics(
    processed_data: pd.DataFrame, summary_data: pd.DataFrame, visualizer: Visualizer
):
    """Render advanced metrics section"""
    st.header("Advanced Analytics")

    tab1, tab2 = st.tabs(["Duration Distribution", "Multi-Metric Comparison"])

    with tab1:
        st.markdown("### Trip Duration Distribution")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Mean Duration", f"{processed_data['duration'].mean():.1f} min")
        with col2:
            st.metric(
                "Median Duration", f"{processed_data['duration'].median():.1f} min"
            )
        with col3:
            st.metric(
                "Mode Duration", f"{processed_data['duration'].mode()[0]:.0f} min"
            )
        with col4:
            st.metric("Max Duration", f"{processed_data['duration'].max():.1f} min")

        fig = visualizer.plot_duration_distribution(processed_data)
        st.pyplot(fig)

    with tab2:
        st.markdown("### Multi-Metric Comparison")
        fig = visualizer.plot_metrics_comparison(summary_data)
        st.pyplot(fig)
        st.markdown(
            """
        **Insight:** All key metrics show coordinated growth, indicating healthy 
        infrastructure expansion aligned with increasing demand.
        """
        )

    st.divider()


def render_data_explorer(
    processed_data: pd.DataFrame, summary_data: pd.DataFrame, loader: DataLoader
):
    """Render interactive data explorer"""
    st.header("Data Explorer")

    tab1, tab2 = st.tabs(["Trip Data", "Quarterly Summary"])

    with tab1:
        st.markdown("### Filter and Explore Trip Data")

        col1, col2, col3 = st.columns(3)

        with col1:
            years = sorted(processed_data["year"].unique())
            selected_years = st.multiselect("Select Years", years, default=years[-2:])

        with col2:
            quarters = sorted(processed_data["quarter"].unique())
            selected_quarters = st.multiselect(
                "Select Quarters", quarters, default=quarters
            )

        with col3:
            day_types = processed_data["day_type"].unique().tolist()
            selected_day_types = st.multiselect(
                "Day Type", day_types, default=day_types
            )

        # Filter data
        filtered_data = loader.filter_data(
            processed_data,
            years=selected_years if selected_years else None,
            quarters=selected_quarters if selected_quarters else None,
            day_types=selected_day_types if selected_day_types else None,
        )

        st.markdown(f"**Showing {len(filtered_data):,} trips**")

        # Display sample
        st.dataframe(
            filtered_data.head(1000)[
                [
                    "start_time",
                    "end_time",
                    "duration",
                    "start_station",
                    "end_station",
                    "bike_id",
                    "year_quarter",
                ]
            ],
            use_container_width=True,
        )

        # Download button
        csv = filtered_data.to_csv(index=False)
        st.download_button(
            label="Download Filtered Data as CSV",
            data=csv,
            file_name="indego_filtered_trips.csv",
            mime="text/csv",
        )

    with tab2:
        st.markdown("### Quarterly Summary Statistics")
        st.dataframe(summary_data, use_container_width=True)

        csv = summary_data.to_csv(index=False)
        st.download_button(
            label="Download Summary as CSV",
            data=csv,
            file_name="indego_quarterly_summary.csv",
            mime="text/csv",
        )

    st.divider()


def render_insights_and_recommendations():
    """Render insights and strategic recommendations"""
    st.header("Key Insights & Recommendations")

    st.markdown("### Key Findings")
    st.success(
        """
    **1. Sustainable Growth**: ~15% YoY growth demonstrates healthy, sustainable expansion
    
    **2. Strong Seasonality**: Clear peaks in Q2-Q3 (spring/summer), dips in Q1/Q4 (winter)
    
    **3. Trip Maturity**: Average duration stabilized at 15-20 minutes, indicating shift 
    from leisure to utilitarian trips (commuting, errands)
    
    **4. Consistent Adoption**: Rolling 12-month trends show no signs of market saturation
    
    **5. Infrastructure Alignment**: Bike and station growth aligns with demand increases
    """
    )

    st.markdown("### Strategic Recommendations")
    st.info(
        """
    **1. Maintain Sustainable Pace**: Continue measured expansion aligned with ~15% growth
    
    **2. Address Seasonality**: Implement winter incentives and promotions to reduce 
    seasonal dips
    
    **3. Optimize Station Placement**: Use data-driven analysis to identify high-demand 
    corridors for new stations
    
    **4. Enhance Retention**: Focus on loyalty programs and membership benefits
    
    **5. Predictive Analytics**: Deploy demand forecasting models for operational efficiency
    """
    )

    st.divider()


def render_sidebar(processed_data: pd.DataFrame):
    """Render sidebar with filters and information"""
    st.sidebar.title("Dashboard Controls")

    st.sidebar.markdown("---")

    st.sidebar.markdown("### Dataset Overview")
    st.sidebar.info(
        f"""
    **Total Records:** {len(processed_data):,}
    
    **Date Range:** {processed_data['start_time'].min().strftime('%Y-%m-%d')} 
    to {processed_data['start_time'].max().strftime('%Y-%m-%d')}
    
    **Years Covered:** {processed_data['year'].nunique()}
    
    **Quarters:** {processed_data['year_quarter'].nunique()}
    """
    )

    st.sidebar.markdown("---")

    st.sidebar.markdown("### About")
    st.sidebar.markdown(
        """
    This dashboard analyzes Philadelphia's Indego Bike Share trip data to 
    provide insights on program growth, usage patterns, and strategic opportunities.
    
    **Data Source:** Indego Open Data Portal
    
    **Analysis Period:** 2020-2025
    """
    )

    st.sidebar.markdown("---")

    st.sidebar.markdown("### Navigation")
    st.sidebar.markdown(
        """
    - **KPIs**: High-level performance metrics
    - **Time Series**: Quarterly trend analysis
    - **Growth**: QoQ and YoY growth rates
    - **Patterns**: Hourly, daily, monthly usage
    - **Stations**: Station-level analytics
    - **Advanced**: Detailed distributions
    - **Explorer**: Interactive data filtering
    - **Insights**: Strategic recommendations
    """
    )


def main():
    """Main application entry point"""

    # Render header
    render_header()

    # Load data
    try:
        loader, processed_data, summary_data = load_and_process_data()
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return

    # Success message
    st.success(f"Successfully loaded {len(processed_data):,} trip records!")

    # Initialize calculator and visualizer
    calc = MetricsCalculator()
    viz = get_visualizer()

    # Calculate KPIs and metrics
    kpis = calc.calculate_kpis(processed_data)
    growth_metrics = calc.calculate_growth_metrics(summary_data)

    # Render sidebar
    render_sidebar(processed_data)

    # Render main content sections
    render_kpi_cards(kpis, growth_metrics)
    render_time_series_analysis(summary_data, viz)
    render_growth_analysis(summary_data, viz)
    render_usage_patterns(processed_data, loader, viz)
    render_station_analysis(processed_data, loader, viz)
    render_advanced_metrics(processed_data, summary_data, viz)
    render_data_explorer(processed_data, summary_data, loader)
    render_insights_and_recommendations()

    # Footer
    st.markdown("---")
    st.markdown(
        """
    <div style='text-align: center'>
        <p>Indego Bike Share Analytics Dashboard | Built with Streamlit</p>
    </div>
    """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
