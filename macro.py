import win32api
import pyautogui
import keyboard
import time

# Variable para controlar la interrupción del macro
stop_macro = False

# Función para configurar la tecla de detención desde la UI
def set_stop_key(key):
    global stop_key
    stop_key = key
    # Configura la tecla de acceso rápido global para detener el macro
    keyboard.add_hotkey(stop_key, lambda: stop_macro_set())

def stop_macro_set():
    global stop_macro
    stop_macro = True
    print(f"Macro detenido por tecla {stop_key}")

def move_cursor_relative(dx, dy):
    # Obtiene la posición actual del cursor
    x, y = win32api.GetCursorPos()
    # Mueve el cursor a la nueva posición relativa
    win32api.SetCursorPos((x + dx, y + dy))

def run_macro(break_time, delay):
    global stop_macro
    stop_macro = False  # Reinicia la variable al iniciar el macro

    # Inicializa
    time.sleep(3)
    pyautogui.press('e')
    pyautogui.press('e')
    
    while not stop_macro:
        pyautogui.mouseDown(button='left')  # Empieza a sostener el botón izquierdo
        time.sleep(break_time)  # Mantiene el botón presionado según el tiempo de rotura calculado
        pyautogui.mouseUp(button='left')  # Suelta el botón izquierdo
        pyautogui.click(button='right')
        time.sleep(1.4)  # Esperar para que el aldeano reconozca el atril
        
        keyboard.press('space')  # Presiona la barra espaciadora
        time.sleep(0.1)  # Espera un breve momento mientras salta
        keyboard.release('space')  # Suelta la barra espaciadora
        time.sleep(0.28)
        
        pyautogui.click(button='right')  # Abre el menú del aldeano
        time.sleep(0.1)
        move_cursor_relative(-125, -110)
        time.sleep(delay / 2)
        move_cursor_relative(0, 35)
        time.sleep(delay / 2)  # Espera para ver el encantamiento
        
        pyautogui.press('e')  # Cierra el menú
        time.sleep(0.5)  # Espera antes de repetir
