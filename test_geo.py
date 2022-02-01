"""Test for geo module"""

from floodsystem.geo import stations_by_distance, stations_within_radius
from floodsystem.stationdata import build_station_list
from haversine import haversine

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

def test_stations_within_radius():
    # Build list of stations within 10km of cambridge city centre
    stationlist = build_station_list()
    centre = (52.2053, 0.1218)
    radius = 10
    stations_to_test = stations_within_radius(stationlist, centre, radius)
    
    # Test up to 5 stations to ensure they are within the radius
    count = 0
    for station in stationlist:
        if station.name in stations_to_test:
            assert haversine(station.coord, centre) < radius
            count += 1
            if count > 4:
                break
