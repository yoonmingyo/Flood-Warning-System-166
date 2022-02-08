# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_distance
from floodsystem.geo import haversine_formula


def run():
    stations = build_station_list()
    p = [52.2053, 0.1218]

    a = stations_by_distance(stations, p)
    closest = a[:10]
    furthest = a[-10:]

    print(closest)
    print(furthest)


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
