
# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  
from .stationdata import build_station_list
from .station import MonitoringStation
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


#Task 1D

def rivers_with_station(stations):
    """
    Function that, given a list of station objects,
    returns a container with the names of the rivers with a monitoring station.
    
    Args:
        stations (list): List of stations (MonitoringStation).
    
    Returns:
        set: Set of names of rivers with a monitoring station.
    """

    return {station.river for station in stations}


def stations_by_river(stations):
    """
    Function that returns a dictionary that maps river names (the ‘key’)
    to a list of station objects on a given river.
    
    Args:
        stations (list): List of stations (MonitoringStation).
    
    Returns:
        dict: Keys - river names.
    """

    return {key: list(value) for key, value in groupby(
        sorted(
            stations,
            key=lambda x: x.river
        ),
        lambda x: x.river
    )}


def rivers_by_station_number(stations, N):
    """
    Function that returns a list of tuples containing the river name and the number of stations it has.
    
    Args:
        stations (list): List of stations (MonitoringStation)
        N (int): The number of desired rivers with the largest number of stations
    
    Returns:
        list: tuple of (river, number of stations on river) sorted in descending order
    """

    return list(reduce(
        lambda acc, val: acc + [val] if (len(acc) < N or val[1] == acc[-1][1]) else acc,
        sorted(
            [(key, len(i)) for key, i in stations_by_river(stations).items()],
            key=lambda x: (-x[1], x[0])
        ),
        []
    ))


