from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime

stations = build_station_list()
update_water_levels(stations)

names = stations_highest_rel_level(stations, 100)
list_names=[]
for name in names:
    list_names.append(name[0])

stations = build_station_list()
update_water_levels(stations)

deviation_water_level = []
def stations_highest_dev(stations, N):
    for station in stations:
        if station.name in list_names:
            dt = 5
            dates, levels = fetch_measure_levels(station.measure_id,
                                             dt=datetime.timedelta(days=dt))
            if len(dates)==0:
                print ("NO AVAILABLE DATA for:", station.name)
            else:
                total=0
                for level in levels:
                    total+=level
                    area=total-(len(levels)*station.typical_range[1])
            deviation_water_level.append((station.name, area))
    deviation_water_level.sort(key=lambda tup: tup[1], reverse = True)
    return deviation_water_level[:N]