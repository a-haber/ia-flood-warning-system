import matplotlib.pyplot as plt


def plot_water_levels(station, dates, levels):
    """Display a plot of water level data against time for a given station"""
    plt.plot(dates, levels)

    plt.xlabel("Date")
    plt.ylabel("Water Level (m)")
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()

    plt.show()