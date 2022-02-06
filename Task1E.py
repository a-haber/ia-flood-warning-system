from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    """Requirements for Task 1E:"""

    # Fetch the stations and store as list
    stations = build_station_list()

    # List the rivers
    print(rivers_by_station_number(stations, 9))


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
