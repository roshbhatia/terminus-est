"""
Minimal test firmware for Terminus Est keyboard
Tests just ONE key at position ROW0 x COL1 (GP10 x GP1)
Should output 'Z' when pressed
"""
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

# Test only ONE key: ROW0 x COL1
keyboard.row_pins = (board.GP10,)  # ROW0 only
keyboard.col_pins = (board.GP1,)   # COL1 only
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Output 'Z' when this key is pressed
keyboard.keymap = [[KC.Z]]

if __name__ == "__main__":
    keyboard.go()
