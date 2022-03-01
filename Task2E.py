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
    dateslist = []
    levelslist = []
    for station in highest_waterlevel_stations:
        measure_id = station.measure_id
        dates, levels = fetch_measure_levels(measure_id, datetime.timedelta(days=dt))
        dateslist.append(dates)
        levelslist.append(levels)
    
    plot_water_levels(highest_waterlevel_stations, dateslist, levelslist)



    


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
