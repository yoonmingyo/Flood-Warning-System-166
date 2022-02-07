# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

def rivers_with_station(stations):
    """Takes a list of stations and returns a set of all the rivers
    in alphabetic order upon which those stations are located"""
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    rivers = sorted(rivers)
    return rivers

def rivers_by_station_number(stations, N):
    """Returns a list of the N rivers with the
    greatest number of monitoring stations"""

    stations_b_r = stations_by_river(stations)


    number_of_stations = sorted_by_key([(river,len(stations)) for river, stations in stations_b_r.items()],1,True)

    print_nos = number_of_stations[:N]
    i = N+1
    while True:
        if print_nos[-1][1] == number_of_stations[i][1]:
            print_nos.append(number_of_stations[i])
            i+=1
        else:
            break

    return print_nos


def haversine_formula(x1, y1, x2, y2):
    # difference in x and y
    d_X = (x2 - x1) * math.pi / 180.0
    d_Y = (y2 - y1) * math.pi / 180.0

    # converting x1 and x2 to radians
    x1 = x1 * math.pi / 180.0
    x2 = x2 * math.pi / 180.0

    a= math.sin(d_X/2)**2 + math.cos(x1)*math.cos(x2)*(math.sin(d_Y/2)**2)
    # radius,r of Earth (assuming that it is a perfect sphere)
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

