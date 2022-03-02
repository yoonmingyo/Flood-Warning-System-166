""" Issue warnings for towns that have stations reading relative water levels
    that indicate possibility for a flood
"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.analysis import flood_warn
import operator

def run():

    # Build stations
    stations = build_station_list()

    # Update station data
    update_water_levels(stations)

    stat_over_thresh = stations_level_over_threshold(stations,1.3)

    just_stat_over_thresh = [i[0] for i in stat_over_thresh]

    warning_stations = flood_warn(just_stat_over_thresh)

    towns_with_warnings = {}

    warning_strings = ('No Warning','Low Risk','Moderate Risk',\
    'High Risk','Severe Risk')

    for station in warning_stations:
        if station.town in towns_with_warnings:
            if station.warning_level > towns_with_warnings[station.town]:
                towns_with_warnings[station.town]=station.warning_level
        else:
            towns_with_warnings[station.town]=station.warning_level

    to_del = []
    for town in towns_with_warnings:
        if towns_with_warnings[town]==None or town == None:
            to_del.append(town)

    for town in to_del:
        del towns_with_warnings[town]


    s_towns_with_warnings = sorted(towns_with_warnings.items(),\
        key=operator.itemgetter(1),reverse=True)

    for town in s_towns_with_warnings:
        if town[1] == None:
            continue
        print("Town name:",town[0])
        print("Warning level:",warning_strings[town[1]])
        print("")


run()