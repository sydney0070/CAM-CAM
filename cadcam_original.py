import math
from pprint import pprint

# Given dimensions
diameter = 530  # mm
radius = diameter / 2  # mm
height = 530  # mm (assuming height equals diameter)

# Material proportions
proportions = {
    "IN718": 0.6,   # Ni-based
    "Ti64": 0.25,   # Ti-based
    "SS316L_AlSi10Mg": 0.15  # Special Steel
}

# Material densities (kg/mm^3)
densities = {
    "IN718": 8.15e-6,  # kg/mm^3
    "Ti64": 4.41e-6,   # kg/mm^3
    "SS316L_AlSi10Mg": 7.9e-6  # kg/mm^3 (average of SS316L and AlSi10Mg)
}

# Powder costs ($/kg)
powder_costs = {
    "IN718": (120 + 180) / 2,  # Average cost
    "Ti64": (250 + 500) / 2,
    "SS316L_AlSi10Mg": (70 + 90) / 2
}

# Calculate volume of the cylinder (mm^3)
volume = math.pi * radius**2 * height

# Calculate material costs
material_costs = {}
total_material_cost = 0

for material, proportion in proportions.items():
    material_volume = volume * proportion  # Volume for the material
    material_mass = material_volume * densities[material]  # Mass in kg
    cost = material_mass * powder_costs[material]  # Cost in $
    material_costs[material] = cost
    total_material_cost += cost

# Output results
material_costs["Total"] = total_material_cost
pprint(material_costs)
