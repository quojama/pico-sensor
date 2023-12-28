## 概要

Bosch社製のセンサーBME280を使って温湿度と大気圧をOLEDに表示するサンプルです。タクトスイッチを押すことで右下の画像を切り替え、ソケット通信で簡単なWebサーバーを作りテキストを表示します。

![291956404-62c1d481-8774-489e-b8ef-7630af7fb385](https://github.com/quojama/pico-sensor/assets/4445606/65dec7af-0afc-489d-b554-3fbdccdfcf1d)

## 使うパーツ (秋月電子で調達)

- [Raspberry Pi Pico W](https://akizukidenshi.com/catalog/g/gM-17947/) (or [Pico](https://akizukidenshi.com/catalog/g/gM-16132/))
- [BME280 sensor module](https://akizukidenshi.com/catalog/g/gK-09421/)
- [0.96" SSD1306 OLED display](https://akizukidenshi.com/catalog/g/gP-12031/)
- [Tactile switch](https://akizukidenshi.com/catalog/g/gP-08073/)
- [3mm blue LED](https://akizukidenshi.com/catalog/g/gI-13233/)
  - LEDはなんでもいいですし、なくてもいいです。ただし繋がない場合は該当コードを削除してください。
- [Breadboard](https://akizukidenshi.com/catalog/g/gP-05294/)
  - こちらも必要に応じて出問題なしです。

## つなぎ方

| BME280 | Raspberry Pi Pico (W) | SSD1306 | LED     | Tactile switch |
| ------ | --------------------- | ------- | ------- | -------------- |
| VCC    | 3V3 (36pin)           | VCC     | -       | -              |
| GND    | GND                   | GND     | Cathode | GND            |
| -      | GP7 (10pin)           | SCL     | -       | -              |
| -      | GP6 (9pin)            | SDA     | -       | -              |
| CSB    | -                     | -       | -       | -              |
| SDI    | GP4 (6pin)            | -       | -       | -              |
| SDO    | GND                   | -       |         |                |
| SCK    | GP5 (7pin)            | -       | -       | -              |
| -      | GP10 (14pin)          | -       | Anode   | -              |
| -      | GP19 (25pin)          | -       | -       | To GND         |

## WIFIの設定

`/lib` ディレクトリに `env.py` ファイルを作成してSSIDとパスワードを設定してください。

```python
SSID = "YOUR SSID"
PASSWORD = "YOUR PASSWORD"
```
## テキストの切り替え

デフォルトは `Hello!` です。再起動時はこの値になります。

起動するとシェルにPicoのIPアドレスが表示されます。

```bash
Connection successful
('xxx.xxx.x.xx', 'xxxx.xxx.xxx.x', 'xxx.xxx.x.x', 'xxx.xxx.x.x')
```
`http://YOUR.IP.ADDRESS/` にアクセスし、テキストを入力すれば文字が変わります。

![image](https://github.com/quojama/pico-sensor/assets/4445606/537a0396-b74e-464e-b94a-bdd3b73b786f)

文字はスペースも含めて10～11文字以上は右下のイラストと被ってしまいますので良い感じにしてください。

セキュリティは考慮されていないので注意してくださいね。

## 画像の作り方

ディスプレイのサイズは128x64ドットです。何らかの方法で128x64pxのモノクロ二階調の画像を作成してください。JPGでもPNGでも問題ないです。

次に [img2ccp](https://javl.github.io/image2cpp/) を使って画像をプレーンのビットマップに変換します。最後のOutputの項目にあるCode output formatはPlain bytesを選択してください。

そちらのビットマップの文字列を.txtとして /img フォルダの中に保存するだけで追加されます。

## インストール済のイラストサンプル

![PXL_20231220_163648357](https://github.com/quojama/pico-sensor/assets/4445606/13964660-7d17-4830-9769-b543d7930795)

![PXL_20231220_163733769](https://github.com/quojama/pico-sensor/assets/4445606/cae4f6c6-7d80-4b24-a03e-18d8dab445b4)

![PXL_20231220_163715927](https://github.com/quojama/pico-sensor/assets/4445606/dead1a67-4469-447a-bb3d-1483873509a5)
