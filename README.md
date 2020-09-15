# esp32_rmt_pwm
A 8-channel PWM library using RMT for MicroPytohn on ESP32.

On ESP32, the [PWM](http://docs.micropython.org/en/latest/esp32/quickref.html#pwm-pulse-width-modulation) in MicroPython lacks the feature for using different frequencies on different pins. All the PWM pins would be the same frequency after usnig PWM.freq() method. This prevents us doing some funny stuff like composing music using multiple notes.

Fortunately, there's a technique names [RMT](http://docs.micropython.org/en/latest/library/esp32.html#rmt) on ESP32 that provide 8 channels for sending pulse signals. We can use RMT to emulate PWM signals by sending pulse signal repeatly.

This library defines a PWM class with the same interface of the PWM class in the MicroPython library. You can port existed scripts without any trouble. 


