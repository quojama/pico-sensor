Tempurture, humidity, and pressure sensor by MicroPython Rapsberry Pi Pico W (or Pico).

![image](https://github.com/quojama/pico-sensor/assets/4445606/f22d2cfd-139e-4baa-9424-44ad3c23e016)

## Components

- [Raspberry Pi Pico W](https://akizukidenshi.com/catalog/g/gM-17947/) (or [Pico](https://akizukidenshi.com/catalog/g/gM-16132/))
- [BME280 sensor module](https://akizukidenshi.com/catalog/g/gK-09421/)
- [0.96" SSD1306 OLED display](https://akizukidenshi.com/catalog/g/gP-12031/)


## Wiring

| BME280 | Raspberry Pi Pico (W) | SSD1306 |
| --- | --- | --- |
| VCC | 3V3 (36pin) | VCC |
| GND | GND | GND |
| - | GP7 (10pin) | SCL |
| - | GP6 (9pin) | SDA |
| CSB | - | - |
| SDI | GP4 (6pin) | - |
| SDO | GND | - |
| SCK | GP5 (7pin) | - |
