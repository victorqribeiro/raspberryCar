
from flask import Flask, render_template,request,redirect,url_for
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#motor A
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

#motor B
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

app = Flask(__name__)
title = "RaspberryCar"
heading = "ToDo Reminder"

@app.route("/")
def tasks():
	return render_template('index.html')

@app.route("/forward")
def forward():
	GPIO.output(17, GPIO.HIGH)
	GPIO.output(27, GPIO.LOW)
	GPIO.output(23, GPIO.HIGH)
	GPIO.output(24, GPIO.LOW)
	sleep(1)
	GPIO.output(17, GPIO.LOW)
	GPIO.output(27, GPIO.LOW)
	GPIO.output(23, GPIO.LOW)
	GPIO.output(24, GPIO.LOW)
	return redirect("/")
	
@app.route("/backwards")
@app.route("/backward")
def backward():
	GPIO.output(17, GPIO.LOW)
	GPIO.output(27, GPIO.HIGH)
	GPIO.output(23, GPIO.LOW)
	GPIO.output(24, GPIO.HIGH)
	sleep(1)
	GPIO.output(17, GPIO.LOW)
	GPIO.output(27, GPIO.LOW)
	GPIO.output(23, GPIO.LOW)
	GPIO.output(24, GPIO.LOW)
	return redirect("/")

@app.route("/left")
def left():	
	GPIO.output(17, GPIO.LOW)
	GPIO.output(27, GPIO.HIGH)
	GPIO.output(23, GPIO.HIGH)
	GPIO.output(24, GPIO.LOW)
	sleep(1)
	GPIO.output(17, GPIO.LOW)
	GPIO.output(27, GPIO.LOW)
	GPIO.output(23, GPIO.LOW)
	GPIO.output(24, GPIO.LOW)
	return redirect("/")
	
@app.route("/right")
def right():
	GPIO.output(17, GPIO.HIGH)
	GPIO.output(27, GPIO.LOW)
	GPIO.output(23, GPIO.LOW)
	GPIO.output(24, GPIO.HIGH)

	sleep(1)
	GPIO.output(17, GPIO.LOW)
	GPIO.output(27, GPIO.LOW)
	GPIO.output(23, GPIO.LOW)
	GPIO.output(24, GPIO.LOW)
	return redirect("/")
	
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080, debug=True)
