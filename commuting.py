def calculate_emissions(distance, mode):
    emissions_factors = {
        "car": 0.21,
        "bus": 0.10,
        "train": 0.05,
        "bicycle": 0,
        "walking": 0
    }
    return distance * emissions_factors.get(mode, 0)
