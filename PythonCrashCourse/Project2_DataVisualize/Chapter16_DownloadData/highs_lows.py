# ----------------------
# Author: blateyang
# Date: 2018/3/14
# ----------------------

"""Download weather data in csv form and visualize it """

import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Read data from csv file
# filename = 'sitka_weather_07-2014.csv'
filename = 'death_valley_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            # strptime() transform str to time class
            date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[2])
        except ValueError:
            print(date, ' missing data')
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

print(header_row)
# print(highs)
# print(lows)

# Plot high temperature graph
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, 'r', alpha=0.5)
plt.plot(dates, lows, 'b', alpha=0.5)
plt.fill_between(dates, lows, highs, alpha=0.1)
# plt.title('Daily high temperatures, July 2014')
plt.title('Daily high and low temperatures, 2014')
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()  # plot slope date label
plt.ylabel('Temperature (F)')
plt.show()