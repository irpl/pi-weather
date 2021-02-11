from gpiozero import MCP3008
import time, math

ADC = MCP3008(channel=0)
DIR_INTERVAL = 5

volts_angle = {
	0.44: 0.0, 0.43: 0.0,
	1.43: 22.5,
	1.25: 45.0, 1.26: 45.0,
	2.8: 67.5,
	2.75: 90.0,
	2.9: 112.5,
	2.29:135.0, 2.3: 135.0,
	2.58: 157.5,
	1.86: 180.0,
	2.03: 202.5,
	0.79: 225.0,
	0.87: 247.5, 0.86: 247.5,
	0.13: 270.0, 0.14: 270.0,
	0.35: 292.5, 0.36: 292.5,
	0.24: 315.0,
	0.62: 337.5, 0.61: 337.5
}

def get_average_dirs(angles):
	sin_sum = 0.0
	cos_sum = 0.0

	for angle in angles:
		r = math.radians(angle)
		sin_sum += math.sin(r)
		cos_sum += math.cos(r)

	flen = float(len(angles))
	s = sin_sum / flen
	c = cos_sum / flen
	arc = math.degrees(math.atan(s / c))
	average = 0.0

	if s > 0 and c > 0:
		average = arc
	elif c < 0:
		average = arc + 180
	elif s < 0 and c > 0:
		average = arc + 360

	return 0.0 if average == 360 else average

def get_dir():
	dirs = []
	start_time = time.time()
	time.sleep(1)
	# while (time.time() - start_time <= DIR_INTERVAL):
	wind_dir = round(ADC.value * 3.3, 2)
	if not wind_dir in volts_angle:
		# print(f"not found: {str(wind_dir)}")
		return -1
	else:
		return volts_angle[wind_dir]
	
	# return get_average_dirs(dirs)

while True:
	# time.sleep(1)
	# print(round(ADC.value * 3.3, 2))
	print(get_dir())



