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
    return 'New values';

if __name__ == "__main__":
    app.run()