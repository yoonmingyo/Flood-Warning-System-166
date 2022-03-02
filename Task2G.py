from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.dev import stations_highest_dev
from floodsystem.analysis import grad
import datetime

def plot_graph(risk_level):
    for sample in risk_level:
        for station in stations:
                if station.name == sample:
                    dt = 5
                    dates, levels = fetch_measure_levels(station.measure_id,
                                                     dt=datetime.timedelta(days=dt))
                    if len(dates)==0:
                        print ("NO AVAILABLE DATA for:", station.name)
                    else:
                        plot_water_level_with_fit(station, dates, levels, 4)
                        #print ("Gradient of curve:", grad(dates,levels,4))
                        grad_risk.append((station.name, grad(dates,levels,4)))

stations = build_station_list()
update_water_levels(stations)

#dev = stations_highest_dev(stations, 10)

grad_risk = []
n = 12
area_risk = stations_highest_dev(stations, n)
high_dev=[]

for a in area_risk:
    high_dev.append(a[0])

for sample in high_dev:
    for station in stations:
            if station.name == sample:
                dt = 5
                dates, levels = fetch_measure_levels(station.measure_id,
                                                 dt=datetime.timedelta(days=dt))
                if len(dates)==0:
                    print ("NO AVAILABLE DATA for:", station.name)
                else:
                    grad_risk.append((station.name, grad(dates,levels,4)))

grad_risk.sort(key=lambda tup: tup[1], reverse = True)

scaled_area=[]
for i in area_risk:
    x=(i[1]-area_risk[-1][1])/(area_risk[0][1]-area_risk[-1][1])
    scaled_area.append((i[0],x))

scaled_grad=[]
for j in grad_risk:
    x=(j[1]-grad_risk[-1][1])/(grad_risk[0][1]-grad_risk[-1][1])
    scaled_grad.append((j[0],x))

#print (scaled_area)
#print (scaled_grad)

combined_risk=[]
for r in scaled_area:
    for g in scaled_grad:
        if g[0]==r[0]:
            combined_risk.append((g[0],0.4*r[1]+0.6*g[1]))

#print("Combined risk")
#print (combined_risk)

low=[]
moderate=[]
high=[]
severe=[]

for c in combined_risk:
    if 0<c[1]<=(0.25*combined_risk[0][1]):
        low.append(c[0])
    elif (0.25*combined_risk[0][1])<c[1]<=(0.5*combined_risk[0][1]):
        moderate.append(c[0])
    elif (0.5*combined_risk[0][1])<c[1]<=(0.75*combined_risk[0][1]):
        high.append(c[0])
    elif (0.75*combined_risk[0][1])<c[1]<=(combined_risk[0][1]):
        severe.append(c[0])

print ("low risk: ", low)
print ("moderate risk: ", moderate)
print ("high risk: ", high)
print ("severe risk: ", severe)

print ("LOW RISK STATIONS")
plot_graph(low)
print ("MODERATE RISK STATIONS")
plot_graph(moderate)
print ("HIGH RISK STATIONS")
plot_graph(high)
print ("SEVERE RISK STATIONS")
plot_graph(severe)