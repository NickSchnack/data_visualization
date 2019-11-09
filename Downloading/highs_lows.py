import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Get dates and high temperatures from file
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows, diffs = [], [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
            diff = high - low
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            diffs.append(diff)

# Plot the data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.plot(dates, diffs, c='green', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha=0.1)
plt.fill_between(dates, 0, diffs, facecolor = 'green', alpha=0.1)
fig.autofmt_xdate()

# Format the plot.
plt.title("Daily highs, lows, and temperature differences, 2014\nDeath Valley, CA", fontsize=20)
plt.xlabel('', fontsize=20)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

# Show the data.
plt.show()