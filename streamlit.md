# Indego Bike Share Analytics Dashboard

A comprehensive Streamlit dashboard for analyzing Philadelphia's Indego Bike Share program data from 2020-2025.

## Project Structure

```
src/
├── __init__.py           # Package initialization
├── app.py                # Main Streamlit application
├── config.py             # Configuration constants and paths
├── data_loader.py        # Data loading and processing class
├── metrics.py            # KPI calculations and metrics
├── visualizations.py     # Visualization functions
```

## Features

### 1. Key Performance Indicators (KPIs)

- Total trips and ride hours
- Average trip duration
- Unique bikes and active stations
- Year-over-year growth rates

### 2. Time Series Analysis

- Total trips per quarter
- Total ride minutes (revenue proxy)
- Average trip duration trends
- Rolling 12-month totals

### 3. Growth Analysis

- Quarter-over-quarter (QoQ) growth rates
- Year-over-year (YoY) growth rates
- Total growth from 2020-2025
- Growth trend visualizations

### 4. Usage Patterns

- Hourly trip patterns (weekday vs weekend)
- Daily trip patterns by day of week
- Monthly heatmap showing seasonal trends
- Peak time identification

### 5. Station Analysis

- Top stations by total activity
- Station utilization metrics
- Departure and arrival statistics

### 6. Advanced Analytics

- Trip duration distribution
- Multi-metric comparison dashboard
- Statistical summaries

### 7. Interactive Data Explorer

- Filter by year, quarter, and day type
- View and download filtered data
- Quarterly summary statistics export

### 8. Strategic Insights

- Key findings summary
- Data-driven recommendations
- Growth assessment

## Running the Dashboard

### Option 1: From src directory

```bash
cd src
streamlit run app.py
```

### Option 2: From project root

```bash
streamlit run src/app.py
```

### Option 3: With specific port

```bash
streamlit run src/app.py --server.port 8501
```

## Requirements

All required packages are listed in `requirements.txt`:

- streamlit
- pandas
- numpy
- matplotlib
- seaborn

Install dependencies:

```bash
pip install -r requirements.txt
```

## Data Requirements

The dashboard expects CSV files in the `data/` directory with the following structure:

- File naming pattern: `indego-trips-YYYY-qQ.csv`
- Required columns:
  - `trip_id`: Unique trip identifier
  - `start_time`: Trip start timestamp
  - `end_time`: Trip end timestamp
  - `duration`: Trip duration in minutes
  - `start_station`: Starting station name
  - `end_station`: Ending station name
  - `bike_id`: Bike identifier

## Code Organization

### config.py

Contains all configuration constants including:

- File paths
- Data validation constraints
- App settings
- Color schemes
- Chart configurations

### data_loader.py

`DataLoader` class with methods for:

- Loading CSV files from data directory
- Cleaning and processing raw data
- Generating quarterly summaries
- Station and temporal analysis
- Data filtering

### metrics.py

`MetricsCalculator` class with methods for:

- Calculating KPIs
- Computing growth metrics
- Period comparisons
- Seasonality analysis
- Utilization metrics
- Peak time identification

### visualizations.py

`Visualizer` class with methods for:

- Line plots (trips, minutes, duration)
- Growth rate visualizations
- Hourly and daily pattern charts
- Station activity charts
- Heatmaps
- Distribution plots
- Multi-metric dashboards

### app.py

Main Streamlit application with:

- Page configuration
- Data loading and caching
- Multiple dashboard sections
- Interactive filters
- Download capabilities
- Responsive layout

## Performance Optimizations

1. **Data Caching**: Uses `@st.cache_data` and `@st.cache_resource` decorators
2. **Lazy Loading**: Data loaded only when needed
3. **Efficient Processing**: Pandas operations optimized for large datasets
4. **Responsive Design**: Wide layout with collapsible sidebar

## Customization

### Changing Color Schemes

Edit `COLOR_PALETTE` in `config.py`:

```python
COLOR_PALETTE = {
    "primary": "#1f77b4",
    "secondary": "#ff7f0e",
    # ... add more colors
}
```

### Adjusting Chart Sizes

Modify `DEFAULT_FIGURE_SIZE` in `config.py`:

```python
DEFAULT_FIGURE_SIZE = (12, 6)  # (width, height)
```

### Adding New Metrics

1. Add calculation method to `MetricsCalculator` in `metrics.py`
2. Add visualization method to `Visualizer` in `visualizations.py`
3. Add rendering function in `app.py`

## Troubleshooting

### Error: "No CSV files found"

- Ensure data files are in the `data/` directory
- Check file naming pattern matches `*.csv`

### Error: "Module not found"

- Install all requirements: `pip install -r requirements.txt`
- Ensure running from correct directory

### Performance Issues

- Reduce date range filter
- Use fewer top stations in station analysis
- Clear Streamlit cache: `streamlit cache clear`

## Future Enhancements

Potential additions:

- Geographic mapping with station locations
- User type analysis (if available in data)
- Weather correlation analysis
- Predictive modeling for demand forecasting
- Real-time data integration
- Mobile responsiveness improvements

## License

This project is for educational and analytical purposes.

## Contact

For questions or suggestions, please refer to the main project README.
