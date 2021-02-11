import bme280
import smbus2
from time import sleep

I2C_PORT = 1
I2C_BME_ADDRESS = 0x77
I2C_BUS = smbus2.SMBus(I2C_PORT)

bme280.load_calibration_params(I2C_BUS,I2C_BME_ADDRESS)

def getBME():
    bme280_data = bme280.sample(I2C_BUS,I2C_BME_ADDRESS)
    return {
    	"humidity": bme280_data.humidity,
    	"pressure": bme280_data.pressure,
    	"ambient_temperature": bme280_data.temperature
    }
print(getBME())