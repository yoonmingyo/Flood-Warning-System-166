'''from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
import matplotlib
import matplotlib.dates
import numpy as np

def test_polyfit():
        dates = matplotlib.dates.date2num([5,4,3,2,1])
        levels = [16,9,4,1,0]

        p, d0 = polyfit(dates,levels,2)
        assert round(p[2]) == 1
        assert d0 == 1

        dates = matplotlib.dates.date2num([10,5,4,3,2])
        levels = [57,-18,-3,8,9]

        p, d0 = polyfit(dates,levels,3)
        assert round(p[2]) == -8
        assert d0 == 2'''
    
from floodsystem.analysis import *
import datetime
from dateutil.parser import parse
from matplotlib.dates import date2num

def test_poltfit():

    dates = [parse("01/01/15"),parse("01/02/15"),parse("01/03/15"),\
        parse("01/04/15"),parse("01/05/15"),parse("01/06/15")]

    levels = [0,1,2,3,4,5]

    assert 1-(polyfit(dates,levels,1))[0][1] < 0.000001
    assert (polyfit(dates,levels,1))[1] ==date2num(parse("01/06/15"))-5

