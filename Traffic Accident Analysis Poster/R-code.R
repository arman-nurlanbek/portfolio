# PART 1
# Number of accidents happened in total 2020.
library(tidyverse)
accidents = read_csv('accidents.csv')
number_of_accidents = nrow(accidents)
print(number_of_accidents)
# Number of accidents classified 'slight'
library(dplyr)
slight_severity = filter(accidents, severity == 'slight')
number_of_slight_accidents  = nrow(slight_severity)
print(number_of_slight_accidents)
# Number of accidents classified 'serious'
serious_severity = filter(accidents, severity == 'serious')
number_of_serious_accidents  = nrow(serious_severity)
print(number_of_serious_accidents)
# Number of accidents classified 'fatal'
fatal_severity = filter(accidents, severity == 'fatal')
number_of_fatal_accidents  = nrow(fatal_severity)
print(number_of_fatal_accidents)


# Sum of total vehicles involved in all accidents
vehicles = accidents %>%
  summarize(number_of_vehicles = sum(number_of_vehicles))
# Sum of total number of casualties
casualties = accidents %>%
  summarize(number_of_casualties = sum(number_of_casualties))


# Percentage of casualties incurred in urban areas
urban_accidents = filter(accidents, area == 'urban')
number_of_urban_casualties = sum(urban_accidents$number_of_casualties)
print(number_of_urban_casualties/casualties*100)

# 5
library(readr)
# Largest number of vehicles include in a single accident
max_vehicles = max(accidents$number_of_vehicles)
max_vehicles_index = which.max(accidents$number_of_vehicles)
accidents[max_vehicles_index, ]
# Largest number of casualties include in a signle accident
max_casualties = max(accidents$number_of_casualties)
max_casualties_index = which.max(accidents$number_of_casualties)
accidents[max_casualties_index, ]

# Part 2
# Plot of locations of accidents with fatal and serious severities
library(ggplot2)
coast = read_csv('coast.csv')
accidents_subset <- accidents[accidents$severity %in% c('serious', 'fatal'),]
ggplot(accidents_subset, aes(x = longitude, y = latitude, color = severity)) +
  geom_point() +
  geom_point(size = 0.5, alpha = 0.1) +
  scale_x_discrete(expand=c(0.01, 0.01))+
  # Adding country outlines to the plot
  geom_polygon(data = coast, aes(x = long, y = lat, group = group),
               fill = NA, color = "red") +
  labs(title = "Locations of Accidents", x = "Longitude", y = "Latitude")

# Part 3
# Plot of total nubmer of accidents per month
ggplot(accidents, aes(x = month, y = frequency(month), color = month)) +
  geom_bar(stat = "identity")+
  scale_x_discrete(expand=c(0.1, 0.01))+
  scale_y_continuous(name="Number of Accidents", labels = scales::comma)+
  labs(title = 'Total number of accidents per month', x = 'Month', y = 'Number of Accidents')+
  geom_hline(yintercept = c(8000, 10000), color = "red")

# Plot of total number of fatal accidents per month
ggplot(fatal_severity, aes(x = month, y = frequency(month), color = month)) +
  geom_bar(stat = "identity")+
  scale_x_discrete(expand=c(0.1, 0.01))+
  scale_y_continuous(name="Number of Accidents", labels = scales::comma)+
  labs(title = 'Total number of fatal accidents per month', x = 'Month', y = 'Number of Accidents')




