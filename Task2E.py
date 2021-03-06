import matplotlib.pyplot as plt
import datetime
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from floodsystem.utils import sorted_by_key


'''def stations_highest_rel_level_2(stations,N):
    mylist =[]
    for station in stations :
        relative_level = station.relative_water_level()
        if relative_level is not None:
                mylist.append((station,station.relative_water_level(),station.measure_id))
    k = sorted_by_key(mylist, 1, reverse = True)
    return k[:N]'''

def run():

    stations = build_station_list()
    update_water_levels(stations)
    selected = stations_highest_rel_level(stations,6)
    # 6 instead of 5 as the first station has no data for levels and dates (one station is ignored so need N=6 for 5 stations to be displayed)
    #print(selected)
    for station, level in selected:
        dt = 10
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        if len(dates) == 0 or len(levels) == 0:
            continue  # Deal with empty lists appearing
        plot_water_levels(station, dates, levels)



if __name__ == "__main__":
    print("*** Task 2E: CUED Part IE Flood Warning System ***")

    # Run Task2E
    run()