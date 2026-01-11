#!/usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt
from array import array
from matplotlib.dates import DateFormatter
import os.path
import math

N_YTICKS = 10

# READING HOMEASSISTANT FILE
if os.path.isfile("ha.csv"):
    # Read CSV with proper datetime parsing
    df = pd.read_csv('ha.csv', parse_dates=[2],na_values=['unavailable'])
    df.columns = ['device','temp', 'timestamp']
    # Drop all invalid data
    df = df.dropna()

# READING OPEN-METEO FILE
if os.path.isfile("meteo.csv"):
    # Read CSV with proper datetime parsing
    df_meteo = pd.read_csv('meteo.csv', parse_dates=[0],na_values=['unavailable'])
    df_meteo.columns = ['timestamp','temp', 'humidity','wind']
    # Drop all invalid data
    df = df.dropna()
    df['temp'] = df['temp']-6.



fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df['timestamp'], df['temp'],df_meteo["timestamp"],df_meteo["temp"], linewidth=1.5)
# Format x-axis as DD-HH-MM
date_format = DateFormatter('%d-%H-%M')
ax.xaxis.set_major_formatter(date_format)



# Create plot

plt.grid(True,which='major',alpha=0.3)
plt.tight_layout()
ax.set_xlabel('Time')
ax.set_ylabel('Value')
ax.set_title('Temperature ')
ax.grid(True, alpha=0.3)


ymin,ymax = plt.ylim()
ytickmin = int(math.floor(ymin/10))*10
ytickmax = int(math.ceil(ymax/10)+1)*10
iStep = (ytickmax-ytickmin)//N_YTICKS
print(ymin,ymax,iStep)
y_ticks = [float(x) for x in range(ytickmin, ytickmax, iStep)]
plt.yticks(y_ticks)
plt.savefig('output_plot.png', dpi=300)


