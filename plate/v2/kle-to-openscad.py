#!/usr/bin/env python3
"""
KLE JSON to OpenSCAD switch positions converter
Parses keyboard-layout.json and generates OpenSCAD array of switch positions
"""

import json
import sys

def parse_kle_json(layout_data):
    """
    Parse KLE JSON format and return list of switch positions.
    Returns: [(x, y, width), ...]
    """
    switches = []
    current_y = 0

    for row in layout_data:
        current_x = 0
        current_width = 1  # Default key width in units

        for item in row:
            if isinstance(item, dict):
                # This is a metadata object that modifies the next key
                if 'x' in item:
                    current_x += item['x']
                if 'y' in item:
                    current_y += item['y']
                if 'w' in item:
                    current_width = item['w']
                # Ignore other properties like 'a' (alignment), etc.

            elif isinstance(item, str):
                # This is an actual key
                switches.append((current_x, current_y, current_width))
                # Move to next position
                current_x += current_width
                # Reset width to default for next key
                current_width = 1

        # Move to next row
        current_y += 1

    return switches

def generate_openscad_array(switches):
    """
    Generate OpenSCAD array declaration from switch positions.
    """
    lines = ["switch_positions = ["]

    # Group by row for readability
    current_row = 0
    row_switches = []

    for x, y, w in switches:
        if y != current_row:
            # Output previous row
            if row_switches:
                lines.append(f"    // Row {current_row}")
                lines.append("    " + ", ".join(row_switches) + ",")
                lines.append("")
            row_switches = []
            current_row = y

        row_switches.append(f"[{x}, {y}, {w}]")

    # Output last row
    if row_switches:
        lines.append(f"    // Row {current_row}")
        lines.append("    " + ", ".join(row_switches))

    lines.append("];")
    return "\n".join(lines)

def main():
    # Load the KLE JSON
    json_file = sys.argv[1] if len(sys.argv) > 1 else "../../layout/keyboard-layout.json"

    print(f"Loading {json_file}...")
    with open(json_file, 'r') as f:
        layout = json.load(f)

    # Parse the layout
    switches = parse_kle_json(layout)

    print(f"Found {len(switches)} switches\n")

    # Generate OpenSCAD code
    openscad_code = generate_openscad_array(switches)

    print(openscad_code)
    print()

    # Print some stats
    print(f"\n// Statistics:")
    print(f"// Total switches: {len(switches)}")
    min_x = min(s[0] for s in switches)
    max_x = max(s[0] for s in switches)
    min_y = min(s[1] for s in switches)
    max_y = max(s[1] for s in switches)
    print(f"// X range: {min_x} to {max_x}")
    print(f"// Y range: {min_y} to {max_y}")
    print(f"// Dimensions: {max_x - min_x + 1}U x {max_y - min_y + 1}U")

if __name__ == "__main__":
    main()
