from machine import Pin
from esp32 import RMT

class PWM():
    # free RMT channel table
    RMT_channels = [False, False, False, False, False, False, False, False]
    
    def __init__(self, pwm_pin, freq=5000, duty=512):
        for idx in range(len(PWM.RMT_channels)):
            if not PWM.RMT_channels[idx]:                      # find free channel
                PWM.RMT_channels[idx] = True;                  # mark used cnannel
                self.RMT_channel = idx                         # keep the channel number
                self.RMT_obj = RMT(idx, pin=pwm_pin, clock_div=80)
                self.init(freq, duty)
                break
        else:
            raise RuntimeError('No RMT channel available.')
        
    def run(self):
        period = 1000000 / (self.pwm_freq)
        up_time = int(period * (self.pwm_duty / 1023))
        down_time = int(period) - up_time
        self.RMT_obj.loop(False)
        self.RMT_obj.write_pulses((up_time, down_time), start=1)
        self.RMT_obj.loop(True)
        # MicroPython 1.13 requires loop() running before write_pulses()
        # MicroPython 1.12 would report error if loop() runs before any write_pulses()
        self.RMT_obj.write_pulses((up_time, down_time), start=1)
        
    def freq(self, new_freq):
        self.pwm_freq = new_freq if new_freq > 15 else 16
        self.run()
        
    def duty(self, new_duty):
        self.pwm_duty = new_duty if new_duty < 1023 else 1023
        self.run()
        
    def deinit(self):
        self.RMT_obj.deinit()
        PWM.RMT_channels[self.RMT_channel] = False
    
    def init(self, freq=5000, duty=512):
        self.freq(freq)
        self.duty(duty)


