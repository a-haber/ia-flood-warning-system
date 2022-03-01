# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations   
from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.flood as flood


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_inconsistent_typical_range_stations():

    # Create three test stations
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange_A = (-2.3, 3.4445)
    trange_B = None
    trange_C = (3.4445, -2.3)
    river = "River X"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange_A, river, town)
    s2 = MonitoringStation(s_id, m_id, label, coord, trange_B, river, town)
    s3 = MonitoringStation(s_id, m_id, label, coord, trange_C, river, town)

    stations = [s1, s2, s3]
    data = inconsistent_typical_range_stations(stations)
    assert s1 not in data
    assert s2 in data
    assert s3 in data

def test_stations_level_over_threshold():

    # Build list of stations

    stations = build_station_list()
    update_water_levels(stations)

    present = flood.stations_level_over_threshold(stations, 0.8)
    assert present[0][1] > 0.8
    if len(present) > 1:

        # The returned list should be in descending order

        assert present[0][1] >= present[1][1]


def test_stations_highest_rel_level():

    # Build list of stations

    stations = build_station_list()
    update_water_levels(stations)

    shortlist = flood.stations_highest_rel_level(stations, 10)
    assert len(shortlist) == 10
    assert shortlist[0][1] >= shortlist[1][1]