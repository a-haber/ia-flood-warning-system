"""Test for geo module"""

from numpy import geomspace
from floodsystem.geo import rivers_by_station_number, rivers_with_station, stations_by_distance, stations_by_river, stations_within_radius
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from os import path
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

def test_rivers_with_station():
    # Tests that the function has at least 900 rivers and Allison Dyke is in rivers
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    # Check if there are more stations than 900 (there should be 949 or 950, depending on the day)
    assert len(rivers) >= 900
    # Check if the Allison Dyke is in rivers
    assert "Allison Dyke" in rivers

# Task 1E
def test_rivers_by_station_number():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "station"
    coord = (1, 1)
    trange = None
    river1 = "River 1"
    river2 = "River 2"
    river3 = "River 3"
    river4 = "River 4"
    town = "Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river1, town)
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river2, town)
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river1, town)
    s4 = MonitoringStation(s_id, m_id, label, coord, trange, river3, town)
    s5 = MonitoringStation(s_id, m_id, label, coord, trange, river2, town)
    s6 = MonitoringStation(s_id, m_id, label, coord, trange, river1, town)
    s7 = MonitoringStation(s_id, m_id, label, coord, trange, river3, town)
    s8 = MonitoringStation(s_id, m_id, label, coord, trange, river4, town)
    stations = [s1, s2, s3, s4, s5, s6, s7, s8]

    assert len(rivers_by_station_number(stations, 1)) == 1

    river_list = rivers_by_station_number(stations, 2)

    # Multiple entries with same number in Nth position
    assert len(river_list) == 3

    assert "River 4" not in [item[0] for item in river_list]

    for river in ["River 1", "River 2", "River 3"]:
        assert river in [item[0] for item in river_list]

#  Milestone 1 finished – ready for marking