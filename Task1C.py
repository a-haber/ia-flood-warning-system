from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


def run():
    """Requirements for Task 1C"""

    # Build list of stations, set centre coordinates and required radius
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 10 # distance in km

    # Build list of stations which are within the radius
    within_radius = stations_within_radius(stations, centre, r)
    
    #sort list by alphabetical order and print
    within_radius = sorted(within_radius)
    print("Stations within {} km:".format(r))
    print(within_radius)


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
