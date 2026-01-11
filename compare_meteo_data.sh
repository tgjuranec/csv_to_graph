#!/bin/bash
#
#

curl "https://archive-api.open-meteo.com/v1/era5?latitude=45.87&longitude=15.76&start_date=2021-01-01&end_date=2021-12-31&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

echo "time,temp,humidity,wind" > meteo.csv && jq -r '.hourly | ([.time, .temperature_2m, .relative_humidity_2m, .wind_speed_10m] | transpose[] | @csv)' meteo.json >> meteo.csv


