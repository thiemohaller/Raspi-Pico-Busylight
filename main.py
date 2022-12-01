from machine import Pin,Timer
from random import randint
import time

# fancy way: state machine
# not fancy way: bool

# define PINS
rgb_red = Pin(11, Pin.OUT)
rgb_blue = Pin(12, Pin.OUT)
rgb_green = Pin(13, Pin.OUT)
button_change_state = Pin(17, Pin.IN, Pin.PULL_UP)

# define values
isBusyState = False

red_value = 0
green_value = 255
blue_value = 100

def button_was_pressed():
    # detect if button was pressed
    first = button_change_state.value()
    time.sleep(0.01)
    second = button_change_state.value()
    # * return true once the button is released
    return not first and second

while True:
    if button_was_pressed():
        print('Button was pressed!')
        isBusyState = not isBusyState
        print('currently in busy state: ', isBusyState)

    if isBusyState: 
        rgb_red.value(255)
        rgb_green.value(0)
        rgb_blue.value(0)
    else: 
        rgb_red.value(0)
        rgb_green.value(255)
        rgb_blue.value(0)
