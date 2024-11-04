"""
Author: Ved Vyas
Functionality of code:
So I made this code to protect our ballot boxes from getting burned down. I was really angry 
when I heard about the recent incidents, so I decided to make a simple protection system 
that uses a Raspberry Pi. It's pretty straightforward - if someone tries to burn the box, 
it'll catch them in the act with a photo, make a loud noise to scare them off, and spray 
some water to stop the fire. Then it sends everything to the police. Nothing fancy, just 
practical stuff that could actually help protect our democracy.
"""

import RPi.GPIO as GPIO  # I'm using this to control the Raspberry Pi's pins
import time  # Need this for adding delays and timestamps
from picamera import PiCamera  # This lets me take photos with the Pi camera
import requests  # I'll use this to send alerts to the police

class SimpleBallotProtection:
    def __init__(self):
        # I'm setting up the pin numbers for my sensors and devices
        self.FIRE_SENSOR_PIN = 17  # Connected my fire sensor to pin 17
        self.BUZZER_PIN = 18       # My alarm buzzer is on pin 18
        self.PUMP_PIN = 19         # Water pump connects to pin 19
        
        # Setting up how I want to control these pins
        GPIO.setmode(GPIO.BCM)  # I prefer using the BCM pin numbering system
        GPIO.setup(self.FIRE_SENSOR_PIN, GPIO.IN)  # Fire sensor needs to send signals in
        GPIO.setup(self.BUZZER_PIN, GPIO.OUT)      # Buzzer will receive signals from Pi
        GPIO.setup(self.PUMP_PIN, GPIO.OUT)        # Same for the water pump
        
        # Getting my camera ready to take photos
        self.camera = PiCamera()  # This creates my camera object so I can take pictures
        
    def sound_alarm(self):
        """When someone messes with the box, I'm making this thing LOUD"""
        GPIO.output(self.BUZZER_PIN, GPIO.HIGH)  # Turning my buzzer on full blast
        
    def stop_alarm(self):
        """Okay, enough noise - time to shut it off"""
        GPIO.output(self.BUZZER_PIN, GPIO.LOW)  # Turning the buzzer off
        
    def activate_pump(self):
        """Fire detected? Let's get that water flowing!"""
        GPIO.output(self.PUMP_PIN, GPIO.HIGH)  # Turning on my water pump
        
    def stop_pump(self):
        """Fire should be out by now, so I'm turning off the water"""
        GPIO.output(self.PUMP_PIN, GPIO.LOW)  # Shutting down the pump
        
    def take_photo(self):
        """Smile for the camera! This takes a snapshot of whoever's messing with our democracy"""
        # I'm adding a timestamp to the photo name so I can keep track of when stuff happens
        photo_name = f'incident_{time.strftime("%Y%m%d_%H%M%S")}.jpg'
        self.camera.capture(photo_name)  # Actually taking the photo
        return photo_name  # Sending back the file name so I can use it later
        
    def alert_authorities(self, photo_path):
        """Time to let the police know what's going down"""
        # This is where I'd put the actual police department's web address
        police_url = "http://police-department.gov/alert"
        
        try:
            # Packaging up all the evidence
            with open(photo_path, 'rb') as photo:
                alert_data = {
                    'location': 'Ballot Box 1',  # Which ballot box got hit
                    'incident': 'Fire detected',  # What happened
                    'time': time.strftime("%Y-%m-%d %H:%M:%S")  # When it happened
                }
                files = {'photo': photo}  # Adding the photo I just took
                # Sending everything to the police
                requests.post(police_url, data=alert_data, files=files)
        except:
            # If something goes wrong with the alert, I at least want to know about it
            print("Failed to send alert to authorities")
            
    def run(self):
        """This is my main program that keeps watch 24/7"""
        try:
            print("Ballot box protection system is running...")  # Just letting myself know it's working
            while True:  # This keeps running until someone stops it
                if GPIO.input(self.FIRE_SENSOR_PIN):  # Checking if my fire sensor detected anything
                    print("Fire detected! Taking action...")  # Logging that we caught something
                    
                    # First thing's first - get a photo of whoever's doing this
                    photo = self.take_photo()
                    
                    # Time to make some noise and spray some water!
                    self.sound_alarm()
                    self.activate_pump()
                    
                    # Letting the police know what's happening
                    self.alert_authorities(photo)
                    
                    # Keep the alarm and water running for 10 seconds
                    time.sleep(10)
                    
                    # Okay, should be handled by now - turning everything off
                    self.stop_alarm()
                    self.stop_pump()
                    
                time.sleep(0.5)  # I check for fire every half second - seems like a good balance
                
        except KeyboardInterrupt:
            # If I need to shut it down, I want to do it cleanly
            print("Shutting down...")
        finally:
            # Always clean up my GPIO pins and close the camera properly
            GPIO.cleanup()
            self.camera.close()

# This is where my program actually starts running
if __name__ == "__main__":
    protection = SimpleBallotProtection()  # Creating my protection system
    protection.run()  # Starting the guard duty!