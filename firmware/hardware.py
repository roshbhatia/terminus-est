import board
from kmk.scanners import DiodeOrientation

COL_PINS = (
    board.GP0,  # C0
    board.GP1,  # C1
    board.GP2,  # C2
    board.GP3,  # C3
    board.GP4,  # C4
    board.GP5,  # C5
    board.GP6,  # C6
    board.GP7,  # C7
    board.GP8,  # C8
    board.GP9,  # C9
    None,  # C10 (not connected)
    None,  # C11 (not connected)
    board.GP16,  # C12
    board.GP17,  # C13
    board.GP18,  # C14
    board.GP19,  # C15
    board.GP20,  # C16
    board.GP21,  # C17
    board.GP22,  # C18
    board.GP26,  # C19
    board.GP27,  # C20
    board.GP28,  # C21
)

ROW_PINS = (
    board.GP10,  # R0
    board.GP11,  # R1
    board.GP12,  # R2
    board.GP13,  # R3
    board.GP14,  # R4
    board.GP15,  # R5
)

DIODE_ORIENTATION = DiodeOrientation.COL2ROW
