from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import pyautogui  # Importa pyautogui para el movimiento del cursor
import keyboard  # Importa keyboard para escuchar la tecla de detención
import time
import threading

# Inicializa los controladores
keyboard_ctrl = KeyboardController()
mouse = MouseController()

# Variable global para controlar la interrupción del macro
stop_macro = False
stop_key = 'backspace'  # Tecla de detención por defecto (personalizable)

# Función para configurar la tecla de detención
def set_stop_key(key):
    global stop_key
    stop_key = key

def stop_macro_set():
    global stop_macro
    stop_macro = True

# Hilo para monitorear la tecla de detención con keyboard
def monitor_stop_key():
    global stop_macro
    while not stop_macro:
        if keyboard.is_pressed(stop_key):
            stop_macro_set()
            break
        time.sleep(0.1)

def move_cursor_relative(dx, dy):
    # Obtiene la posición actual del cursor y mueve de forma relativa usando pyautogui
    x, y = pyautogui.position()
    pyautogui.moveTo(x + dx, y + dy)

def run_macro(break_time, delay):
    global stop_macro
    stop_macro = False  # Reinicia la variable stop al iniciar el macro

    # Inicia el monitor de tecla de detención en un hilo separado
    stop_thread = threading.Thread(target=monitor_stop_key)
    stop_thread.start()

    # Inicialización
    time.sleep(3)

    # Presiona 'e' dos veces para iniciar
    keyboard_ctrl.press('e')
    keyboard_ctrl.release('e')
    time.sleep(0.1)
    keyboard_ctrl.press('e')
    keyboard_ctrl.release('e')

    while not stop_macro:
        # Mantiene el botón izquierdo del mouse
        mouse.press(Button.left)
        time.sleep(break_time)  # Mantener el botón por el tiempo calculado
        mouse.release(Button.left)
        
        # Clic derecho
        mouse.click(Button.right)
        time.sleep(1.4)  # Espera a que el aldeano reconozca el atril

        # Salta con la barra espaciadora
        keyboard_ctrl.press(Key.space)
        time.sleep(0.1)
        keyboard_ctrl.release(Key.space)
        time.sleep(0.28)
        
        # Clic derecho de nuevo
        mouse.click(Button.right)
        time.sleep(0.1)
        
        # Mueve el cursor para revisar encantamientos usando pyautogui
        move_cursor_relative(-125, -110)
        time.sleep(delay / 2)
        move_cursor_relative(0, 35)
        time.sleep(delay / 2)  # Espera para ver el encantamiento

        # Cierra el menú con 'esc'
        keyboard_ctrl.press(Key.esc)
        keyboard_ctrl.release(Key.esc)
        time.sleep(0.5)  # Espera antes de repetir
