from letmecreate.core.common import MIKROBUS_1
from letmecreate.core import pwm
from time import sleep

# inits

pwm.init(MIKROBUS_1)

pwm.set_duty_cycle(MIKROBUS_1, 50)


# Notes

def set_f7():
	pwm.set_frequency(MIKROBUS_1, 2794)

def set_g7():
	pwm.set_frequency(MIKROBUS_1, 3136)

def set_a7():
	pwm.set_frequency(MIKROBUS_1, 3520)

def set_b7():
	pwm.set_frequency(MIKROBUS_1, 3951)

def set_c8():
	pwm.set_frequency(MIKROBUS_1, 4186)

def set_d8():
	pwm.set_frequency(MIKROBUS_1, 4699)

def set_e8():
	pwm.set_frequency(MIKROBUS_1, 5274)

def set_f8():
	pwm.set_frequency(MIKROBUS_1, 5588)

def set_g8():
	pwm.set_frequency(MIKROBUS_1, 6271)

def set_a8():
	pwm.set_frequency(MIKROBUS_1, 7040)

# Play durations

def whole_play():
	pwm.enable(MIKROBUS_1)
	sleep(0.4)
	pwm.disable(MIKROBUS_1)

def half_play():
	pwm.enable(MIKROBUS_1)
	sleep(0.2)
	pwm.disable(MIKROBUS_1)

def quarter_play():
	pwm.enable(MIKROBUS_1)
	sleep(0.1)
	pwm.disable(MIKROBUS_1)

# Rest durations

def whole_rest():
	sleep(0.4)

def half_rest():
	sleep(0.2)

def quarter_rest():
	sleep(0.1)

