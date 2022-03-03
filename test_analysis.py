from floodsystem.analysis import polyfit
from matplotlib.dates import num2date
import numpy as np

def test_polyfit(self):
        dates = num2date([5,4,3,2,1])
        levels = [16,9,4,1,0]

        p, d0 = polyfit(dates,levels,2)
        assert round(p[2]) == 1
        assert d0 == 1

        dates = num2date([10,5,4,3,2])
        levels = [57,-18,-3,8,9]

        p, d0 = polyfit(dates,levels,3)
        assert round(p[2]) == -8
        assert d0 == 2
