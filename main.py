from machine import Pin,Timer
from random import randint
import time

# define PINS
rgb_red = Pin(11, Pin.OUT)
rgb_blue = Pin(12, Pin.OUT)
rgb_green = Pin(13, Pin.OUT)
button_change_state = Pin(17, Pin.IN, Pin.PULL_UP)

# define values
red_value = 0
green_value = 255
blue_value = 100

def change_LED_color():
    global red_value, green_value, blue_value
    print('changing values')
    red_value = randint(0,255)
    green_value = 0
    blue_value = randint(0,255)

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
        change_LED_color()

    rgb_red.value(red_value)
    rgb_green.value(green_value)
    rgb_blue.value(blue_value)
    
