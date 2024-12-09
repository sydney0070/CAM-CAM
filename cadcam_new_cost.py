import math

# Original dimensions of FJ44
original_length = 1050  # mm (converted from cm)
original_diameter = 530  # mm
original_radius = original_diameter / 2  # mm

# Scaled dimensions (60% scale)
scale = 0.6
scaled_length = original_length * scale  # mm
scaled_radius = original_radius * scale  # mm

# Calculate scaled volume (assuming a cylinder)
scaled_volume = math.pi * scaled_radius**2 * scaled_length  # mm³

# Material proportions
proportions = {
    "IN718": 0.6,   # Ni-based
    "Ti64": 0.25,   # Ti-based
    "SS316L_AlSi10Mg": 0.15  # Special Steel
}

# Material densities (kg/mm³) and powder costs ($/kg)
densities = {
    "IN718": 8.15e-6,  # kg/mm³
    "Ti64": 4.41e-6,   # kg/mm³
    "SS316L_AlSi10Mg": 7.9e-6  # kg/mm³ (average of SS316L and AlSi10Mg)
}

powder_costs = {
    "IN718": 150,   # $/kg
    "Ti64": 375,    # $/kg
    "SS316L_AlSi10Mg": 79  # $/kg
}

# Calculate material costs
material_costs = {}
total_material_cost = 0

for material, proportion in proportions.items():
    material_volume = scaled_volume * proportion  # Volume for the material
    material_mass = material_volume * densities[material]  # Mass in kg
    cost = material_mass * powder_costs[material]  # Cost in $
    material_costs[material] = cost
    total_material_cost += cost

# Add total cost
material_costs["Total"] = total_material_cost

material_costs

# Print the total material cost
print(f"총 재료비: ${material_costs['Total']:.2f}")

