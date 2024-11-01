import tkinter as tk
from tkinter import messagebox
import threading
from macro import run_macro, set_stop_key  # Import macro function and function to set the stop key

# Calculate break time based on material and enchantment
def calculate_break_time(material, efficiency_level):
    base_times = {
        "Wood": 2,
        "Stone": 1,
        "Iron": 0.75,
        "Diamond": 0.6,
        "Netherite": 0.55,
        "Gold": 0.45,
        "Raw Salmon": 3.7
    }
    efficiency_multipliers = {
        "No Enchantment": 1.0,
        "Efficiency I": 1.25,
        "Efficiency II": 1.3,
        "Efficiency III": 1.35,
        "Efficiency IV": 1.4,
        "Efficiency V": 1.5
    }
    base_time = base_times.get(material, 1.15)
    multiplier = efficiency_multipliers.get(efficiency_level, 1.0)
    return base_time / multiplier

# Function to start the macro from the UI
def start_macro():
    try:
        material = material_var.get()
        efficiency_level = efficiency_var.get()
        delay = float(delay_entry.get())
        stop_key = stop_key_var.get()

        # Set the stop key
        set_stop_key(stop_key)

        # Calculate the break time for the lectern
        break_time = calculate_break_time(material, efficiency_level)
        
        messagebox.showinfo("Macro", f"The macro has started with the {material} axe and {efficiency_level}. Use {stop_key} to stop it.")
        # Start the macro function in a separate thread
        macro_thread = threading.Thread(target=run_macro, args=(break_time, delay))
        macro_thread.start()  # Start the macro in a separate thread
    except ValueError:
        messagebox.showerror("Error", "Please enter valid values.")

# UI setup with tkinter
root = tk.Tk()
root.title("Zod's Trading macro")
root.geometry("300x300")

# Axe material selection
tk.Label(root, text="Axe Material:").pack()
material_var = tk.StringVar(value="Wood")
material_options = ["Wood", "Stone", "Iron", "Diamond", "Netherite"]
material_menu = tk.OptionMenu(root, material_var, *material_options)
material_menu.pack()

# Enchantment selection
tk.Label(root, text="Enchantment:").pack()
efficiency_var = tk.StringVar(value="No Enchantment")
efficiency_options = ["No Enchantment", "Efficiency I", "Efficiency II", "Efficiency III", "Efficiency IV", "Efficiency V"]
efficiency_menu = tk.OptionMenu(root, efficiency_var, *efficiency_options)
efficiency_menu.pack()

# Stop key selection
tk.Label(root, text="Stop Key:").pack()
stop_key_var = tk.StringVar(value="F10")
stop_key_options = ["backspace", "enter", "tab"] + [f"f{i}" for i in range(1, 13)]
stop_key_menu = tk.OptionMenu(root, stop_key_var, *stop_key_options)
stop_key_menu.pack()

# Delay for checking enchantment
tk.Label(root, text="Delay (s):").pack()
delay_entry = tk.Entry(root)
delay_entry.pack()

# Button to start the macro
start_button = tk.Button(root, text="Start Macro", command=start_macro)
start_button.pack()

# tkinter loop
root.mainloop()
