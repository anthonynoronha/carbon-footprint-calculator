import commuting
import electricity
import water
import food

def main():
    print("Welcome to the Carbon Footprint Calculator")
    total_emissions = 0

    # Commuting
    distance = float(input("Enter your daily commuting distance (km): "))
    mode = input("Enter your mode of transport (car, bus, train, bicycle, walking): ")
    commuting_emissions = commuting.calculate_emissions(distance, mode)
    total_emissions += commuting_emissions
    print(f"Commuting emissions: {commuting_emissions} kg CO2")

    # Electricity
    electricity_usage = float(input("Enter your monthly electricity usage (kWh): "))
    electricity_emissions = electricity.calculate_emissions(electricity_usage)
    total_emissions += electricity_emissions
    print(f"Electricity emissions: {electricity_emissions} kg CO2")

    # Water
    water_usage = float(input("Enter your average daily water consumption (liters): "))
    water_emissions = water.calculate_emissions(water_usage)
    total_emissions += water_emissions
    print(f"Water emissions: {water_emissions} kg CO2")

    # Food
    diet = input("Enter your dietary preference (vegetarian, vegan, omnivore): ")
    food_emissions = food.calculate_emissions(diet)
    total_emissions += food_emissions
    print(f"Food emissions: {food_emissions} kg CO2")

    print(f"Total carbon footprint: {total_emissions} kg CO2")

if __name__ == "__main__":
    main()
