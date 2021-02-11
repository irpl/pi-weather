from gpiozero import Button
import math, time, statistics

BUCKET_SIZE = 0.2794
RAIN_INTERVAL = 5 
rain_fall_sensor = Button(6)
tip_count = 0

def tip():
    global tip_count
    tip_count += 1
    # print("tip" + str(tip_count))

# def calculate_speed(time_sec):
# 	global wind_count
# 	circumference_cm = (2 * math.pi) * radius_cm
# 	rotations = wind_count / 2.0
# 	dist_cm = circumference_cm * rotations
# 	speed = dist_cm / time_sec
# 	return speed


def reset_rain():
    global tip_count
    tip_count = 0


rain_fall_sensor.when_pressed = tip

while True:
	# continue
	# global tip_count
	tip_count = 0
	start_time = time.time()

	while (time.time() - start_time) <= RAIN_INTERVAL:
		# time.sleep(wind_interval)
		continue
	end_time = time.time()
	print( round(tip_count * BUCKET_SIZE, 4), "mm" )
