"""
Terminus Est Keyboard - KMK Configuration
Raspberry Pi Pico
"""

print("Starting Terminus Est...")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

# Pin Configuration
# Columns: Left side (GP0-GP9) + Right side (GP16-GP22, GP26-GP28)
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
    board.GP16, # COL10
    board.GP17, # COL11
    board.GP18, # COL12
    board.GP19, # COL13
    board.GP20, # COL14
    board.GP21, # COL15
    board.GP22, # COL16
    board.GP26, # COL17
    board.GP27, # COL18
    board.GP28, # COL19
)

# Rows: GP10-GP15
keyboard.row_pins = (
    board.GP10, # ROW0
    board.GP11, # ROW1
    board.GP12, # ROW2
    board.GP13, # ROW3
    board.GP14, # ROW4
    board.GP15, # ROW5
)

# Diode orientation - adjust based on your actual wiring
# Common options: COL2ROW or ROW2COL
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Keymap
# This is a basic starter keymap - customize based on your layout
# Each row in the matrix corresponds to the physical layout
keyboard.keymap = [
    [
        # Row 0 (20 keys across all columns)
        KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.NO,   KC.NO,   KC.NO,
        KC.NO,   KC.NO,   KC.NO,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC,

        # Row 1
        KC.TAB,  KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.NO,   KC.ESC,  KC.NO,
        KC.NO,   KC.ESC,  KC.NO,   KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC,

        # Row 2
        KC.LCTL, KC.LCTL, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.NO,   KC.LALT, KC.NO,
        KC.NO,   KC.RALT, KC.NO,   KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.BSLS,

        # Row 3
        KC.LSFT, KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.NO,   KC.LGUI, KC.NO,
        KC.NO,   KC.RGUI, KC.NO,   KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.ENT,  KC.NO,

        # Row 4
        KC.NO,   KC.LSFT, KC.LSFT, KC.NO,   KC.NO,   KC.SPC,  KC.SPC,  KC.SPC,  KC.NO,   KC.NO,
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.SPC,  KC.SPC,  KC.SPC,  KC.NO,   KC.ENT,  KC.ENT,

        # Row 5
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.SPC,  KC.SPC,  KC.SPC,  KC.NO,   KC.MO(1),
        KC.NO,   KC.NO,   KC.SPC,  KC.SPC,  KC.SPC,  KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
    ],
    # Layer 1 - Function layer (activated by MO(1) key)
    [
        # Row 0
        KC.TRNS, KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.NO,   KC.NO,   KC.NO,
        KC.NO,   KC.NO,   KC.NO,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.DEL,

        # Row 1
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,   KC.TRNS, KC.NO,
        KC.NO,   KC.TRNS, KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,

        # Row 2
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,   KC.TRNS, KC.NO,
        KC.NO,   KC.TRNS, KC.NO,   KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT, KC.TRNS, KC.TRNS, KC.TRNS,

        # Row 3
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,   KC.TRNS, KC.NO,
        KC.NO,   KC.TRNS, KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,

        # Row 4
        KC.NO,   KC.TRNS, KC.TRNS, KC.NO,   KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,   KC.NO,
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,   KC.TRNS, KC.TRNS,

        # Row 5
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,   KC.TRNS,
        KC.NO,   KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
    ],
]

if __name__ == '__main__':
    keyboard.go()
