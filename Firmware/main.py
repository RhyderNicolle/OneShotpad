import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

keyboard = KMKKeyboard()

PINS = [
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [[
    KC.LCTL(KC.INS),
    KC.LSFT(KC.INS),
    KC.DEL,
    KC.LCTL(KC.Z),
    KC.LCTL(KC.S),
    KC.LCTL(KC.Y),
]]

if __name__ == '__main__':
    keyboard.go()