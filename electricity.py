def calculate_emissions(usage):
    emissions_factor = 0.233  # kg CO2 per kWh
    return usage * emissions_factor
