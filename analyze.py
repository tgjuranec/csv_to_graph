#!/usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt
from array import array
from matplotlib.dates import DateFormatter

# Read CSV with proper datetime parsing
df = pd.read_csv('ha.csv', parse_dates=[2],na_values=['unavailable'])
df.columns = ['device','temp', 'timestamp']
# Drop all invalid data
df = df.dropna()

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df['timestamp'], df['temp'],linewidth=1.5)
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
y_ticks = [float(x/10) for x in range(int(ymin*10), int((ymax+1)*10), 5)]
print(ymin,ymax)
plt.yticks(y_ticks)
plt.savefig('output_plot.png', dpi=300)


