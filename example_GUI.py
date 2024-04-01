import tkinter as tk
from pyfirmata import Arduino, util
import time

class ArduinoGUI:
    def __init__(self, master):
        self.master = master
        master.title("Arduino LED PWM Control")

        # Connect to Arduino
        # Adjust your Arduino connection port accordingly
        # self.board = Arduino('/dev/ttyUSB0') 
        # self.board = Arduino('/dev/ttyUSB1')
        self.board = Arduino('/dev/ttyACM0')
        # self.board = Arduino('/dev/ttyACM1')

        self.led_pin = self.board.get_pin('d:11:p')  # d for digital, 11 for pin, p for PWM

        # Create a GUI slider for controlling LED brightness
        self.brightness_scale = tk.Scale(master, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, label="Brightness", command=self.update_brightness)
        self.brightness_scale.pack()

        # Initialize LED brightness
        self.update_brightness(0)

    def update_brightness(self, brightness):
        self.led_pin.write(float(brightness))

    def close(self):
        self.board.exit()
        self.master.destroy()

# Create the GUI window
root = tk.Tk()
app = ArduinoGUI(root)

# Ensure the application cleans up properly upon exit
root.protocol("WM_DELETE_WINDOW", app.close)

# Run the application
root.mainloop()