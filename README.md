# esp32_rmt_pwm
A 8-channel PWM library using RMT for MicroPytohn on ESP32.

On ESP32, the [PWM](http://docs.micropython.org/en/latest/esp32/quickref.html#pwm-pulse-width-modulation) in MicroPython lacks the feature for using different frequencies on different pins. All the PWM pins would be the same frequency after usnig PWM.freq() method. This prevents us doing some funny stuff like composing music using multiple notes.

Fortunately, there's a technique names [RMT](http://docs.micropython.org/en/latest/library/esp32.html#rmt) on ESP32 that provide 8 channels for sending pulse signals. We can use RMT to emulate PWM signals by sending pulse signal repeatly.

This library defines a PWM class with the same interface of the PWM class in the MicroPython library. You can port existed scripts without any trouble. 

### Usage

```python
>>> from machine import Pin
>>> from esp32_rmt_pwm import PWM
>>> p25 = PWM(Pin(25))
>>> p25.freq(261)
>>> p25.duty(768)
>>> p25.deinit()
```

Note that the frequency is limited to 16~5000000Hz due to the clock divider we choose for RMT is 80. The time click therefore is 1000000us / (80MHz / 80) = 1us. The longest pulse width is 1us × 32767 × 2 = 65534us. So the minimum frequency is 1000000us / 65534us ≒ 16Hz.