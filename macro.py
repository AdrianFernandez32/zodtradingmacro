import win32api
import pyautogui
import keyboard
import time

# Variable to control macro interruption
stop_macro = False

# Function to set the stop key from the UI
def set_stop_key(key):
    global stop_key
    stop_key = key
    # Set up a global hotkey to stop the macro
    keyboard.add_hotkey(stop_key, lambda: stop_macro_set())

def stop_macro_set():
    global stop_macro
    stop_macro = True

def move_cursor_relative(dx, dy):
    # Get the current cursor position
    x, y = win32api.GetCursorPos()
    # Move the cursor to the new relative position
    win32api.SetCursorPos((x + dx, y + dy))

def run_macro(break_time, delay):
    global stop_macro
    stop_macro = False  # Reset the variable when starting the macro

    # Initialization
    time.sleep(3)
    pyautogui.press('e')
    pyautogui.press('e')
    
    while not stop_macro:
        pyautogui.mouseDown(button='left')  # Start holding the left mouse button
        time.sleep(break_time)  # Hold the button for the calculated break time
        pyautogui.mouseUp(button='left')  # Release the left mouse button
        pyautogui.click(button='right')
        time.sleep(1.4)  # Wait for the villager to recognize the lectern
        
        keyboard.press('space')  # Press the space bar
        time.sleep(0.1)  # Short delay for the jump
        keyboard.release('space')  # Release the space bar
        time.sleep(0.28)
        
        pyautogui.click(button='right')  # Open the villager menu
        time.sleep(0.1)
        move_cursor_relative(-125, -110)
        time.sleep(delay / 2)
        move_cursor_relative(0, 35)
        time.sleep(delay / 2)  # Wait to view the enchantment
        
        pyautogui.press('e')  # Close the menu
        time.sleep(0.5)  # Wait before repeating
