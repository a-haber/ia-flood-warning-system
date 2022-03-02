"""Test for analysis module"""

import datetime
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import numpy
import matplotlib

def test_polyfit():
    # Build list of dates and levels
    stationlist = build_station_list()
    for station in stationlist[:5]:
        measure_id = station.measure_id
        dates, levels = fetch_measure_levels(measure_id, datetime.timedelta(days=5))

        # Check that the function outputs the correct type of data
        output = polyfit(dates, levels, 4)
        assert isinstance(output, tuple)
        assert isinstance(output[0], numpy.poly1d)
        assert isinstance(output[1], float)
        assert len(output) == 2