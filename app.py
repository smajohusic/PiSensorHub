from flask import Flask, render_template, jsonify, json
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
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)

    if humidity is not None and temperature is not None:
        return json.dumps({'temperature': '{0:0.1f}'.format(temperature), 'humidity': '{1:0.1f}'.format(humidity)});

    return null

if __name__ == "__main__":
    app.run()