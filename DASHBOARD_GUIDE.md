# Indego Bike Share Dashboard - User Guide

## Quick Start

### Running the Dashboard

**Method 1: Using the launch script (Recommended)**

```bash
./run_dashboard.sh
```

**Method 2: Using Streamlit directly**

```bash
cd src
streamlit run app.py
```

**Method 3: From project root**

```bash
streamlit run src/app.py
```

The dashboard will automatically open in your default web browser at `http://localhost:8501`

---

## Dashboard Overview

The Indego Bike Share Analytics Dashboard provides comprehensive insights into Philadelphia's bike share program from 2020-2025, with over 5.9 million trip records analyzed.

### Main Sections

1. **Key Performance Indicators (KPIs)**
2. **Time Series Analysis**
3. **Growth Analysis**
4. **Usage Patterns Analysis**
5. **Station Analysis**
6. **Advanced Analytics**
7. **Data Explorer**
8. **Key Insights & Recommendations**

---

## Section-by-Section Guide

### 1. Key Performance Indicators (KPIs)

Located at the top of the dashboard, these cards provide at-a-glance metrics:

- **Total Trips**: Complete count of all trips with YoY growth rate
- **Total Ride Hours**: Sum of all ride time (proxy for revenue)
- **Avg Trip Duration**: Mean duration across all trips
- **Unique Bikes**: Number of distinct bikes in the fleet
- **Active Stations**: Number of stations with recorded activity

**What to look for:**

- Green delta (↑) indicates positive growth
- Red delta (↓) indicates decline
- Use these to quickly assess overall program health

---

### 2. Time Series Analysis

Four interactive tabs showing quarterly trends:

#### Tab 1: Total Trips

- **Shows**: Number of trips per quarter from 2020-2025
- **Pattern**: Strong seasonality with Q2-Q3 peaks (spring/summer)
- **Insight**: Steady growth post-pandemic recovery

#### Tab 2: Ride Minutes

- **Shows**: Total ride time per quarter (revenue proxy)
- **Pattern**: Mirrors trip patterns but with different scale
- **Insight**: Usage has more than tripled since 2020

#### Tab 3: Avg Duration

- **Shows**: Average trip length over time
- **Pattern**: Stabilized around 15-20 minutes after early 2020 peak
- **Insight**: Shift from leisure to utilitarian use (commuting)

#### Tab 4: Rolling 12-Month

- **Shows**: Sum of last 4 quarters (smoothed annual view)
- **Pattern**: Continuous upward trend
- **Insight**: No signs of market saturation

**How to use:**

- Click tabs to switch between views
- Look for trend direction and consistency
- Compare peaks and troughs across years

---

### 3. Growth Analysis

Two-column layout showing growth dynamics:

#### Left Column: Growth Rate Charts

- **Top chart**: Quarter-over-Quarter (QoQ) growth
  - Shows short-term acceleration/deceleration
  - Expect high volatility due to seasonality
  - Red dashed line = 0% growth baseline

- **Bottom chart**: Year-over-Year (YoY) growth
  - Shows annual growth trends
  - Less volatile, more strategic metric
  - Indicates long-term health

#### Right Column: Growth Metrics Summary

- **Avg QoQ Growth**: Average quarter-to-quarter change (~18.8%)
- **Avg YoY Growth**: Average year-to-year change (~14.9%)
- **Total Growth**: Overall expansion from 2020 to 2025

**Interpretation:**

- QoQ > 0%: Positive short-term momentum
- YoY > 0%: Positive long-term trend
- ~15% YoY is healthy, sustainable growth

---

### 4. Usage Patterns Analysis

Three tabs analyzing temporal patterns:

#### Tab 1: Hourly Patterns

- **X-axis**: Hour of day (0-23)
- **Y-axis**: Number of trips
- **Lines**: Weekday (blue) vs Weekend (orange)

**What to look for:**

- Weekday peaks during commute hours (7-9 AM, 4-6 PM)
- Weekend peaks during afternoon leisure time
- Off-peak hours for maintenance scheduling

#### Tab 2: Daily Patterns

- **Shows**: Trip volume by day of week
- **Format**: Bar chart
- **Peak indicator**: Shows busiest day

**Insights:**

- Identify low-demand days for maintenance
- Plan staffing and bike redistribution

#### Tab 3: Monthly Heatmap

- **Rows**: Months (Jan-Dec)
- **Columns**: Years (2020-2025)
- **Color**: Intensity = trip volume

**How to read:**

- Darker colors = higher activity
- Consistent summer peaks visible
- Winter troughs evident

---

### 5. Station Analysis

#### Left Side: Top Stations Chart

- **Interactive slider**: Adjust number of stations displayed (5-30)
- **Metric**: Total activity (departures + arrivals)
- **Format**: Horizontal bar chart

**Use cases:**

- Identify high-demand locations for capacity expansion
- Target stations for infrastructure upgrades
- Recognize successful locations for replication

#### Right Side: Statistics Panel

- **Avg Trips per Station**: Measure of utilization evenness
- **Max/Min Trips**: Identify outliers
- **Top 5 Table**: Quick reference for busiest stations

---

### 6. Advanced Analytics

Two detailed analysis tabs:

#### Tab 1: Duration Distribution

- **Shows**: Histogram of trip durations (0-60 minutes)
- **Below chart**: Mean, median, and mode statistics

**Insights:**

- Most common trip duration
- Distribution shape (normal, skewed, bimodal)
- Outlier identification

#### Tab 2: Multi-Metric Comparison

- **Format**: 2x2 grid of charts
  - Top-left: Total Trips
  - Top-right: Total Ride Minutes
  - Bottom-left: Unique Bikes
  - Bottom-right: Active Stations

