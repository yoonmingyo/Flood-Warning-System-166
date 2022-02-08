from floodsystem.utils import sorted_by_key  # noqa
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import haversine_formula
from floodsystem.station import inconsistent_typical_range_stations

stations = build_station_list()
centre = [52.2053,0.1218]
r = 10


def test_stations_by_distance(stations):
    a = stations_by_distance(stations)
    for x in range(1,len(a)):
        before = a[x-1]
        after = a[x]
    assert before[2] < after[2] 

def test_stations_within_radius(stations):
    b = stations_within_radius(stations, centre, r)
    assert len(b) == 11
    for station in b:
        assert haversine_formula(station.coord[0], station.coord[1], centre[0], centre[1]) <= r


