from floodsystem.utils import sorted_by_key  # noqa
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_within_radius, stations_by_distance, rivers_with_station, stations_by_river, rivers_by_station_number
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


def test_rivers_with_station():
    """Tests that the function has at least 800 rivers inc. Thames"""
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    assert len(rivers) >= 800
    assert "Thames" in rivers

def test_stations_by_river():
    """Check that certain stations are produced in the list for certain rivers"""
    stations = build_station_list()
    assert "Armley" in stations_by_river(stations, "River Aire")
    assert "Benson Lock" in stations_by_river(stations, "Thames")


def test_rivers_by_station_number():
    """Tests the length of a few outputs and checks order of rivers"""
    stations = build_station_list()
    assert len(rivers_by_station_number(stations, 1)) >= 1
    assert len(rivers_by_station_number(stations, 10)) >= 10
    assert len(rivers_by_station_number(stations, 30)) >= 30
    biggest_river = rivers_by_station_number(stations, 1)
    assert biggest_river[0][0] == "Thames"