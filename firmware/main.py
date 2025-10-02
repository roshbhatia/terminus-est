print("Starting Terminus Est...")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys

XXXXXXX = KC.NO
_______ = KC.TRNS

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())

# ┌─────────────────────────────────────────────────────────────────────────────┐
# │ Matrix Configuration: 6 rows × 22 columns (COL2ROW)                          │
# └─────────────────────────────────────────────────────────────────────────────┘

keyboard.col_pins = (
    board.GP0,   # C0
    board.GP1,   # C1
    board.GP2,   # C2
    board.GP3,   # C3
    board.GP4,   # C4
    board.GP5,   # C5
    board.GP6,   # C6
    board.GP7,   # C7
    board.GP8,   # C8
    board.GP9,   # C9
    None,        # C10 (not connected)
    None,        # C11 (not connected)
    board.GP17,  # C12
    board.GP18,  # C13
    board.GP19,  # C14
    board.GP20,  # C15
    board.GP21,  # C16
    board.GP22,  # C17
    board.GP26,  # C18
    None,        # C19 (not connected)
    board.GP27,  # C20
    board.GP28,  # C21
)

keyboard.row_pins = (
    board.GP10,  # R0
    board.GP11,  # R1
    board.GP12,  # R2
    board.GP13,  # R3
    board.GP15,  # R4
    board.GP16,  # R5
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ┌─────────────────────────────────────────────────────────────────────────────┐
# │ Physical Layout                                                               │
# ├─────────────────────────────────────────────────────────────────────────────┤
# │  Left Half                                    Right Half                      │
# │                                                                               │
# │      `    1    2    3    4    5    6              7    8    9    0    -   +  │
# │  Tab Tab  Q    W    E    R    T   Esc           Esc  Y    U    I    O    P   │
# │ Ctrl Ctrl A    S    D    F    G   Alt           Alt  H    J    K    L    ;   │
# │      Sft Sft   Z    X    C    V    B   Cmd     Cmd   B    N    M    ,    .   │
# │          Sft Sft               Spc Spc Spc     Spc Spc Spc               Ent │
# │                                Spc Spc Spc Fn       Spc Spc Spc              │
# └─────────────────────────────────────────────────────────────────────────────┘

# fmt: off
keyboard.keymap = [
    # ┌───────────────────────────────────────────────────────────────────────┐
    # │ Layer 0: Base (QWERTY)                                                 │
    # └───────────────────────────────────────────────────────────────────────┘
    [
        # Row 0
        XXXXXXX, KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC,
        # Row 1
        KC.TAB,  KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    XXXXXXX, XXXXXXX, KC.ESC,  XXXXXXX, XXXXXXX, KC.ESC,  XXXXXXX, KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSPC,
        # Row 2
        KC.LCTL, KC.LCTL, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    XXXXXXX, XXXXXXX, KC.LALT, XXXXXXX, XXXXXXX, KC.LALT, XXXXXXX, KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.BSLS, XXXXXXX,
        # Row 3
        XXXXXXX, KC.LSFT, KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    XXXXXXX, KC.LGUI, XXXXXXX, XXXXXXX, KC.LGUI, XXXXXXX, KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.ENT,  XXXXXXX,
        # Row 4
        XXXXXXX, KC.LSFT, KC.LSFT, XXXXXXX, XXXXXXX, KC.SPC,  KC.SPC,  KC.SPC,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.SPC,  KC.SPC,  KC.SPC,  XXXXXXX, XXXXXXX, KC.ENT,  KC.ENT,  XXXXXXX, XXXXXXX,
        # Row 5
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.SPC,  KC.SPC,  KC.SPC,  KC.MO(1),XXXXXXX, XXXXXXX, XXXXXXX, KC.SPC,  KC.SPC,  KC.SPC,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
    ],
    # ┌───────────────────────────────────────────────────────────────────────┐
    # │ Layer 1: Function (Media, Arrows, Reset)                              │
    # └───────────────────────────────────────────────────────────────────────┘
    [
        # Row 0
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        # Row 1
        _______, _______, _______, _______, _______, _______, _______, _______, _______, KC.RESET,_______, _______, KC.RESET,_______, _______, _______, _______, _______, KC.MPLY, _______, _______, _______,
        # Row 2
        _______, _______, _______, _______, _______, KC.MNXT, _______, _______, _______, _______, _______, _______, _______, _______, KC.UP,   KC.LEFT, KC.DOWN, KC.RGHT, _______, _______, _______, _______,
        # Row 3
        _______, _______, _______, _______, _______, _______, _______, KC.MPRV, _______, _______, _______, _______, _______, _______, KC.MPRV, _______, _______, _______, _______, _______, _______, _______,
        # Row 4
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        # Row 5
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
    ],
]
# fmt: on

if __name__ == "__main__":
    keyboard.go()
