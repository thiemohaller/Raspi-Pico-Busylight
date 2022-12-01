from machine import Pin,Timer

led = Pin(25, Pin.OUT)
LED_state = True
timer = Timer()

def tick(timer):
    global led, LED_state
    LED_state = not LED_state
    led.value(LED_state)

timer.init(freq=1, mode=timer.PERIODIC, callback=tick)
