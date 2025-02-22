import pyautogui
import time
import keyboard  # Necessário para detectar pressionamento de teclas

# Lista das teclas de seta
setas = ['up', 'right', 'down', 'left']
executando = True  # Define o estado inicial como 'executando'

# Variável para detectar o pressionamento das teclas
toggle_pausar = False

while True:
    # Detecta o pressionamento da tecla "P" e "S" em sequência
    if keyboard.is_pressed('p') and not toggle_pausar:
        time.sleep(0.3)  # Espera um pouco para evitar múltiplos cliques rápidos
        toggle_pausar = True
        print(f'Código {"pausado" if not executando else "iniciado"}')

    if keyboard.is_pressed('s') and toggle_pausar:
        time.sleep(0.3)  # Espera um pouco para evitar múltiplos cliques rápidos
        executando = not executando  # Alterna entre pausar e continuar
        toggle_pausar = False  # Reseta a variável para permitir a troca da tecla P

  

    # Se o código estiver em execução, executa a sequência
    if executando:
        for seta in setas:
            pyautogui.keyDown(seta)  # Mantém a tecla pressionada
            time.sleep(3)  # Aguarda 3 segundos com a tecla pressionada
            pyautogui.keyUp(seta)  # Solta a tecla
            time.sleep(1)  # Intervalo de 1 segundo entre as teclas
    else:
        time.sleep(1)  # Aguarda um tempo caso esteja pausado
