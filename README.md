Tempurture, humidity, and pressure sensor by MicroPython Rapsberry Pi Pico W (or Pico).

![PXL_20231210_173749873](https://github.com/quojama/pico-sensor/assets/4445606/94351a25-70b7-4e99-bd5c-5e21986fb28d)

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
| SDO | - | - |
| SCK | GP5 (7pin) | - |
