from kmk.keys import KC

BASE_R0 = [
    KC.NO,  # C0
    KC.GRV,  # C1
    KC.N1,  # C2
    KC.N2,  # C3
    KC.N3,  # C4
    KC.N4,  # C5
    KC.N5,  # C6
    KC.N6,  # C7
    KC.NO,  # C8
    KC.NO,  # C9
    KC.NO,  # C10
    KC.NO,  # C11
    KC.NO,  # C12
    KC.NO,  # C13
    KC.NO,  # C14
    KC.N7,  # C15
    KC.N8,  # C16
    KC.N9,  # C17
    KC.N0,  # C18
    KC.MINS,  # C19
    KC.EQL,  # C20
    KC.BSPC,  # C21
]

BASE_R1 = [
    KC.TAB,  # C0
    KC.TAB,  # C1
    KC.Q,  # C2
    KC.W,  # C3
    KC.E,  # C4
    KC.R,  # C5
    KC.T,  # C6
    KC.NO,  # C7
    KC.NO,  # C8
    KC.ESC,  # C9
    KC.NO,  # C10
    KC.NO,  # C11
    KC.ESC,  # C12
    KC.NO,  # C13
    KC.Y,  # C14
    KC.U,  # C15
    KC.I,  # C16
    KC.O,  # C17
    KC.P,  # C18
    KC.LBRC,  # C19
    KC.RBRC,  # C20
    KC.BSPC,  # C21
]

BASE_R2 = [
    KC.LCTL,  # C0
    KC.LCTL,  # C1
    KC.A,  # C2
    KC.S,  # C3
    KC.D,  # C4
    KC.F,  # C5
    KC.G,  # C6
    KC.NO,  # C7
    KC.NO,  # C8
    KC.LALT,  # C9
    KC.NO,  # C10
    KC.NO,  # C11
    KC.LALT,  # C12
    KC.NO,  # C13
    KC.H,  # C14
    KC.J,  # C15
    KC.K,  # C16
    KC.L,  # C17
    KC.SCLN,  # C18
    KC.QUOT,  # C19
    KC.BSLS,  # C20
    KC.NO,  # C21
]

BASE_R3 = [
    KC.NO,  # C0
    KC.LSFT,  # C1
    KC.LSFT,  # C2
    KC.Z,  # C3
    KC.X,  # C4
    KC.C,  # C5
    KC.V,  # C6
    KC.B,  # C7
    KC.NO,  # C8
    KC.LGUI,  # C9
    KC.NO,  # C10
    KC.NO,  # C11
    KC.LGUI,  # C12
    KC.NO,  # C13
    KC.B,  # C14
    KC.N,  # C15
    KC.M,  # C16
    KC.COMM,  # C17
    KC.DOT,  # C18
    KC.SLSH,  # C19
    KC.ENT,  # C20
    KC.NO,  # C21
]

BASE_R4 = [
    KC.NO,  # C0
    KC.LSFT,  # C1
    KC.LSFT,  # C2
    KC.NO,  # C3
    KC.NO,  # C4
    KC.SPC,  # C5
    KC.SPC,  # C6
    KC.SPC,  # C7
    KC.NO,  # C8
    KC.NO,  # C9
    KC.NO,  # C10
    KC.NO,  # C11
    KC.NO,  # C12
    KC.SPC,  # C13
    KC.SPC,  # C14
    KC.SPC,  # C15
    KC.NO,  # C16
    KC.NO,  # C17
    KC.ENT,  # C18
    KC.ENT,  # C19
    KC.NO,  # C20
    KC.NO,  # C21
]

BASE_R5 = [
    KC.NO,  # C0
    KC.NO,  # C1
    KC.NO,  # C2
    KC.NO,  # C3
    KC.NO,  # C4
    KC.NO,  # C5
    KC.SPC,  # C6
    KC.SPC,  # C7
    KC.SPC,  # C8
    KC.MO(1),  # C9
    KC.NO,  # C10
    KC.NO,  # C11
    KC.NO,  # C12
    KC.SPC,  # C13
    KC.SPC,  # C14
    KC.SPC,  # C15
    KC.NO,  # C16
    KC.NO,  # C17
    KC.NO,  # C18
    KC.NO,  # C19
    KC.NO,  # C20
    KC.NO,  # C21
]

BASE_LAYER = BASE_R0 + BASE_R1 + BASE_R2 + BASE_R3 + BASE_R4 + BASE_R5

