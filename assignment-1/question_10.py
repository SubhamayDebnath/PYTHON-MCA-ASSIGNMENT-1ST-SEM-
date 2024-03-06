# In a town, the percentage of men is 52. The percentage of total literacy is 48. If total
# percentage of literate men is 35 of the total population, write a program to find the total
# number of illiterate men and women if the population of the town is 80,000.

total_literacy_percentage = 48
total_men_percentage =52
total_literate_men_percentage=35
total_population = 80000
total_number_of_literate = (total_literacy_percentage * total_population) / 100
total_number_of_men=(total_men_percentage * total_population) / 100  
total_literate_men=(total_literate_men_percentage * total_population) / 100
total_illiterate_men=total_number_of_men - total_literate_men
total_illiterate_women=(total_number_of_literate - total_literate_men)
print(" the total number of illiterate men is ",total_illiterate_men," and women is",total_illiterate_women);