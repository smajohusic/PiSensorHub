from flask import Flask, render_template
import sys
import time
import Adafruit_DHT

app = Flask(__name__)
app.debug = True

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/api/temperature-and-humidity')
def temperatureAdnHumidity():
    sensor = Adafruit_DHT.DHT22
    pin = 23

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        return jsonify({
                'temperature': '{0:0.1f}'.format(temperature),
                'humidity': '{1:0.1f}'.format(humidity),
            })

    return null

if __name__ == "__main__":
    app.run()