from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    # Set coordinate from which to measure distance
    p = (52.2053, 0.1218)

    # Build stations by distance
    station_distances = stations_by_distance(stations, p)

    # Return 10 closest and furthest stations
    tenClosest = station_distances[:10]
    tenFurthest = station_distances[-10:]
    print("Ten closest stations:\n{}".format(tenClosest))
    print("Ten furthest stations:\n{}".format(tenFurthest))


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
