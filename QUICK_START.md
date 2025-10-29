# Quick Start Guide

## Run the Dashboard in 3 Steps

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Verify Setup (Optional)

```bash
python verify_setup.py
```

### Step 3: Launch Dashboard

```bash
./run_dashboard.sh
```

**OR**

```bash
streamlit run src/app.py
```

The dashboard will open automatically in your browser at `http://localhost:8501`

---

## What You'll See

### Main Sections (in order)

1. **KPI Cards** - Quick metrics overview
2. **Time Series** - Quarterly trends (4 tabs)
3. **Growth Analysis** - QoQ & YoY rates
4. **Usage Patterns** - Hourly, daily, monthly (3 tabs)
5. **Station Analysis** - Top stations & stats
6. **Advanced Analytics** - Distribution & comparisons (2 tabs)
7. **Data Explorer** - Filter & export data (2 tabs)
8. **Insights** - Key findings & recommendations

---

## Quick Tips

### Navigation

- **Scroll** down to explore all sections
- **Click tabs** to see different views
- **Use sidebar** for dataset info (collapsible)

### Interaction

- **Adjust sliders** to change number of stations shown
- **Select filters** in Data Explorer to narrow data
- **Download** filtered data as CSV

### Performance

- First load takes ~30-60 seconds (loading 5.9M records)
- Subsequent loads are cached and fast (~2-5 seconds)
- Use filters to speed up large analyses

---

## Keyboard Shortcuts

**In Terminal (while running):**

- `C` + `Enter` - Clear cache and rerun
- `R` + `Enter` - Rerun without clearing
- `Ctrl + C` - Stop dashboard

**In Browser:**

- `Cmd/Ctrl + R` - Refresh page
- `Cmd/Ctrl + F` - Find on page

---

## Troubleshooting

### Issue: "Module not found"

```bash
pip install -r requirements.txt
```

### Issue: "No CSV files found"

- Ensure `data/` directory exists
- Check CSV files are present

### Issue: Dashboard is slow

- Clear cache: Press `C` in terminal
- Reduce date filters
- Limit top N stations

### Issue: Charts not showing

- Refresh browser: `Cmd/Ctrl + R`
- Clear Streamlit cache
- Check terminal for errors

---

## Need More Help?

- **Comprehensive Guide**: See `DASHBOARD_GUIDE.md`
- **Technical Details**: See `src/README.md`
- **Implementation**: See `STREAMLIT_APP_SUMMARY.md`
- **Project Overview**: See main `README.md`

---

## File Structure Overview

```
perpay-bike-share-challenge/
├── src/                    # Source code
│   ├── app.py             # Main dashboard
│   ├── config.py          # Configuration
│   ├── data_loader.py     # Data loading
│   ├── metrics.py         # KPI calculations
│   └── visualizations.py  # Charts
├── data/                  # CSV files (23 quarters)
├── run_dashboard.sh       # Launch script
├── verify_setup.py        # Setup checker
├── requirements.txt       # Dependencies
└── *.md                   # Documentation
```

---

**Ready to explore!** 🚴

Launch the dashboard and start analyzing Indego Bike Share data!
