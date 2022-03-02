from floodsystem.stationdata import build_station_list, update_water_levels

def main():
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
            # >90% - low risk

            percentage = (station.latest_level - station.typical_range[0]) / (station.typical_range[1] - station.typical_range[0])

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

    severe.sort()
    high.sort()
    moderate.sort()
    low.sort()
    no_data.sort()
    print(f"Severe Risk:\n{severe}\n")
    print(f"High Risk:\n{high}\n")
    print(f"Moderate Risk:\n{moderate}\n")
    print(f"Low Risk:\n{low}\n")
    print(f"No Reliable Data:\n{no_data}\n")

if __name__ == "__main__":
    main()