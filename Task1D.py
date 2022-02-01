from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river


def demo_1():
    """Requirements for Task 1D:
    given a list of station objects,
    returns a list with the names of the rivers with a monitoring station"""

    # Fetch the stations and store as list
    stations = build_station_list()

    # List the rivers
    rivers = rivers_with_station(stations)

    print(rivers)


def demo_2():
    """Requirements for Task 1D:
    printing the names of the stations located on the following rivers in alphabetical order"""

    # Build a list of stations.
    stations = build_station_list()

    # Construct the dict with the list of stations
    rivers_and_stations = stations_by_river(stations)

    # Print the value (list of stations) of selected dict items (with the specified rivers as key)
    print(rivers_and_stations['River Aire'])
    print(rivers_and_stations['River Cam'])
    print(rivers_and_stations['River Thames'])


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    demo_1()
    demo_2()