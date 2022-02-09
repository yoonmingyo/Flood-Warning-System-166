
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
    """Takes a list of stations and returns a set of all the rivers
    in alphabetic order upon which those stations are located"""
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    rivers = sorted(rivers)
    return rivers

def stations_by_river(stations, river):
    """Takes a list of stations and returns a list of all the station names
    on a specific river in alphabetic order"""
    station_names = []
    for station in stations:
        if station.river == river:
            station_names.append(station.name)
    station_names = sorted(station_names)
    return station_names

def rivers_by_station_number(stations, N):
    """Take a list of stations and return the N rivers with the most stations upon
    them, in the form of a list of tuples in descending order"""

    # use another function in geo to build list of non-repeated rivers
    rivers = rivers_with_station(stations)

    # initialise list
    rivers_with_count = []

    for river in rivers:
        count = 0
        for station in stations:
            if station.river == river:
                count += 1

        # now that the number of times the river appears in the station list
        # has been determined, the river can be appended
        rivers_with_count.append((river, count))

    # sort list according to number of rivers
    rivers_with_count = sorted(
        rivers_with_count, key=lambda x: x[1], reverse=True)

    # if the next river has the same number of stations, N must be increased
    # to include this river
    while rivers_with_count[N - 1][1] == rivers_with_count[N][1]:
        N += 1

    return rivers_with_count[:N]


