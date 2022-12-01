from machine import Pin,Timer

led_red = Pin(14, Pin.OUT)
led_blue = Pin(17, Pin.OUT)

LED_state_red = True
LED_state_blue = False

timer = Timer()

def tick(timer):
    global led_red, led_blue, LED_state_red, LED_state_blue
    LED_state_red = not LED_state_red
    LED_state_blue = not LED_state_blue
    led_red.value(LED_state_red)
    led_blue.value(LED_state_blue)

timer.init(freq=1, mode=timer.PERIODIC, callback=tick)
