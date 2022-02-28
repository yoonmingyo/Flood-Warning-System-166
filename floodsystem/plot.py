import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels

import numpy as np
from bokeh.io import output_file
from bokeh.models import DatetimeTickFormatter, Span, BoxAnnotation
from bokeh.plotting import figure
from matplotlib.dates import date2num
from analysis import polyfit

def plot_water_levels(station, dates, levels):
# Plot
    plt.plot(dates, levels)

# Add axis labels, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station)

# Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    """
    Function that makes a graph of the water level over time for a given station with a least-square fit polynomial with a degree of p.
    Args:
        station (MonitoringStation): The desired station to graph.
        dates (list): The list of dates for the x-axis.
        levels (list): The corresponding water level for each date, y-axis.
        p (int): The degree of polynomial that is desired.
    Returns:
        Bokeh plot object.
    """
    output_file(station.name + ".html")
    graph = figure(title=station.name, x_axis_label="Date", y_axis_label="Water level (m)")
    graph.line(dates, levels, line_width=2)
    poly, d0 = polyfit(dates, levels, p)
    graph.line(dates, [poly(date - d0) for date in date2num(dates)], line_width=2, line_color='orange')
    low = Span(location=station.typical_range[0], dimension='width', line_color='gray', line_dash="4 4", line_width=2)
    graph.add_layout(low)
    high = Span(location=station.typical_range[1], dimension='width', line_color='gray', line_dash="4 4", line_width=2)
    graph.add_layout(high)
    low_box = BoxAnnotation(top=station.typical_range[0], fill_alpha=0.1, fill_color='gray')
    mid_box = BoxAnnotation(bottom=station.typical_range[0], top=station.typical_range[1], fill_alpha=0.1,
                            fill_color='green')
    high_box = BoxAnnotation(bottom=station.typical_range[1], fill_alpha=0.1, fill_color='red')
    graph.add_layout(low_box)
    graph.add_layout(mid_box)
    graph.add_layout(high_box)
    graph.xaxis.formatter = DatetimeTickFormatter(
        hours=["%d %B %Y"],
        days=["%d %B %Y"],
        months=["%d %B %Y"],
        years=["%d %B %Y"],
    )
    graph.xaxis.major_label_orientation = np.pi / 4
    return graph