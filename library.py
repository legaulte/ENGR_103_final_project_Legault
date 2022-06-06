# import packages
import numpy as np

# Function 1: Find yearly data
def find_yearly_data(yr_array, country_user, country_array, data_set, year_user_start, year_user_end):
    yearly_data_set1 = []
    for x in range(len(yr_array)):
        if int(year_user_start) <= int(yr_array[x]) and country_array[x] == country_user and int(year_user_end) >= int(
                        yr_array[x]):
            yearly_data_set1.append(data_set[x])
    return yearly_data_set1

# Function 2: Computing average installed capacity
def ave_installed_cap(yearly_data_set):
    ave_inst_cap = np.sum(yearly_data_set) / len(yearly_data_set)
    return ave_inst_cap

# Function 3: Computing rate of change
def rate_of_change(data_set):
    data_set_max = np.max(data_set)  # max is the first value
    data_set_min = np.min(data_set)
    roc_data_set = (data_set_max-data_set_min)/(len(data_set))
    return roc_data_set

# Function 4: Comparison of rate of change
def inst_cap_rate_analysis(roc_data_set):
    if rate_of_change < 0:
        print("The installed capacity is decreasing, indicating that...")
    elif rate_of_change > 0:
        print("The installed capacity is increasing, indicating that...")

# Function 5: Computing % of installed capacity
def percent_of_country(data_set1,data_set2):
    data_set1_sum = np.sum(data_set1)
    data_set2_sum = np.sum(data_set2)
    total_sum = data_set1_sum + data_set2_sum
    per_country1 = (data_set1_sum/total_sum) * 100
    return per_country1

# Function 6: Display console information
def display_console_info(country_user,ave_cntry,max_cntry,roc_country,per_inst_cap):
    print("  ")
    print("For the country,", country_user, "...")
    print("\tThe average installed capacity over your selected year range is",
          np.round(ave_cntry, decimals=4), "gW.")
    print("\tThe maximum installed capacity over your the selected year range is",
          np.round(max_cntry, decimals=4),"gW.")
    print("\tThe rate of change of installed capacity over the year range is:",
          np.round(roc_country, decimals=4), "gW/year.")
    print("\tThe percent of installed capacity that comes from this country compared to the total"
          " of the two countries is",np.round(per_inst_cap, decimals=4),"%.")