FN_R0 = [
    KC.TRNS,  # C0
    KC.TRNS,  # C1
    KC.TRNS,  # C2
    KC.TRNS,  # C3
    KC.TRNS,  # C4
    KC.TRNS,  # C5
    KC.TRNS,  # C6
    KC.TRNS,  # C7
    KC.TRNS,  # C8
    KC.TRNS,  # C9
    KC.TRNS,  # C10
    KC.TRNS,  # C11
    KC.TRNS,  # C12
    KC.TRNS,  # C13
    KC.TRNS,  # C14
    KC.TRNS,  # C15
    KC.TRNS,  # C16
    KC.TRNS,  # C17
    KC.TRNS,  # C18
    KC.TRNS,  # C19
    KC.TRNS,  # C20
    KC.TRNS,  # C21
]

FN_R1 = [
    KC.TRNS,  # C0
    KC.TRNS,  # C1
    KC.TRNS,  # C2
    KC.TRNS,  # C3
    KC.TRNS,  # C4
    KC.TRNS,  # C5
    KC.TRNS,  # C6
    KC.TRNS,  # C7
    KC.TRNS,  # C8
    KC.RESET,  # C9
    KC.TRNS,  # C10
    KC.TRNS,  # C11
    KC.RESET,  # C12
    KC.TRNS,  # C13
    KC.TRNS,  # C14
    KC.TRNS,  # C15
    KC.TRNS,  # C16
    KC.TRNS,  # C17
    KC.MPLY,  # C18
    KC.TRNS,  # C19
    KC.TRNS,  # C20
    KC.TRNS,  # C21
]

FN_R2 = [
    KC.TRNS,  # C0
    KC.TRNS,  # C1
    KC.TRNS,  # C2
    KC.TRNS,  # C3
    KC.TRNS,  # C4
    KC.MNXT,  # C5
    KC.TRNS,  # C6
    KC.TRNS,  # C7
    KC.TRNS,  # C8
    KC.TRNS,  # C9
    KC.TRNS,  # C10
    KC.TRNS,  # C11
    KC.TRNS,  # C12
    KC.TRNS,  # C13
    KC.UP,  # C14
    KC.LEFT,  # C15
    KC.DOWN,  # C16
    KC.RGHT,  # C17
    KC.TRNS,  # C18
    KC.TRNS,  # C19
    KC.TRNS,  # C20
    KC.TRNS,  # C21
]

FN_R3 = [
    KC.TRNS,  # C0
    KC.TRNS,  # C1
    KC.TRNS,  # C2
    KC.TRNS,  # C3
    KC.TRNS,  # C4
    KC.TRNS,  # C5
    KC.TRNS,  # C6
    KC.MPRV,  # C7
    KC.TRNS,  # C8
    KC.TRNS,  # C9
    KC.TRNS,  # C10
    KC.TRNS,  # C11
    KC.TRNS,  # C12
    KC.TRNS,  # C13
    KC.MPRV,  # C14
    KC.TRNS,  # C15
    KC.TRNS,  # C16
    KC.TRNS,  # C17
    KC.TRNS,  # C18
    KC.TRNS,  # C19
    KC.TRNS,  # C20
    KC.TRNS,  # C21
]

FN_R4 = [
    KC.TRNS,  # C0
    KC.TRNS,  # C1
    KC.TRNS,  # C2
    KC.TRNS,  # C3
    KC.TRNS,  # C4
    KC.TRNS,  # C5
    KC.TRNS,  # C6
    KC.TRNS,  # C7
    KC.TRNS,  # C8
    KC.TRNS,  # C9
    KC.TRNS,  # C10
    KC.TRNS,  # C11
    KC.TRNS,  # C12
    KC.TRNS,  # C13
    KC.TRNS,  # C14
    KC.TRNS,  # C15
    KC.TRNS,  # C16
    KC.TRNS,  # C17
    KC.TRNS,  # C18
    KC.TRNS,  # C19
    KC.TRNS,  # C20
    KC.TRNS,  # C21
]

FN_R5 = [
    KC.TRNS,  # C0
    KC.TRNS,  # C1
    KC.TRNS,  # C2
    KC.TRNS,  # C3
    KC.TRNS,  # C4
    KC.TRNS,  # C5
    KC.TRNS,  # C6
    KC.TRNS,  # C7
    KC.TRNS,  # C8
    KC.TRNS,  # C9
    KC.TRNS,  # C10
    KC.TRNS,  # C11
    KC.TRNS,  # C12
    KC.TRNS,  # C13
    KC.TRNS,  # C14
    KC.TRNS,  # C15
    KC.TRNS,  # C16
    KC.TRNS,  # C17
    KC.TRNS,  # C18
    KC.TRNS,  # C19
    KC.TRNS,  # C20
    KC.TRNS,  # C21
]

FUNCTION_LAYER = FN_R0 + FN_R1 + FN_R2 + FN_R3 + FN_R4 + FN_R5

KEYMAP = [BASE_LAYER, FUNCTION_LAYER]
