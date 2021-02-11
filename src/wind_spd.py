from gpiozero import Button
import math, time, statistics

WIND_SPEED = 2.4
WIND_INTERVAL = 5

radius_cm = 8.67

wind_count = 0

def spin():
    global wind_count
    wind_count += 1
    # print("spin" + str(wind_count))

# def calculate_speed(time_sec):
# 	global wind_count
# 	circumference_cm = (2 * math.pi) * radius_cm
# 	rotations = wind_count / 2.0
# 	dist_cm = circumference_cm * rotations
# 	speed = dist_cm / time_sec
# 	return speed

# def reset_wind():
#     global wind_count
#     wind_count = 0

wind_speed_sensor = Button(5)
wind_speed_sensor.when_pressed = spin

while True:
	wind_count = 0
	start_time = time.time()
	while (time.time() - start_time) <= WIND_INTERVAL:
		# time.sleep(wind_interval)
		continue
	end_time = time.time()
	# print( calculate_speed(end_time - start_time), "cm/s" )
	print( (wind_count/(end_time - start_time)) * WIND_SPEED )