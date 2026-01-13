#!/bin/bash
#
#

DATE1="2026-01-04"
DATE2="2026-01-13"

source .venv/bin/activate

curl "https://archive-api.open-meteo.com/v1/era5?latitude=45.87&longitude=15.76&start_date=$DATE1&end_date=$DATE2&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m" > meteo.json

echo "time,temp,humidity,wind" > meteo.csv && jq -r '.hourly | ([.time, .temperature_2m, .relative_humidity_2m, .wind_speed_10m] | transpose[] | @csv)' meteo.json >> meteo.csv

python3 analyze.py
