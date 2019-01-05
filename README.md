# raspberryCar

A raspberry pi on wheels. See it working below.

[![groupImg](http://img.youtube.com/vi/4IDLDofuuLc/0.jpg)](http://www.youtube.com/watch?v=4IDLDofuuLc)

## About

This is my first real experiment with robotics. I've ordered the arduino car kit on the internet, but some parts went missing. 
So, instead of a arduino, I've used my raspberry pi to control the wheels. 
I wrote a simple flask server to expose the commands (go left, right, forward and backward) over the internet, that could be accessed by any device. 
Later I decided to use [myChatBot](https://github.com/victorqribeiro/myChatBot) to control the car.

## Brag

This project was featured on HACKADAY - [Control Anything With a Chat Bot](https://hackaday.com/2019/01/05/control-anything-with-a-chat-bot).

## Warning

You might have to add the address of the server as a trusted site, If you want to use the voice control without a SSL certificate.
