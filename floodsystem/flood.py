from floodsystem import stationdata
from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):

    """Returns a list of the tuples, each containing the name of a station at which the relative
        water level is above tol and the relative water level at that station"""

    flooded_stations = []

    stationdata.update_water_levels(stations)

    for station in stations:
        if station.relative_water_level(station.latest_level) is not None:
            if station.relative_water_level(station.latest_level) > tol:
                station_name_water_level = station.name, station.relative_water_level(station.latest_level)
                flooded_stations.append(station_name_water_level)

    sorted_flooded_stations = sorted_by_key(flooded_stations, 1, reverse=True)

    return sorted_flooded_stations

def stations_highest_rel_level(stations, N):

    """Returns a list of the N stations at which the water level,
    relative to the typical range, is highest"""

    stations_relative_level = []

    stationdata.update_water_levels(stations)

    for station in stations:
        if station.relative_water_level(station.latest_level) is not None:
            station_name_water_level = station.name, station.relative_water_level(station.latest_level)
            stations_relative_level.append(station_name_water_level)

    sorted_stations_relative_level = sorted_by_key(stations_relative_level, 1, reverse=True)

    return sorted_stations_relative_level[:N]