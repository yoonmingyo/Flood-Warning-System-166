from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_within_radius
from floodsystem.geo import haversine_formula

def run():
    stations = build_station_list()
    centre = [52.2053, 0.1218]
    r = 10
    a = stations_within_radius(stations, centre, r)
    b = sorted(a)
    print(b)


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
