"""
Authors: Ved Vyas , Maarifa International Club
Functionality of code:
/* I created this program after seeing those terrible ballot box fire incidents during 
the November 2024 election. I was really upset about it and wanted to do something to 
help. Even though I'm still learning Python, I figured I could make a basic protection 
system. My program is pretty simple - it just reads from a fire sensor and if it 
detects fire, it sends signals to turn on sprinklers, alarms, and cameras. I know 
it's not super fancy, but I hope it can help protect the voting process. */



#Operative clause: 
#HEREBY PROPOSE the following technological solution for ballot box protection:

# I need this to add delays in my program
import time

def read_fire_sensor():
    # Here I'm trying to read from my fire sensor file
    try:
        # Opening my sensor file to check its reading
        with open('fire_sensor.txt', 'r') as file:
            # Getting the number from the file (should be 0 or 1)
            reading = int(file.read().strip())
            return reading
    except:
        # If something goes wrong reading the file, I'll print an error
        print("Can't read fire_sensor.txt!")
        return 0

def send_signal_to_sprinkler(signal):
    # This is where I send the on/off signal to my sprinkler system
    try:
        # Opening the sprinkler control file
        with open('sprinkler_signal.txt', 'w') as file:
            # Writing either 1 (on) or 0 (off) to the file
            file.write(str(signal))
        # Letting myself know the signal was sent
        print("Sprinkler signal sent:", signal)
    except:
        # If there's a problem, I want to know about it
        print("Couldn't send signal to sprinkler!")

def send_signal_to_alarm(signal):
    # Similar to my sprinkler function, but this one controls the alarm
    try:
        # Opening the alarm control file
        with open('alarm_signal.txt', 'w') as file:
            # Sending the on/off signal
            file.write(str(signal))
        # Confirming the signal was sent
        print("Alarm signal sent:", signal)
    except:
        # Letting myself know if something went wrong
        print("Couldn't send signal to alarm!")

def send_signal_to_camera(signal):
    # This function controls my camera system
    try:
        # Opening the camera control file
        with open('camera_signal.txt', 'w') as file:
            # Writing the signal to turn camera on or off
            file.write(str(signal))
        # Print confirmation that it worked
        print("Camera signal sent:", signal)
    except:
        # Error message if it fails
        print("Couldn't send signal to camera!")

# This is where my main program starts!
print("Starting my ballot box protection program...")
print("Put 1 in fire_sensor.txt to simulate fire, 0 for no fire")
print("Check sprinkler_signal.txt, alarm_signal.txt, and camera_signal.txt for outputs")
print("Press Ctrl+C to stop")

try:
    # My program will keep running until I stop it
    while True:
        # First, I need to check my fire sensor
        fire_detected = read_fire_sensor()
        
        # If my sensor detects fire (reads 1)...
        if fire_detected == 1:
            print("\n!!! FIRE DETECTED !!!")
            print("Sending signals to all systems...")
            
            # Turn on all my protection systems at once
            send_signal_to_camera(1)    # Start recording
            send_signal_to_alarm(1)     # Sound the alarm
            send_signal_to_sprinkler(1) # Start spraying water
            
            print("All systems activated!")
            print("Waiting 5 seconds...")
            # I wait 5 seconds before checking again
            time.sleep(5)
            
        else:
            # If there's no fire, I make sure all systems are off
            send_signal_to_camera(0)    # Stop recording
            send_signal_to_alarm(0)     # Turn off alarm
            send_signal_to_sprinkler(0) # Stop water
            
            print("No fire detected - systems on standby")
            # I check again every 2 seconds
            time.sleep(2)
        
except KeyboardInterrupt:
    # This runs when I press Ctrl+C to stop the program
    print("\nStopping program...")
    # I make sure to turn everything off before stopping
    send_signal_to_camera(0)
    send_signal_to_alarm(0)
    send_signal_to_sprinkler(0)
    print("All systems off!")
