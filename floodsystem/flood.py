from .stationdata import build_station_list, update_water_levels
from .station import MonitoringStation
from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    over_threshold =  []
    for station in stations :
        relative_level = station.relative_water_level()
        if relative_level is not None:
            if relative_level > tol:
                over_threshold.append((station,station.relative_water_level()))
    k = sorted_by_key(over_threshold, 1, reverse = True)
    return k

def stations_highest_rel_level(stations,N):
    mylist =[]
    for n in range(0,N):
        mylist.append(stations_level_over_threshold(stations,-999)[n])
        # Negative number for tolerance to make sure all the stations are included
    return mylist


#altered code to match Task2F

def stations_highest_rel_level_2(stations,N):
    mylist =[]
    for station in stations :
        relative_level = station.relative_water_level()
        if relative_level is not None:
                mylist.append((station.name,station.relative_water_level()))
    k = sorted_by_key(mylist, 1, reverse = True)
    return k[:N]


    '''for station in stations :
        relative_level = station.relative_water_level()
        if relative_level is not None:
                #mylist.append((station,station.relative_water_level()))
                mylist.append(stations_level_over_threshold(stations,-99999)[n])
    k = sorted_by_key(mylist, 1, reverse = True)
    return k[:N]'''