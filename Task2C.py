from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold


def run():
    stations = build_station_list()
    update_water_levels(stations)
    N = 10
    highest_list = stations_highest_rel_level(stations,N)
    for station,level in highest_list:
        print(station.name,level)

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
