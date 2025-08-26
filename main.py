import pyautogui
import time


# Function to move the mouse up and down and click after movement
def move_and_click(repeat, move_distance, delay):
    x = 0
    minutes_to_run = 60
    while x < minutes_to_run:
        # Move mouse up
        pyautogui.move(0, -move_distance)
        pyautogui.click()
        pyautogui.move(0, move_distance)
        time.sleep(delay)

        x += 1


# Parameters
repeat = 10  # Number of up and down movements
move_distance = 100  # Distance in pixels to move the mouse
delay = 60  # Delay in seconds between movements

# Run the function
move_and_click(repeat, move_distance, delay)
