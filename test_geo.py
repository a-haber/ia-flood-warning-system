"""Test for geo module"""

from numpy import geomspace
from floodsystem.geo import rivers_by_station_number, rivers_with_station, stations_by_distance, stations_by_river, stations_within_radius
from floodsystem.station import MonitoringStation
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

def test_rivers_with_station():
    # Tests that the function has at least 900 rivers and Allison Dyke is in rivers
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    # Check if there are more stations than 900 (there should be 949 or 950, depending on the day)
    assert len(rivers) >= 900
    # Check if the Allison Dyke is in rivers
    assert "Allison Dyke" in rivers

#Task 1E
    def test_rivers_by_station_number(self):
        station1 = MonitoringStation(station_id="111",
                                     measure_id="111",
                                     label="Station 1",
                                     coord=(0, 1),
                                     typical_range=(0.1, 0.4),
                                     river="River 1",
                                     town="Town 1")
        station2 = MonitoringStation(station_id="222",
                                     measure_id="222",
                                     label="Station 2",
                                     coord=(1, 1),
                                     typical_range=(0.3, 0.8),
                                     river="River 2",
                                     town="Town 2")
        station3 = MonitoringStation(station_id="333",
                                     measure_id="333",
                                     label="Station 3",
                                     coord=(0, 3),
                                     typical_range=(0.43, 0.88),
                                     river="River 2",
                                     town="Town 3")
        station4 = MonitoringStation(station_id="444",
                                     measure_id="444",
                                     label="Station 4",
                                     coord=(8, 3),
                                     typical_range=(0.1, 0.9),
                                     river="River 3",
                                     town="Town 4")
                                     
    # Milestone 1 finished – ready for marking
