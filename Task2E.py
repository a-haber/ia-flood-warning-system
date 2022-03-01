import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():

    # Build list of stations
    stations = build_station_list()

    # Find 5 stations at which current relative water level is greatest
    N = 5
    highest_waterlevel_stations = stations_highest_rel_level(stations, N)

    # Desired number of days to plot is 10
    dt = 10

    # Plot water levels over past 10 days for these stations

    # NB - NEED TO CHANGE THIS ONCE stations_highest_rel_level IS FIXED
    for station in highest_waterlevel_stations:
        for i in stations:
            if i.name == station[0]:
                measure_id = i.measure_id
                dates, levels = fetch_measure_levels(measure_id, datetime.timedelta(days=dt)) # WILL NEED TO CHANGE station[0] TO station.measure_id 
                plot_water_levels(i, dates, levels)


    


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
