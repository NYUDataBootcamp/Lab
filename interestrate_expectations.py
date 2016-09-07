import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import cm


#
# Read in data frame
#
df = pd.read_csv("mcs_interestrate_change.csv", skiprows=1)

#
# Once we have done this need to set dates as index
#

# First set all days to 1
df["Day"] = 1

# Use pd.to_datetime to convert Month/Day/Year column into a datetime
df["Date"] = pd.to_datetime(df[["Day", "Month", "Year"]])

# Set index
df = df.set_index("Date")

#
# Restrict to data we care about
#
df = df[["Go Up", "Stay the Same", "Go Down"]]

#
# Create bar plot -- Want bi-annual instead of monthly so it is readable
#
data = df.resample("6M").first()

# Plot commands
fig, ax = plt.subplots(figsize=(20, 10))

data.plot(ax=ax, kind="bar", stacked=True, colormap=cm.viridis)

# Set labels
ax.set_xlabel("Time")
ax.set_ylabel("Inflation Expectations (Up/Down/Same)")
fig.suptitle("Evolving Consumer Confidence")
ax.legend(loc=3)

# Fix index
mask = []
years = []
for (idx, date) in enumerate(data.index):
    month, year = date.month, date.year

    if (month is 1) and (year % 5 is 0):
        mask.append(idx)
        years.append(year)

ax.set_xticks(mask)
ax.set_xticklabels(years, horizontalalignment='center')
plt.xticks(rotation=0)

plt.show()

