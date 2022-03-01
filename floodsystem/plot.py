import matplotlib.pyplot as plt
from .station import MonitoringStation

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
    
    # If input is only one station:
    # Plot that station on its own
    elif isinstance(stations, MonitoringStation):
        plt.plot(dates, levels)
        plt.xlabel("Date")
        plt.ylabel("Water Level (m)")
        plt.title(stations.name)
        plt.xticks(rotation=45)
    
    plt.tight_layout()

    plt.show()