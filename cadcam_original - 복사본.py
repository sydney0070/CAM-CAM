import math

# Assumptions and constants
build_time_percentage = 0.7  # Build Time is 70% of the total production time
total_production_time = 3500  # Total production time in hours (hidden in logic)

# Adjusted total build time
adjusted_total_build_time = total_production_time * build_time_percentage  # Adjusted build time in hours

# Material proportions
proportions = {
    "IN718": 0.6,   # Ni-based
    "Ti64": 0.25,   # Ti-based
    "SS316L_AlSi10Mg": 0.15  # Special Steel
}

# Build rates, layer heights, and recoat times
layer_heights = {
    "IN718": 0.04,  # mm
    "Ti64": 0.06,   # mm
    "SS316L_AlSi10Mg": (0.02 + 0.03) / 2  # Average for Special Steel
}

build_rates = {
    "IN718": 4.2,   # mm³/s
    "Ti64": 9.0,    # mm³/s
    "SS316L_AlSi10Mg": (2.0 + 7.4) / 2  # Average for Special Steel
}

recoat_times = {
    "IN718": 9,   # sec
    "Ti64": 9,    # sec
    "SS316L_AlSi10Mg": (12 + 12) / 2  # Average for Special Steel
}

# Cylinder dimensions
diameter = 530  # mm
radius = diameter / 2  # mm
height = 530  # mm (assuming height equals diameter)

# Volume calculation
volume = math.pi * radius**2 * height  # mm³

# Calculate original Build Time for each material
build_times = {}
original_total_build_time = 0

for material, proportion in proportions.items():
    material_volume = volume * proportion  # Volume for the material
    build_time = (
        material_volume / (build_rates[material] * 0.8)  # Build Rate adjusted by 80% efficiency
    ) + (height / layer_heights[material]) * recoat_times[material] / 3600  # Hours
    build_times[material] = build_time
    original_total_build_time += build_time

# Scaling factor to match the adjusted total build time
scaling_factor = adjusted_total_build_time / original_total_build_time

# Adjusting individual build times
adjusted_build_times = {material: time * scaling_factor for material, time in build_times.items()}
adjusted_build_times["Adjusted Total"] = sum(adjusted_build_times.values())  # Adjusted total build time

print(f"총 Adjusted Build Time: {adjusted_build_times['Adjusted Total']:.0f}시간")

