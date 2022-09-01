def calculate_emissions(diet):
    emissions_factors = {
        "vegetarian": 3,
        "vegan": 2,
        "omnivore": 5
    }
    return emissions_factors.get(diet, 0) * 30  # Assuming monthly impact
