import board
import digitalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP26, board.GP27, board.GP28, board.GP29)
keyboard.row_pins = (board.GP6, board.GP7, board.GP0, board.GP1)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.N1, KC.N2, KC.N3, KC.N4,
        KC.W, KC.A, KC.S, KC.D,
        KC.Z, KC.X, KC.C, KC.V,
        KC.Q, KC.E, KC.R, KC.T
    ]
]

enc = EncoderHandler()
keyboard.modules.append(enc)

enc.pins = (
    (board.GP2, board.GP4, None),
)

enc.map = [
    ((KC.VOLU, KC.VOLD),),
]

btn = digitalio.DigitalInOut(board.GP3)
btn.switch_to_input(pull=digitalio.Pull.UP)

def scan():
    if not btn.value:
        keyboard.tap_key(KC.MUTE)

keyboard.before_matrix_scan = scan

if __name__ == "__main__":
    keyboard.go()
