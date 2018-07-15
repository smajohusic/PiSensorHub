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
        data = []
        data[0]('{0:0.1f}'.format(temperature))
        data[1]('{1:0.1f}'.format(humidity))

        jsonString = json.dumps(data)

        return jsonify(data=jsonString)

    return null

if __name__ == "__main__":
    app.run()