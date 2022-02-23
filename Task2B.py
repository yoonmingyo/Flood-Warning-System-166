from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold
def run():
    stations = build_station_list()
    update_water_levels(stations)
    tol = 0.8
    final_list = stations_level_over_threshold(stations, tol)
    for x in final_list:
        print(x[0],x[1])

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
