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