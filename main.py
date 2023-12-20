import os

import bme280
import framebuf
import ssd1306
import utime
from machine import I2C, Pin

# タクトスイッチのためにGPIO 19、内蔵プルアップ抵抗を使います。
button = Pin(19, Pin.IN, Pin.PULL_UP)

# `/img` フォルダ内のテキストファイル名のリスト
image_files = os.listdir("/img")
image_files = [file for file in image_files if file.endswith(".txt")]
current_image_index = 0
print(image_files)

# 2つのLEDの設定。内蔵のLEDをPico Wで使う場合は "LED" とし、
# 無印Picoの場合は25とします
# 今回は内蔵LEDを画像切替の時のみ点灯、外部LEDを常時点灯とします
led = Pin("LED", Pin.OUT)
# 外部LEDの設定と常時点灯。適当な抵抗も忘れないように。
ext_led = Pin(10, Pin.OUT)
ext_led.value(1)

# SSD1306の初期化 (SCL: GP6, SDA: GP7)
i2c_ssd = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c_ssd)

# BME280センサーの初期化 (SCL: GP4, SDA: GP5)
i2c_bme = I2C(0, scl=Pin(5), sda=Pin(4))
bme = bme280.BME280(i2c=i2c_bme)

# 画像表示
def display_image(x, y, width, height, data):
    image = framebuf.FrameBuffer(data, width, height, framebuf.MONO_HLSB)
    oled.blit(image, x, y)

# 画像データをロード
def load_image_data(filename):
    with open(filename, 'r') as file:
        data = file.read()
        byte_values = [int(b.strip(), 16) for b in data.split(',')]
        return bytearray(byte_values)

# 次の画像をロード
def load_next_image():
    global current_image_index
    if image_files:
        # 次の画像にインデックスを更新
        current_image_index = (current_image_index + 1) % len(image_files)
        image_path = '/img/' + image_files[current_image_index]
        return load_image_data(image_path)
    return None

# 起動時の画像をロード
if image_files:
    image_data = load_image_data('/img/' + image_files[current_image_index])

# ここからメインのループ
while True:
    # タクトスイッチが押されたら外付けLEDを点灯し、
    # 次の画像を読み込む関数を実行
    # 1.5秒スリープして外付けLEDを消灯
    if not button.value():
        led.value(1)
        image_data = load_next_image()
        utime.sleep(1.5)
        led.value(0)

    # BME280からのデータ
    temperature, pressure, humidity = bme.read_compensated_data()

    # データをフォーマット
    temperature = int(temperature / 100)
    humidity = int(humidity / 1024)
    pressure = int(pressure / 256 / 100)

    # データ表示用のテキスト
    temp_text = "Temp :{}C".format(temperature)
    humidity_text = "Humid:{}%".format(humidity)
    pressure_text = "Press:{:,}hPa".format(pressure)

    # OLEDをリセット
    oled.fill(0)

    # 画像を表示
    display_image(0, 0, 128, 64, image_data)

    # テキスト部分
    oled.text(temp_text, 5, 5)
    oled.text(humidity_text, 5, 18)
    oled.text(pressure_text, 5, 30)
    oled.text("Merry Xmas", 3, 51)

    # テキストを囲む四角
    oled.hline(0, 1, 125, 1) #top
    oled.hline(0, 41, 125, 1) #bottom
    oled.vline(0, 1, 41, 1) #left
    oled.vline(125, 1, 41, 1) #right

    oled.show()
