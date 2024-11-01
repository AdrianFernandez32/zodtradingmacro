import tkinter as tk
from tkinter import messagebox
import threading
from macro import run_macro, set_stop_key  # Importa la función del macro y la función para establecer la tecla de detención

# Cálculo del tiempo de rotura basado en el material y encantamiento
def calculate_break_time(material, efficiency_level):
    base_times = {
        "Madera": 1.9,
        "Piedra": 0.95,
        "Hierro": 0.65,
        "Diamante": 0.5,
        "Netherite": 0.45,
        "Oro": 0.35
    }
    efficiency_multipliers = {
        "Sin Encantamiento": 1.0,
        "Eficiencia I": 1.25,
        "Eficiencia II": 1.3,
        "Eficiencia III": 1.35,
        "Eficiencia IV": 1.4,
        "Eficiencia V": 1.5
    }
    base_time = base_times.get(material, 1.15)
    multiplier = efficiency_multipliers.get(efficiency_level, 1.0)
    return base_time / multiplier

# Función para iniciar el macro desde la UI
def start_macro():
    try:
        material = material_var.get()
        efficiency_level = efficiency_var.get()
        delay = float(delay_entry.get())
        stop_key = stop_key_var.get()

        # Configura la tecla de detención
        set_stop_key(stop_key)

        # Calcula el tiempo de rotura del atril
        break_time = calculate_break_time(material, efficiency_level)
        
        messagebox.showinfo("Macro", f"El macro ha comenzado con el hacha de {material} y {efficiency_level}. Usa {stop_key} para detenerlo.")
        # Llama a la función del macro en un hilo
        macro_thread = threading.Thread(target=run_macro, args=(break_time, delay))
        macro_thread.start()  # Inicia el macro en un hilo separado
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores válidos.")

# Configuración de la UI con tkinter
root = tk.Tk()
root.title("Minecraft Macro")
root.geometry("300x300")

# Selección de tipo de hacha
tk.Label(root, text="Material del Hacha:").pack()
material_var = tk.StringVar(value="Madera")
material_options = ["Madera", "Piedra", "Hierro", "Diamante", "Netherite"]
material_menu = tk.OptionMenu(root, material_var, *material_options)
material_menu.pack()

# Selección de encantamiento
tk.Label(root, text="Encantamiento:").pack()
efficiency_var = tk.StringVar(value="Sin Encantamiento")
efficiency_options = ["Sin Encantamiento", "Eficiencia I", "Eficiencia II", "Eficiencia III", "Eficiencia IV", "Eficiencia V"]
efficiency_menu = tk.OptionMenu(root, efficiency_var, *efficiency_options)
efficiency_menu.pack()

# Selección de la tecla de detención
tk.Label(root, text="Tecla de detención:").pack()
stop_key_var = tk.StringVar(value="F10")
stop_key_options = ["backspace", "enter", "tab"] + [f"f{i}" for i in range(1, 13)]
stop_key_menu = tk.OptionMenu(root, stop_key_var, *stop_key_options)
stop_key_menu.pack()

# Tiempo de espera para revisar el encantamiento
tk.Label(root, text="Tiempo de espera (s):").pack()
delay_entry = tk.Entry(root)
delay_entry.pack()

# Botón para iniciar el macro
start_button = tk.Button(root, text="Iniciar Macro", command=start_macro)
start_button.pack()

# Loop de tkinter
root.mainloop()
