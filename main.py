import bme280
import ssd1306
import utime
from machine import I2C, Pin

# pico w on board LED init
led = Pin("LED", Pin.OUT)

# SSD1306 init (SCL: GP6, SDA: GP7)
i2c_ssd = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c_ssd)

# BME280 init (SCL: GP4, SDA: GP5)
i2c_bme = I2C(0, scl=Pin(5), sda=Pin(4))
bme = bme280.BME280(i2c=i2c_bme)

while True:
    # get data from BME280
    temperature, pressure, humidity = bme.read_compensated_data()

    # format data
    temperature = int(temperature / 100)
    humidity = int(humidity / 1024)
    pressure = int(pressure / 256 / 100)

    temp_text = "Temp:{}C".format(temperature)
    humidity_text = "Humid:{}%".format(humidity)
    pressure_text = "Pres:{:,}hPa".format(pressure)

    # bink built in LED
    led.value(1)
    utime.sleep(0.2)
    led.value(0)

    # OLED display

    oled.fill(0)

    # text
    oled.text(temp_text, 5, 22)
    oled.text(humidity_text, 5, 35)
    oled.text(pressure_text, 5, 47)

    #b
    oled.hline(0, 18, 120, 1) #top
    oled.hline(0, 58, 120, 1) #bottom
    oled.vline(0, 18, 40, 1) #left
    oled.vline(120, 18, 40, 1) #right

    oled.show()

    utime.sleep(10)
