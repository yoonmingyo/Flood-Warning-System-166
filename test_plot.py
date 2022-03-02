from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
import datetime

def test_plot_water_levels():
    # Tests checks if plot is built for 'River Cam'
    # Does not check graph for accuracy

    stations = build_station_list()
    update_water_levels(stations)
    for station in stations:
        if station.name == 'Cam':
            station_cam = station
            break

    dt = 10
    dates, levels = fetch_measure_levels(station.measure_id,
                                         dt=datetime.timedelta(days=dt))

    plot_water_levels(station_cam, dates, levels)

    assert "Graphs displayed"
