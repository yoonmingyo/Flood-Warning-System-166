import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
import dateutil.parser
import datetime
import numpy as np
from .stationdata import build_station_list
from .analysis import polyfit
import floodsystem.geo
import matplotlib



def plot_water_levels(station, dates, levels):
# Plot

    plt.plot(dates, levels)
    plt.plot([dates[-1], dates[0]], [station.typical_range[0], station.typical_range[0]])
    plt.plot([dates[-1], dates[0]], [station.typical_range[1], station.typical_range[1]])

# Add axis labels, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

# Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    """Plots the historical water levels of station given by dates and levels.
    It then plots those levels along with a polynomial best fit of degree
    p which can then be used to estimate future water levels"""
    plot_water_levels(station, dates, levels)
    best_fit, offset = polyfit(dates, levels, p)

    x = matplotlib.dates.date2num(dates)
    y = best_fit(x - offset)
    plt.plot(dates, y, label="$Best Fit$")
    plt.legend(loc=2)
