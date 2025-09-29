#!/usr/bin/env python3
"""
Basic validation script for ZMK configuration files.
This checks for common issues in device tree files and keymap.
"""

import os
import sys
import json
import re
from pathlib import Path

def check_file_exists(filepath):
    """Check if a file exists and is readable."""
    if not Path(filepath).exists():
        print(f"❌ Missing file: {filepath}")
        return False
    print(f"✅ Found: {filepath}")
    return True

def validate_device_tree(filepath):
    """Basic validation of device tree syntax."""
    try:
        with open(filepath, 'r') as f:
            content = f.read()

        # Check for basic DT syntax
        if 'compatible =' not in content:
            print(f"⚠️  {filepath}: Missing 'compatible' property")

        # Check for balanced braces
        open_braces = content.count('{')
        close_braces = content.count('}')
        if open_braces != close_braces:
            print(f"❌ {filepath}: Unbalanced braces ({open_braces} open, {close_braces} close)")
            return False

        # Check for GPIO pin references
        gpio_pins = re.findall(r'pro_micro (\d+)', content)
        if gpio_pins:
            print(f"✅ {filepath}: Found GPIO pins: {', '.join(set(gpio_pins))}")

        return True
    except Exception as e:
        print(f"❌ Error reading {filepath}: {e}")
        return False

def validate_keymap(filepath):
    """Basic validation of keymap file."""
    try:
        with open(filepath, 'r') as f:
            content = f.read()

        # Check for required includes
        required_includes = ['behaviors.dtsi', 'dt-bindings/zmk/keys.h']
        for include in required_includes:
            if include not in content:
                print(f"⚠️  {filepath}: Missing include: {include}")

        # Check for keymap structure
        if 'keymap {' not in content:
            print(f"❌ {filepath}: Missing keymap definition")
            return False

        # Check for layers
        layers = re.findall(r'(\w+_layer)\s*{', content)
        if layers:
            print(f"✅ {filepath}: Found layers: {', '.join(layers)}")

        return True
    except Exception as e:
        print(f"❌ Error reading {filepath}: {e}")
        return False

def main():
    """Main validation function."""
    print("🔍 Validating ZMK Configuration for Terminus Est")
    print("=" * 50)

    # Check required files
    required_files = [
        'config/west.yml',
        'config/boards/shields/terminus_est/Kconfig.shield',
        'config/boards/shields/terminus_est/Kconfig.defconfig',
        'config/boards/shields/terminus_est/terminus_est.dtsi',
        'config/boards/shields/terminus_est/terminus_est_left.overlay',
        'config/boards/shields/terminus_est/terminus_est_right.overlay',
        'config/terminus_est.keymap',
        'build.yaml'
    ]

    all_files_exist = True
    for file in required_files:
        if not check_file_exists(file):
            all_files_exist = False

    if not all_files_exist:
        print("\n❌ Some required files are missing!")
        return False

    print("\n🔍 Validating Device Tree Files")
    print("-" * 30)

    # Validate device tree files
    dt_files = [
        'config/boards/shields/terminus_est/terminus_est.dtsi',
        'config/boards/shields/terminus_est/terminus_est_left.overlay',
        'config/boards/shields/terminus_est/terminus_est_right.overlay'
    ]

    dt_valid = True
    for dt_file in dt_files:
        if not validate_device_tree(dt_file):
            dt_valid = False

    print("\n🔍 Validating Keymap")
    print("-" * 20)

    # Validate keymap
    keymap_valid = validate_keymap('config/terminus_est.keymap')

    print("\n📊 Validation Summary")
    print("=" * 20)

    if all_files_exist and dt_valid and keymap_valid:
        print("✅ All validations passed!")
        print("🚀 Ready to build ZMK firmware!")
        return True
    else:
        print("❌ Some validations failed!")
        print("🔧 Please fix the issues above before building.")
        return False

if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    success = main()
    sys.exit(0 if success else 1)