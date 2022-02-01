from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Requirements for Task 1F"""

    # Build list of stations with inconsistent range data
    stations = build_station_list()
    inconsistentStations = inconsistent_typical_range_stations(stations)

    # Create list containing just the names of these stations
    inconsistentStationNames = []
    for station in inconsistentStations:
        inconsistentStationNames.append(station.name)
    
    # Sort list alphabetically and print
    inconsistentStationNames = sorted(inconsistentStationNames)
    print(inconsistentStationNames)


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
