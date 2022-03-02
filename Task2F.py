import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level

def run():
    # Build list of stations
    stations = build_station_list()

    # Find 5 stations at which current relative water level is greatest
    N = 5
    highest_waterlevel_stations = stations_highest_rel_level(stations, N)

    # Desired number of days to plot is 2, polynomial degree is 4
    dt = 10
    p = 4

    # Plot water levels over time for these stations
    # For clarity, plot each station individually
    for station in highest_waterlevel_stations:
        try:
            measure_id = station.measure_id
            dates, levels = fetch_measure_levels(measure_id, datetime.timedelta(days=dt))
            plot_water_level_with_fit(station, dates, levels, p)
            
        except IndexError: # Some stations have faulty data - will not plot a useful graph
            pass

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
