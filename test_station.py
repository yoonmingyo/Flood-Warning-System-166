# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_typical_range_stations():
    test_station = MonitoringStation(None,None,None,None,None,None,None)
    test_station_2 = MonitoringStation("x","x","x",(0,0),(5,3),"x","x")
    assert test_station.typical_range_consistent() == False
    assert test_station_2.typical_range_consistent() == False


'''def test_inconsistent_typical_range_stations():
    """Ensures that all the stations returned by inconsistent_typical_range_stations
    are actually inconsisten (assumes that inconsistent testing works correctly)
    """
    stations = build_station_list()
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    for s in inconsistent_stations:
        assert not s.typical_range_consistent()
'''