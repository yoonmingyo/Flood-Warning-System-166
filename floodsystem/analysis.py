
import numpy as np
import matplotlib
import matplotlib.dates
import scipy as sp
from .station import MonitoringStation
from .stationdata import build_station_list, update_water_levels

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

def grad(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels

    p_grad = np.polyfit(x, y, p)

    recent=matplotlib.dates.date2num(dates[1])
    later=matplotlib.dates.date2num(dates[2])
    y2 = np.polyval(p_grad,recent)
    y1 = np.polyval(p_grad,later)
    grad=(y2-y1)/(recent-later)
    return grad