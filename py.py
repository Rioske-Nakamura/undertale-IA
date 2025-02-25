import pyautogui
import time
import keyboard  # Necessário para detectar pressionamento de teclas

# Lista das teclas de seta
setas = ['up', 'right', 'down', 'left']
executando = True  # Define o estado inicial como 'executando'
z_ativado = False  # Variável para alternar o estado da tecla "z"

def verificar_pausa():
    global executando
    if keyboard.is_pressed('p') and keyboard.is_pressed('s'):
        time.sleep(0.3)  # Evita múltiplos cliques rápidos
        executando = not executando  # Alterna entre pausar e continuar
        print(f'Código {"pausado" if not executando else "iniciado"}')

def verificar_z():
    global z_ativado
    if keyboard.is_pressed("z"):
        time.sleep(0.3)  # Evita múltiplas ativações rápidas
        z_ativado = not z_ativado  # Alterna entre ativado/desativado
        print(f'Pressionamento automático de "z" {"ativado" if z_ativado else "desativado"}')

while True:
    verificar_pausa()
    verificar_z()

    if z_ativado:
        pyautogui.press("z")  # Pressiona a tecla "z" repetidamente 
        time.sleep(0.2)  # Pequeno intervalo entre pressões para não sobrecarregar

    if executando:
        for seta in setas:
            verificar_pausa()
            verificar_z()
            pyautogui.keyDown(seta)
            time.sleep(3)
            pyautogui.keyUp(seta)
            time.sleep(1)
    else:
        time.sleep(0.1)  # Aguarda um tempo menor para resposta mais rápida
