# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  
from .stationdata import build_station_list
from .station import MonitoringStation
import numpy
import math

# Task 1B
def haversine_formula(x1, y1, x2, y2):
    # difference in latitudes and longtitudes
    d_X = (x2 - x1) * math.pi / 180.0
    d_Y = (y2 - y1) * math.pi / 180.0

    # degrees to radians
    x1 = x1 * math.pi / 180.0
    x2 = x2 * math.pi / 180.0

    a= math.sin(d_X/2)**2 + math.cos(x1)*math.cos(x2)*(math.sin(d_Y/2)**2)
    # radius of Earth 
    r = 6371
    distance = 2*r* math.asin(math.sqrt(a))
    return distance

def stations_by_distance(stations, p):
    station_distance = []
    for station in stations:
        coord_p_distance = haversine_formula(station.coord[0], station.coord[1], p[0], p[1])
        name_distance = station.name, station.town, coord_p_distance
        station_distance.append(name_distance)
    sorted_stations = sorted_by_key(station_distance, 2, reverse=False)


    return sorted_stations

#Task 1C

def stations_within_radius(stations, centre, r):
    stations_within = []
    for station in stations:
        if haversine_formula(station.coord[0], station.coord[1],centre[0],centre[1]) < r :
            stations_within.append(station.name)
        else :
            stations_within = stations_within
    return stations_within

    
def rivers_with_station(stations):
    river_station = []
    for station in stations :
        if station.name not in river_station:
            river_station.append(station.name)
    return river_station