**Purpose:**

- Compare growth trajectories
- Identify metric correlations
- Spot infrastructure gaps

---

### 7. Data Explorer

Interactive section for deep dives:

#### Tab 1: Trip Data Explorer

**Filters:**

1. **Years**: Select one or multiple years
2. **Quarters**: Choose specific quarters (Q1-Q4)
3. **Day Type**: Weekday, Weekend, or both

**Features:**

- Shows filtered record count
- Displays first 1,000 rows of filtered data
- **Download button**: Export filtered data as CSV

**Use cases:**

- Custom analysis in external tools
- Detailed investigation of specific periods
- Data sharing with stakeholders

#### Tab 2: Quarterly Summary

- **Shows**: Aggregated statistics by quarter
- All growth metrics included
- **Download button**: Export summary as CSV

---

### 8. Key Insights & Recommendations

Strategic summary section:

#### Left Column: Key Findings

Five main discoveries from the analysis:

1. Sustainable growth rate
2. Strong seasonality patterns
3. Trip maturity indicators
4. Consistent adoption trends
5. Infrastructure alignment

#### Right Column: Strategic Recommendations

Five actionable recommendations:

1. Maintain sustainable expansion pace
2. Address seasonal dips
3. Optimize station placement
4. Enhance user retention
5. Implement predictive analytics

**How to use:**

- Share with decision-makers
- Reference for strategic planning
- Basis for budget proposals

---

## Sidebar Navigation

Located on the left side (collapsible):

### Dataset Overview

- Total records
- Date range
- Coverage statistics

### About Section

- Data source information
- Analysis period
- Project context

### Navigation Guide

- Quick links to sections
- Feature descriptions

**Tip**: Collapse sidebar for more screen space

---

## Tips & Best Practices

### Performance

1. **First load**: May take 30-60 seconds to load all data
2. **Subsequent loads**: Data is cached for faster access
3. **Filter large datasets**: Use Data Explorer filters to improve performance

### Navigation

1. **Scroll smoothly**: Dashboard is designed for top-to-bottom exploration
2. **Use tabs**: Each section has multiple views accessible via tabs
3. **Interactive elements**: Hover over charts for detailed values

### Data Export

1. **CSV downloads**: Available in Data Explorer section
2. **Screenshots**: Use browser tools to capture visualizations
3. **Copy data**: Select and copy from dataframe displays

### Interpretation

1. **Context matters**: Consider seasonality when evaluating growth
2. **Multiple metrics**: Cross-reference different indicators
3. **Time horizons**: Use QoQ for tactics, YoY for strategy

---

## Troubleshooting

### Dashboard won't start

```bash
# Ensure all dependencies are installed
pip install -r requirements.txt

# Try running directly
cd src
streamlit run app.py
```

### Data not loading

- Check that `data/` directory exists
- Verify CSV files are present
- Ensure file naming pattern: `indego-trips-YYYY-qQ.csv`

### Charts not displaying

- Clear cache: In terminal, press `C` then `Enter`
- Refresh browser: `Cmd/Ctrl + R`
- Clear browser cache

### Performance issues

- Reduce date range in filters
- Limit top N stations to fewer items
- Close other browser tabs
- Run: `streamlit cache clear`

---

## Keyboard Shortcuts

When dashboard is running in terminal:

- `C` + `Enter`: Clear cache and rerun
- `R` + `Enter`: Rerun without clearing cache
- `Ctrl + C`: Stop the dashboard

In browser:

- `Cmd/Ctrl + R`: Refresh page
- `Cmd/Ctrl + Shift + R`: Hard refresh (clear cache)
- `Cmd/Ctrl + F`: Find on page

---

## Advanced Usage

### Custom Port

```bash
streamlit run src/app.py --server.port 8080
```

### Dark Theme

```bash
streamlit run src/app.py --theme.base dark
```

### Headless Mode (Server)

```bash
streamlit run src/app.py --server.headless true
```

### Configuration File

Create `.streamlit/config.toml`:

```toml
[server]
port = 8501
headless = false

[theme]
primaryColor = "#1f77b4"
```

---

## Getting Help

### Common Questions

**Q: How often is data updated?**
A: Dashboard reads from CSV files in `data/` directory. Update files to see new data.

**Q: Can I filter by specific date ranges?**
A: Yes, use the Data Explorer section with year/quarter filters.

**Q: How do I export visualizations?**
A: Right-click charts and "Save image as..." or use browser screenshot tools.

**Q: Can I modify the dashboard?**
A: Yes! Edit files in `src/` directory. See `src/README.md` for customization guide.

**Q: Why are there gaps in some quarters?**
A: If data files are missing for certain quarters, they won't appear in visualizations.

### Support Resources

- **Code documentation**: See inline comments in source files
- **Technical details**: Read `src/README.md`
- **Project context**: See main `README.md`
- **Streamlit docs**: <https://docs.streamlit.io>

---

## Next Steps

After exploring the dashboard:

1. **Share insights**: Export charts and summaries for presentations
2. **Deep dive**: Use Data Explorer for custom analysis
3. **Take action**: Implement strategic recommendations
4. **Monitor trends**: Re-run dashboard with updated data regularly
5. **Customize**: Modify code to add organization-specific metrics

---

## Feedback & Improvements

The dashboard is designed to be extensible. Consider adding:

- Geographic mapping of stations
- Weather correlation analysis
- User demographic breakdown (if data available)
- Predictive demand modeling
- Real-time data integration
- Mobile-responsive views

---

**Happy analyzing!** 🚴
