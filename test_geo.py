"""Test for geo module"""

from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def test_stations_by_distance():
    # Build list of 20 stations by distance from engineering dept
    stationlist = build_station_list()
    selected_stations = stationlist[0:19]
    distancelist = stations_by_distance(selected_stations, (52.19773811278152, 0.12101715637660952))

    # Check that the list contains the correct type of information
    assert isinstance(distancelist[1][0], str)
    assert isinstance(distancelist[1][1], str)
    assert isinstance(distancelist[1][2], float)

    # Check that the list is sorted by distance
    for i in range(len(distancelist) - 1):
        assert distancelist[i][2] < distancelist[i+1][2]