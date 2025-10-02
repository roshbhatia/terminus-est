# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "numpy-stl",
# ]
# ///

from stl import mesh
import numpy as np
import sys

# Load the STL file
stl_file = sys.argv[1] if len(sys.argv) > 1 else "plate.stl"

print(f"Loading {stl_file}...")
your_mesh = mesh.Mesh.from_file(stl_file)

# Get the bounding box
all_points = your_mesh.vectors.reshape(-1, 3)
min_vals = all_points.min(axis=0)
max_vals = all_points.max(axis=0)
center = (min_vals + max_vals) / 2

print("\n=== SEARCHING FOR USB CUTOUT ===")
# Look for points near the front edge (min Y)
front_edge_tolerance = 2.0  # mm from front edge
front_points = all_points[all_points[:, 1] < (min_vals[1] + front_edge_tolerance)]

if len(front_points) > 0:
    # Find the X range of front edge points
    front_x_min = front_points[:, 0].min()
    front_x_max = front_points[:, 0].max()
    front_z_min = front_points[:, 2].min()
    front_z_max = front_points[:, 2].max()

    print(f"Front edge spans:")
    print(f"  X: {front_x_min:.2f} to {front_x_max:.2f}")
    print(f"  Z: {front_z_min:.2f} to {front_z_max:.2f}")

    # After centering
    print(f"\nAfter centering at origin:")
    print(f"  X: {front_x_min - center[0]:.2f} to {front_x_max - center[0]:.2f}")
    print(f"  Z: {front_z_min - center[2]:.2f} to {front_z_max - center[2]:.2f}")

print("\n=== FOR OPENSCAD USB CUTOUT ===")
print(f"// USB cutout (adjust these if needed)")
print(f"usb_cutout_x = 0;  // X center position")
print(f"usb_cutout_width = 15;  // Width of cutout")
print(f"usb_cutout_z = {(front_z_min + front_z_max)/2 - center[2]:.2f};  // Z center")
print(f"usb_cutout_height = 8;  // Height of cutout")
print("====================================\n")
