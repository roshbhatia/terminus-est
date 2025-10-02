print("Starting Terminus Est...")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())

keyboard.col_pins = (
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    None,
    None,
    board.GP17,
    board.GP18,
    board.GP19,
    board.GP20,
    board.GP21,
    board.GP22,
    board.GP26,
    None,
    board.GP27,
    board.GP28,
)

keyboard.row_pins = (
    board.GP10,
    board.GP11,
    board.GP12,
    board.GP13,
    board.GP15,
    board.GP16,
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.NO,   KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC,
        KC.TAB,  KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.NO,   KC.NO,   KC.ESC,  KC.NO,   KC.NO,   KC.ESC,  KC.NO,   KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSPC,
        KC.LCTL, KC.LCTL, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.NO,   KC.NO,   KC.LALT, KC.NO,   KC.NO,   KC.LALT, KC.NO,   KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.BSLS, KC.NO,
        KC.NO,   KC.LSFT, KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.NO,   KC.LGUI, KC.NO,   KC.NO,   KC.LGUI, KC.NO,   KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.ENT,  KC.NO,
        KC.NO,   KC.LSFT, KC.LSFT, KC.NO,   KC.NO,   KC.SPC,  KC.SPC,  KC.SPC,  KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.SPC,  KC.SPC,  KC.SPC,  KC.NO,   KC.NO,   KC.ENT,  KC.ENT,  KC.NO,   KC.NO,
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.SPC,  KC.SPC,  KC.SPC,  KC.MO(1),KC.NO,   KC.NO,   KC.NO,   KC.SPC,  KC.SPC,  KC.SPC,  KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
    ],
    [
        KC.NO,   KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,   KC.NO,   KC.RESET,KC.NO,   KC.NO,   KC.RESET,KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.MPLY, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.MNXT, KC.TRNS, KC.NO,   KC.NO,   KC.TRNS, KC.NO,   KC.NO,   KC.TRNS, KC.NO,   KC.UP,   KC.LEFT, KC.DOWN, KC.RGHT, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,
        KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.MPRV, KC.NO,   KC.TRNS, KC.NO,   KC.NO,   KC.TRNS, KC.NO,   KC.MPRV, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,
        KC.NO,   KC.TRNS, KC.TRNS, KC.NO,   KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,   KC.NO,   KC.TRNS, KC.TRNS, KC.NO,   KC.NO,
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,   KC.NO,   KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
    ],
]

if __name__ == '__main__':
    keyboard.go()
