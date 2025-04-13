# Dictionary to store Cricket World Cup winners
world_cup_winners = {
    1975: "West Indies",
    1979: "West Indies",
    1983: "India",
    1987: "Australia",
    1992: "Pakistan",
    1996: "Sri Lanka",
    1999: "Australia",
    2003: "Australia",
    2007: "Australia",
    2011: "India",
    2015: "Australia",
    2019: "England",
    2023: "Australia"
}

# Counting occurrences of each country
country_wins = {}
for country in world_cup_winners.values():
    country_wins[country] = country_wins.get(country, 0) + 1

# Finding the best-performing country
best_country = max(country_wins)

# Display the results
print("Cricket World Cup Winners by Year:", world_cup_winners)
print("\nThe best-performing country is:", best_country, "with", country_wins[best_country], "wins.")
print("\nUnique list of winning countries:", list(set(world_cup_winners.values())))
