# This script reads angle and distance data from the Arduino over the serial port
# and visualizes it as a radar screen with a rectangular, half-screen layout.

add_library('serial')

serial_port = None    # The serial port object
font = None    # Font for displaying text
in_string = ""    # String to buffer data from serial

screen_width = 800
screen_height = 450    # Half the original height with some padding

# Radar screen properties
radar_radius = 350
radar_center_x = screen_width / 2

# Position the radar's baseline near the bottom of the window
radar_center_y = screen_height - 100

# Data from Arduino
current_angle = 0
current_distance = 0

# Data storage for drawing points
points_history = []

def setup():
    """
    This function runs once when the program starts.
    It sets up the display window, initializes the serial communication and
    loads the font.
    """
    global serial_port, font

    # --- Window and Graphics setup ---
    # CHANGED: Use the new rectangular dimensions
    size(screen_width, screen_height)
    smooth()

    # Create 

    pass