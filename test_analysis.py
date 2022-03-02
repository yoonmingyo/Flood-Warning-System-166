""" Unit test for analysis module"""

from floodsystem.analysis import *
from dateutil.parser import parse
from matplotlib.dates import date2num

def test_poltfit():

    dates = [parse("01/01/15"),parse("01/02/15"),parse("01/03/15"),\
        parse("01/04/15"),parse("01/05/15"),parse("01/06/15")]

    levels = [0,1,2,3,4,5]

    assert 1-(polyfit(dates,levels,1))[0][1] < 0.000001
    assert (polyfit(dates,levels,1))[1] ==date2num(parse("01/06/15"))
