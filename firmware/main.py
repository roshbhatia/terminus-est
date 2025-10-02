"""
Terminus Est Keyboard - KMK Configuration
Raspberry Pi Pico

Ported from ZMK configuration at:
https://github.com/roshbhatia/zmk-config-terminus-est
"""

print("Starting Terminus Est...")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

# Enable media keys extension for play/pause, next/prev track, etc.
keyboard.extensions.append(MediaKeys())

# Pin Configuration
# Matrix: 22 columns x 6 rows (some columns not populated)
# Columns mapping from ZMK dtsi file:
keyboard.col_pins = (
    board.GP0,  # COL0
    board.GP1,  # COL1
    board.GP2,  # COL2
    board.GP3,  # COL3
    board.GP4,  # COL4
    board.GP5,  # COL5
    board.GP6,  # COL6
    board.GP7,  # COL7
    board.GP8,  # COL8
    board.GP9,  # COL9
    None,       # COL10 - not connected
    None,       # COL11 - not connected
    board.GP17, # COL12
    board.GP18, # COL13
    board.GP19, # COL14
    board.GP20, # COL15
    board.GP21, # COL16
    board.GP22, # COL17
    board.GP26, # COL18
    None,       # COL19 - not connected
    board.GP27, # COL20
    board.GP28, # COL21
)

# Rows mapping from ZMK dtsi file:
keyboard.row_pins = (
    board.GP10, # ROW0
    board.GP11, # ROW1
    board.GP12, # ROW2
    board.GP13, # ROW3
    board.GP15, # ROW4 (note: GP14 is skipped)
    board.GP16, # ROW5
)

# Diode orientation from ZMK: col2row
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Keymap
# Ported from ZMK configuration
# Matrix layout: 22 columns x 6 rows
# COL: 0     1     2     3     4     5     6     7     8     9     10    11    12    13    14    15    16    17    18    19    20    21
keyboard.keymap = [
    # Layer 0: Base (QWERTY)
    [
        # ROW0
        KC.NO,   KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC,
        # ROW1
        KC.TAB,  KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.NO,   KC.NO,   KC.ESC,  KC.NO,   KC.NO,   KC.ESC,  KC.NO,   KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSPC,
        # ROW2
        KC.LCTL, KC.LCTL, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.NO,   KC.NO,   KC.LALT, KC.NO,   KC.NO,   KC.LALT, KC.NO,   KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.BSLS, KC.NO,
        # ROW3
        KC.NO,   KC.LSFT, KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.NO,   KC.LGUI, KC.NO,   KC.NO,   KC.LGUI, KC.NO,   KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.ENT,  KC.NO,
        # ROW4
        KC.NO,   KC.LSFT, KC.LSFT, KC.NO,   KC.NO,   KC.SPC,  KC.SPC,  KC.SPC,  KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.SPC,  KC.SPC,  KC.SPC,  KC.NO,   KC.NO,   KC.ENT,  KC.ENT,  KC.NO,   KC.NO,
        # ROW5
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.SPC,  KC.SPC,  KC.SPC,  KC.MO(1),KC.NO,   KC.NO,   KC.NO,   KC.SPC,  KC.SPC,  KC.SPC,  KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
    ],
    # Layer 1: Function
    [
        # ROW0
        KC.NO,   KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        # ROW1
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,   KC.NO,   KC.RESET,KC.NO,   KC.NO,   KC.RESET,KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.MPLY, KC.TRNS, KC.TRNS, KC.TRNS,
        # ROW2
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.MNXT, KC.TRNS, KC.NO,   KC.NO,   KC.TRNS, KC.NO,   KC.NO,   KC.TRNS, KC.NO,   KC.UP,   KC.LEFT, KC.DOWN, KC.RGHT, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,
        # ROW3
        KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.MPRV, KC.NO,   KC.TRNS, KC.NO,   KC.NO,   KC.TRNS, KC.NO,   KC.MPRV, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,
        # ROW4
        KC.NO,   KC.TRNS, KC.TRNS, KC.NO,   KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,   KC.NO,   KC.TRNS, KC.TRNS, KC.NO,   KC.NO,
        # ROW5
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,   KC.NO,   KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
    ],
]

if __name__ == '__main__':
    keyboard.go()
