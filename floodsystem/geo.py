# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

from haversine import haversine
from .station import MonitoringStation

def stations_by_distance(stations, p):
    """Return a list of (station, distance) tuples sorted by distance
    from p
    Where stations is a list of MonitoringStation objects, and p is a
    tuple of floats for a coordinate p"""
    stationList = []

    #build list of (station, distance) tuples
    for station in stations:
        coords = station.coord
        distance = haversine(coords, p) # use haversine library to calculate distance in km
        stationList.append((station.name, station.town, distance))
    
    #sort list by distance
    stationList = sorted_by_key(stationList, 2)

    return stationList

def stations_within_radius(stations, centre, r):
    """Return a list of all stations within radius r of a geographic
    coordinate centre"""
    qualifyingStations = []

    # build list of stations within required radius
    for station in stations:
        coords = station.coord
        distance = haversine(coords, centre) # use haversine to calculate distance in km
        if distance < abs(r):
            qualifyingStations.append(station.name)
    
    return qualifyingStations