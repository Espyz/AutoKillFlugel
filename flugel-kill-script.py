import keyboard
import pyautogui
import time

# Флаг для включения/выключения движения мыши
running = False

def toggle_mouse_movement():
    global running
    running = not running
    if running:
        print("Движение мыши включено")
    else:
        print("Движение мыши выключено")

# Привязываем комбинацию Ctrl+Z к функции переключения
keyboard.on_press_key("z", lambda e: toggle_mouse_movement() if keyboard.is_pressed("alt") else None)

print("Программа запущена. Нажмите Ctrl+Z для включения/выключения движения мыши")
print("Для выхода полностью закройте программу")
iter=0
# print(pyautogui.KEY_NAMES)
# Основной цикл
while True:
    if running:
        # Убиваем Флюгелей
        pyautogui.moveRel(0, -5000, duration=0.35)
        for i in range (1, 8):
            pyautogui.press(str(i))
            pyautogui.click(clicks=8, interval=0.1)

        # Ожидаем перезарядки убийц флюгеля
        time.sleep(10)

        # Набираем Души флюгеля
        if (iter % 20 == 0):
            pyautogui.press('8', interval=0.5)
            time.sleep(0.1)
            pyautogui.click(button='right', duration=0.1)
            pyautogui.moveRel(0, -440, duration=0.3)
            pyautogui.click(duration=0.1)
            pyautogui.write('@alfheim', interval=0.1)
            pyautogui.moveRel(-170, 115, duration=0.3)
            pyautogui.keyDown('shift')
            pyautogui.click(clicks=20, interval=0.1)
            pyautogui.keyUp('shift')
            pyautogui.press('esc')
        iter += 1

        # Убираем сломавшуюся душу
        if ((iter > 1) and iter % 2 == 1):
            pyautogui.moveRel(3000, 0, duration=0.3)
            pyautogui.press('9')
            pyautogui.press('q')
            pyautogui.moveRel(-3000, 0, duration=0.3)

        # Спавн Флюгелей
        pyautogui.moveRel(0, 5000, duration=0.35)
        pyautogui.press('9')
        pyautogui.keyDown('shift')
        pyautogui.click(clicks=7, interval=1, button='right')
        pyautogui.keyUp('shift')
    else:
        # Небольшая задержка когда программа выключена, чтобы не нагружать процессор
        time.sleep(0.1)