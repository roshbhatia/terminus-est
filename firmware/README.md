# Terminus Est Firmware

This directory contains the KMK firmware configuration for the Terminus Est keyboard using a Raspberry Pi Pico.

## Prerequisites

- Raspberry Pi Pico
- CircuitPython 7.3 or higher
- KMK firmware

## Setup Instructions

### 1. Install CircuitPython

1. Download CircuitPython for the Raspberry Pi Pico from [circuitpython.org](https://circuitpython.org/board/raspberry_pi_pico/)
2. Hold the BOOTSEL button on the Pico while plugging it into your computer
3. The Pico will appear as a USB drive (RPI-RP2)
4. Copy the `.uf2` CircuitPython firmware file to the drive
5. The Pico will reboot and appear as `CIRCUITPY`

### 2. Install KMK

1. Download KMK from the [main branch](https://github.com/KMKfw/kmk_firmware/archive/refs/heads/master.zip)
2. Extract the archive
3. Copy the `kmk` folder to the root of the `CIRCUITPY` drive
4. The folder structure should be: `CIRCUITPY/kmk/`

### 3. Install Keyboard Configuration

Copy the following files from this `firmware/` directory to the root of your `CIRCUITPY` drive:

- `boot.py`
- `main.py`

Your `CIRCUITPY` drive should now contain:
```
CIRCUITPY/
├── kmk/
├── boot.py
├── main.py
└── lib/ (if you add any additional libraries)
```

### 4. Test Your Keyboard

1. Unplug and replug the Pico
2. The keyboard should be recognized by your computer
3. Press keys to test - they should output according to the keymap in `main.py`

## Customization

### Pin Configuration

The pin configuration is already set up based on the pinout documentation:

- **Columns (20 total):**
  - Left: GP0-GP9
  - Right: GP16-GP22, GP26-GP28

- **Rows (6 total):**
  - GP10-GP15

### Diode Orientation

The current configuration uses `COL2ROW`. If your keyboard doesn't respond correctly, try changing this to `ROW2COL` in `main.py`:

```python
keyboard.diode_orientation = DiodeOrientation.ROW2COL
```

### Keymap

The keymap in `main.py` is a starter configuration. Customize it based on your preferred layout.

- **Layer 0:** Base layer with standard QWERTY layout
- **Layer 1:** Function layer (access via the Fn key)

See the [KMK documentation](https://github.com/KMKfw/kmk_firmware/tree/master/docs/en) for:
- Available keycodes
- Creating macros
- Adding additional layers
- Enabling modules (RGB, rotary encoders, etc.)

## Troubleshooting

### Keyboard not detected
- Ensure CircuitPython is properly installed
- Check that `boot.py` is in the root directory
- Verify USB cable supports data transfer

### Keys not responding
- Check the diode orientation setting
- Verify pin assignments match your PCB
- Use the serial console to view debug output

### Matrix debugging
Connect to the serial console to see debug output:
```python
# Add this to main.py for debugging
keyboard.debug_enable = True
```

## Resources

- [KMK Documentation](https://github.com/KMKfw/kmk_firmware/tree/master/docs/en)
- [KMK Keycodes](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/keycodes.md)
- [CircuitPython Documentation](https://docs.circuitpython.org/)
- [Terminus Est Pinout](../docs/pinout.md)
