import matplotlib.pyplot as plt

from floodsystem.analysis import polyfit
from .station import MonitoringStation
from .analysis import polyfit
import matplotlib

def plot_water_levels(stations, dates, levels):
    """Display a plot of water level data against time for a list
    of up to 6 given stations - either in a 2x3 grid or as one single plot"""

    # If input is a list of multiple stations:
    # Plot data for each station as a subplot in a 2x3 grid
    if type(stations) == list:

        length = len(stations)
        # Ensure maximum of 6 stations being plotted at once
        if length > 6:
            print("Error: Too many stations to plot at once")
            return None

        for i in range(length):
            plt.subplot(2, 3, i+1)
            plt.plot(dates[i], levels[i])
            plt.xlabel("Date")
            plt.ylabel("Water Level (m)")
            plt.title(stations[i].name)
            plt.xticks(rotation=45)

            # Plot typical high/low levels
            high = [stations[i].typical_range[1]] * len(levels[i])
            low = [stations[i].typical_range[0]] * len(levels[i])
            plt.plot(dates[i], high, '--')
            plt.plot(dates[i], low, 'g--')
    
    # If input is only one station:
    # Plot that station on its own
    elif isinstance(stations, MonitoringStation):
        plt.plot(dates, levels, label = "water level data")
        plt.xlabel("Date")
        plt.ylabel("Water Level (m)")
        plt.title(stations.name)
        plt.xticks(rotation=45)
        
        # Plot typical high/low levels
        high = [stations.typical_range[1]] * len(levels)
        low = [stations.typical_range[0]] * len(levels)
        plt.plot(dates, high, '--', label = "typical high level")
        plt.plot(dates, low, 'g--', label='typical low level')
        plt.legend()
    
    plt.tight_layout()

    plt.show()
    return

def plot_water_level_with_fit(station, dates, levels, p):
    """Display water level data alongside best-fit polynomial"""
    poly, offset = polyfit(dates, levels, p)
    x = matplotlib.dates.date2num(dates)

    # Plot water level data and best fit polynomial
    plt.plot(dates, poly(x - offset), label = "best fit polynomial")
    plot_water_levels(station, dates, levels)
    
    return