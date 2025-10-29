#!/bin/bash

# Indego Bike Share Dashboard Launcher
# This script launches the Streamlit dashboard

echo "=========================================="
echo "  Indego Bike Share Analytics Dashboard  "
echo "=========================================="
echo ""

# Check if streamlit is installed
if ! command -v streamlit &> /dev/null
then
    echo "Streamlit is not installed. Installing requirements..."
    pip install -r requirements.txt
fi

# Launch the dashboard
echo "Starting dashboard..."
echo "Dashboard will open in your default browser"
echo "Press Ctrl+C to stop the dashboard"
echo ""

cd src && streamlit run app.py --server.port 8501

# Alternative: Run from project root
# streamlit run src/app.py --server.port 8501

