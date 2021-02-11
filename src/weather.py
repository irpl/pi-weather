from gpiozero import MCP3008, Button
import time, concurrent.futures, requests, bme280, smbus2, os, sys

SERVER_URL = os.environ['SERVER_URL']
if SERVER_URL == "":
	print("SERVER_URL EVIRONMENT VAR NOT SET")
	sys.exit()

# ? Defines
# * wind direction
ADC = MCP3008(channel=0)
DIR_INTERVAL = 5
VOLTS_ANGLE = {
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

# * wind speed
WIND_SPEED = 2.4
WIND_INTERVAL = 5
WIND_SPEED_SENSOR = Button(5)
wind_count = 0

# * rainfall
BUCKET_SIZE = 0.2794
RAIN_INTERVAL = 5 
RAIN_FALL_SENSOR = Button(6)
tip_count = 0

# * bme280
I2C_PORT = 1
I2C_BME_ADDRESS = 0x77
I2C_BUS = smbus2.SMBus(I2C_PORT)
# ? /Defines

# ? Functions
# * wind direction
def getWindDir():
	time.sleep(DIR_INTERVAL)
	wind_dir = round(ADC.value * 3.3, 2)
	if not wind_dir in VOLTS_ANGLE:
		return { "winddir": -1 }
	else:
		return { "winddir": VOLTS_ANGLE[wind_dir] }

# * wind speed
def spin():
    global wind_count
    wind_count += 1
WIND_SPEED_SENSOR.when_pressed = spin

def getWindSpd():
	global wind_count
	wind_count = 0
	start_time = time.time()
	while (time.time() - start_time) <= WIND_INTERVAL:
		time.sleep(WIND_INTERVAL)
		# continue
	end_time = time.time()
	return { "windspd": round((wind_count/(end_time - start_time)) * WIND_SPEED,2) }

# * rain fall
def tip():
    global tip_count
    tip_count += 1
RAIN_FALL_SENSOR.when_pressed = tip

def getRainFall():
	global tip_count
	tip_count = 0
	start_time = time.time()

	while (time.time() - start_time) <= RAIN_INTERVAL:
		time.sleep(RAIN_INTERVAL)
		# continue
	# end_time = time.time()
	return { "rainfall": round(tip_count * BUCKET_SIZE, 4) }


bme280.load_calibration_params(I2C_BUS,I2C_BME_ADDRESS)
def getBME():
    bme280_data = bme280.sample(I2C_BUS,I2C_BME_ADDRESS)
    return {
    	"humidity": bme280_data.humidity,
    	"pressure": bme280_data.pressure,
    	"ambient_temperature": bme280_data.temperature
    }
# ? /Functions

# s = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
	while True:
		fns = [getWindDir, getRainFall, getWindSpd, getBME]
		results = [executor.submit(fn) for fn in fns]

		res_dict = {}
		# print(concurrent.futures.as_completed(results))
		for f in concurrent.futures.as_completed(results):
			# print(f.result())
			res_dict |= f.result()
			# k, v = f.result().split(": ")
			# res_dict[k] = v
			# print(f.result())
		# print (res_dict)
		try:
			res = requests.post(SERVER_URL, json=res_dict)
			print(res.text)
		except Exception as e:
			print(e)

		# f = time.perf_counter()
		# print(f"Finished in {round(f-s, 2)} second(s)")