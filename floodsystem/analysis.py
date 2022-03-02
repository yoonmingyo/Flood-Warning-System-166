
import numpy as np
import matplotlib
import matplotlib.dates
import scipy as sp


def polyfit(dates, levels, p):
    """Returns a polynomial of degree p representing the best fit for a function
    f(dates) = levels. It offsets dates such that the minimum value of the domain
    is equal to 0 to prevent floating point errors. The offset is returned alongside
    the polynomial as (polynomial,offset)."""
    times = matplotlib.dates.date2num(dates)
    d0 = np.min(times)
    times = times - d0
    poly = np.poly1d(np.polyfit(times, levels, p))

    return poly, d0

def flood_warn(stations):
    for station in stations:
        if station.relative_water_level() >= 10 or station.relative_water_level() <=-10:
            continue
        elif station.relative_water_level() >= 2.5:
            station.warning_level = 4
        elif station.relative_water_level() >= 2.1:
            station.warning_level = 3
        elif station.relative_water_level() >= 1.7:
            station.warning_level = 2
        elif station.relative_water_level() >= 1.3:
            station.warning_level = 1
        else:
            station.warning_level = 0


    return stations