from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import numpy as np
import datetime
import matplotlib.dates

def run():
    severe = []
    high = []
    moderate = []
    low = []
    no_data = []
    stations = build_station_list()
    update_water_levels(stations)

    for station in stations:

        # Risk can only be calculated if there is typical range to compare to

        if station.typical_range_consistent() and station.latest_level is not None:

            # The function that calculates the risk of flooding is as follows: 
            # it takes the percentage difference between what the water level at the station is now 
            # and the averaged water level at the station over the last 24 hours

            # If the percentage of water level is compared to the previous day:
            # >150%  - severe risk
            # 120% - 150%  - high risk
            # 90% - 120% - moderate risk
            # <90% - low risk

            percentage = station.relative_water_level(station.latest_level)

            if percentage >= 1.5:
                severe.append(station.name)
            elif percentage >= 1.2:
                high.append(station.name)
            elif percentage >= 0.9:
                moderate.append(station.name)
            else:
                low.append(station.name)
        else:
            no_data.append(station.name)
        
        # For stations identified as high risk, estimate if water level
        # is rising or falling using the polyfit best fit function
        # Then, if water level rising, upgrade warning level to severe
        if station.name in high:
            try:
                # Create best-fit polynomial to approximate water level data over past 5 days
                measure_id = station.measure_id
                dates, levels = fetch_measure_levels(measure_id, datetime.timedelta(days=5))
                bestfit, offset = polyfit(dates, levels, p=4)
                derivative = np.polyder(bestfit) # Differentiate best-fit polynomial
                # Estimate if water level rising or falling at the most recent data point
                gradient = derivative(matplotlib.dates.date2num(dates[0]) - offset) # Evaluate gradient
                # Gradients which are positive but close to 0 are ignored here
                if gradient > 1:
                    high.remove(station.name)
                    severe.append(station.name)
            # Some stations have faulty data - no useful polynomial fit, so leave in current warning category
            except IndexError:
                pass
            except KeyError:
                pass
    
    severe.sort()
    high.sort()
    moderate.sort()
    low.sort()
    no_data.sort()
    print(f"Severe Risk:\n{severe}\n")
    print(f"High Risk:\n{high}\n")
    print(f"Moderate Risk:\n{moderate}\n")
    print(f"Low Risk:\n{len(low)} stations\n")
    print(f"No Reliable Data:\n{len(no_data)} stations\n")

if __name__ == "__main__":
    run()