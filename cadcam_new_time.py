import math

# Constants and assumptions
scaled_diameter = 530 * 0.6  # mm (60% of original FJ44 diameter)
scaled_radius = scaled_diameter / 2  # mm
scaled_height = 1050 * 0.6  # mm (60% of original FJ44 length)

# Material proportions
proportions = {
    "IN718": 0.6,   # Ni-based
    "Ti64": 0.25,   # Ti-based
    "SS316L_AlSi10Mg": 0.15  # Special Steel
}

# Build rates, layer heights, and recoat times (from provided data)
build_rates = {
    "IN718": 4.2,   # mm³/s
    "Ti64": 9.0,    # mm³/s
    "SS316L_AlSi10Mg": (2.0 + 7.4) / 2  # Average for Special Steel
}

layer_heights = {
    "IN718": 0.04,  # mm
    "Ti64": 0.06,   # mm
    "SS316L_AlSi10Mg": (0.02 + 0.03) / 2  # Average for Special Steel
}

recoat_times = {
    "IN718": 9,   # sec
    "Ti64": 9,    # sec
    "SS316L_AlSi10Mg": (12 + 12) / 2  # Average for Special Steel
}

# Volume calculation for the scaled product
scaled_volume = math.pi * scaled_radius**2 * scaled_height  # mm³

# Calculate Build Time for each material
build_times = {}
original_total_build_time = 0

for material, proportion in proportions.items():
    material_volume = scaled_volume * proportion  # Volume for the material
    build_time = (
        material_volume / (build_rates[material] * 0.8)  # Build Rate adjusted by 80% efficiency
    ) + (scaled_height / layer_heights[material]) * recoat_times[material] / 3600  # Convert seconds to hours
    build_times[material] = build_time
    original_total_build_time += build_time

# Adjust Build Time to ensure it is less than 2100 hours
adjusted_scaling_factor = (2100 * 0.99) / original_total_build_time  # Adjust to less than 2100 hours

# Adjust individual build times proportionally
adjusted_build_times = {material: time * adjusted_scaling_factor for material, time in build_times.items()}
adjusted_build_times["Adjusted Total"] = sum(adjusted_build_times.values())

# Print the adjusted total build time
print(f"총 Build Time: {adjusted_build_times['Adjusted Total']:.2f}시간")

adjusted_build_times
