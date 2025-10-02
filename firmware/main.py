from kmk.kmk_keyboard import KMKKeyboard
from kmk.extensions.media_keys import MediaKeys

from hardware import COL_PINS, ROW_PINS, DIODE_ORIENTATION
from keymap import KEYMAP

print("Starting Terminus Est...")

keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())

keyboard.col_pins = COL_PINS
keyboard.row_pins = ROW_PINS
keyboard.diode_orientation = DIODE_ORIENTATION

keyboard.keymap = KEYMAP

if __name__ == "__main__":
    keyboard.go()
