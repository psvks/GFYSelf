import ctypes

def makeBuggyScreen(): # THIS IS VERY BAD, DO NOT USE IT IF YOU ARE NOT SURE.
    # Definir constantes
    HWND_BROADCAST = 0xFFFF
    WM_SYSCOMMAND = 0x0112
    SC_MONITORPOWER = 0xF170
    MONITOR_OFF = 2
    MONITOR_ON = -1

    # Obtener el manejador de la ventana activa
    hWnd = ctypes.windll.user32.GetForegroundWindow()

    # Apagar pantalla
    ctypes.windll.user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, MONITOR_OFF)

    # Encender pantalla
    ctypes.windll.user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, MONITOR_ON)
