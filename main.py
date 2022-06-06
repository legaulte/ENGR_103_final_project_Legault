########################################################################################################################
# Program Filename: final project ENGR 103 Emma Legault
# Author: Emma Legault
# Date: 5/28/22
# Description: The purpose of the program is to compare the installed capacity of two, user-selected countries through
# using various computations and to identify anomalies within the data set that can be then analyzed.
# Input: Installed capacity of two countries, years, country name
# Output: Installed capacity, rate of installed capacity over a range of years, percentage of installed capacity
# in relation to the other country
########################################################################################################################

# Import packages and data sets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import library as lb
file_path = "C:/Users/emmal/Downloads/emberChartData (2).csv"
installed_cap_data = pd.read_csv(file_path)

# PART 1: Doing the groundwork
# Part 1A: Isolate columns in data set
country_name1 = installed_cap_data.loc[:,"country_or_region"]
year1 = installed_cap_data.loc[:,"year"]
e_source1 = installed_cap_data.loc[:,"variable"]
capacity_gw1 = installed_cap_data.loc[:,"capacity_gw"]

# Part 1B: Calling user inputs
year_user_start = input("What is the start year of your range that you'd like to assess (between 2000 and 2021): ")
year_user_end = input("What is the end year of your range that you'd like to assess (between 2000 and 2021): ")
print("Here is the list of countries you may choose from:"
      "https://docs.google.com/document/d/1Et1IuHgn3S49seIzsmiGHWg-DaimsBSCyW9EP5PLrrI/edit?usp=sharing")
country_user1 = input("What is the country you'd like to analyze: ")

# Part 1C: Saving the specific user selected years to an empty array to be used when plotting
year_user_list = []
for x in range(len(year1)):
    if int(year_user_start) <= int(year1[x]) and int(year_user_end) >= int(year1[x]):
        year_user_list.append(year1[x])
    else:
        break

# PART 2: Calling functions that find the data (store data)
yr_data_country1 = lb.find_yearly_data(year1, country_user1, country_name1, capacity_gw1, year_user_start, year_user_end)

# PART 3: Data manipulation and computations

# PART 3A: Store values for the second country
user_decision_2nd_cntry = input("Would you like to analyze another country with your first one (HINT: This isn't a question...)? ")
country_user2 = input("What is that country you'd like to analyze: ")
while True:
    if user_decision_2nd_cntry == "yes" or "YES" or "Yes" or "YEs" or "YeS":
        yr_data_country2 = lb.find_yearly_data(year1,country_user2,country_name1,capacity_gw1,year_user_start,year_user_end)
        yr_data_country2_max = np.max(yr_data_country2)
        roc_installed_cap_cntry2 = lb.rate_of_change(yr_data_country2)
        ave_inst_cap_cntry2 = lb.ave_installed_cap(yr_data_country2)
        percent_inst_country2 = lb.percent_of_country(yr_data_country2,yr_data_country1)
        break
    elif user_decision_2nd_cntry == "no":
        break

# Part 3B: Store values for the first country
yr_data_country1_sort = np.sort(yr_data_country1)
yr_data_country1_max = (np.max(yr_data_country1_sort))
roc_installed_cap_cntry1 = lb.rate_of_change(yr_data_country1)
ave_inst_cap_cntry1 = lb.ave_installed_cap(yr_data_country1)
percent_inst_country1 = lb.percent_of_country(yr_data_country1,yr_data_country2)
percent_array = percent_inst_country1 + percent_inst_country2

# PART 4: Display values

# Part 4A: Display calculated values in console
show_country1_info = lb.display_console_info(country_user1,ave_inst_cap_cntry1,yr_data_country1_max,
                                             roc_installed_cap_cntry1,percent_inst_country1)
show_country2_info = lb.display_console_info(country_user2,ave_inst_cap_cntry2,yr_data_country2_max,
                                             roc_installed_cap_cntry2,percent_inst_country2)

# Part 4B: Display values in console for comparison of the two selected countries
print("  ")
if percent_inst_country1 > percent_inst_country2:
    print("The country,",country_user1,", has a greater energy generation capacity in it's fossil fuel"
                                       " factories than",country_user2,".")
elif percent_inst_country1 < percent_inst_country2:
    print("The country,",country_user1,", has a smaller energy generation capacity in it's fossil fuel "
                                       "factories than",country_user2,".")
print("  ")
print("This concludes the program. Thank you Professor Wengrove, Jesus, Ian, Loc, Isabelle, and Ibraheim for all of "
      "your help and guidance during this term.")
print("I really wouldn't have been able to learn as much as I have these past 11 weeks"
      " if I hadn't been taught by you all. Thank you again.")

# Part 4C: Display values in matplotlib by plotting
# normal installed capacity
fig = plt.subplots()
plt.subplot(221)
plt.title("Installed capacity for fossil fuel factories of 2 countries")
plt.plot(year_user_list, yr_data_country1, linestyle="solid", marker="s", color='orange', label=country_user1)
plt.ylabel("Installed capacity (gW)")
plt.subplot(221)
plt.plot(year_user_list, yr_data_country2, linestyle="solid", marker="s", color='black', label=country_user2)
plt.ylabel("Installed capacity (gW)")
plt.legend()
plt.grid()

# average installed capacity
plt.subplot(222)
plt.title("Average installed capacity")
plt.plot(country_user1, ave_inst_cap_cntry1, linestyle="solid", marker="s", color='orange', label=country_user1)
plt.subplot(222)
plt.plot(country_user2, ave_inst_cap_cntry2, linestyle="solid", marker="s", color='black', label=country_user2)
plt.xlabel("Country")
plt.ylabel("Average installed capacity (gW/year)")
plt.legend()
plt.grid()

# rate of change
plt.subplot(223)
plt.title("Rate of change for installed capacity")
plt.plot(country_user1, roc_installed_cap_cntry1, linestyle="solid", color='orange', marker="s",)
plt.subplot(223)
plt.plot(country_user2, roc_installed_cap_cntry2, linestyle="solid", color='black', marker="s",)
plt.xlabel("Country")
plt.ylabel("Rate of change (gW/year)")
plt.grid()
plt.show()

# # percentage of installed capacity comparison
# countries = (country_user1, country_user2)
# plt.subplot(212)
# fig = plt.figure(figsize = (10,7))
# countries = [country_user1 + country_user2]
# data = [percent_inst_country1, percent_inst_country2]
# fig = plt.figure(figsize=(10, 7))
# plt.pie(data, labels=countries)
# plt.show()


