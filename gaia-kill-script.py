import keyboard
import pyautogui
import time

# Флаг для включения/выключения движения мыши
running = True

def toggle_mouse_movement():
    global running
    running = not running
    if running:
        print("Движение мыши включено")
    else:
        print("Движение мыши выключено")

# Привязываем комбинацию Alt+Z к функции переключения
keyboard.on_press_key("z", lambda e: toggle_mouse_movement() if keyboard.is_pressed("alt") else None)

print("Программа запущена. Нажмите Alt+Z для включения/выключения движения мыши. Убедитесь, что на вашем дк нагруднике 200% верт.ускорение и авт.вкл.полета")
print("Для выхода полностью закройте программу")
iter=1
# print(pyautogui.KEY_NAMES)
# Основной цикл

time.sleep(20)
while True:
    if running:
        # Убиваем Флюгелей
        pyautogui.keyDown('space')
        time.sleep(0.1)
        pyautogui.keyUp('space')

        for i in range (1, 8):
            pyautogui.press(str(i))
            pyautogui.click(clicks=8, interval=0.1)

        # Ожидаем перезарядки убийц флюгеля
        time.sleep(10)

        iter += 1

        # Убираем сломавшуюся душу
        # if ((iter > 1) and iter % 2 == 0):
        #     #Попытка удалять через терминал
        #     pyautogui.press(str(8))
        #     pyautogui.click(button='right', duration=0.1)
        #     pyautogui.moveRel(110, 410, duration=0.3)
        #     pyautogui.click(duration=0.1)
        #     pyautogui.moveRel(-120, -140, duration=0.3)
        #     pyautogui.click(duration=0.1)
        #     pyautogui.moveRel(17, -17, duration=0.3)
        #     pyautogui.click(duration=0.1)
        #     pyautogui.moveRel(0, -700, duration=0.3)
        #     pyautogui.click(duration=0.1)
        #     pyautogui.write('@alfheim', interval=0.1)
        #     pyautogui.moveRel(-170, 115, duration=0.3)
        #     pyautogui.keyDown('shift')
        #     pyautogui.click(clicks=1, interval=0.1)
        #     pyautogui.keyUp('shift')
        #     pyautogui.press('esc')

        # Спавн Флюгелей
        pyautogui.press('9')
        pyautogui.keyDown('shift')
        time.sleep(0.5)
        pyautogui.click(clicks=7, interval=1, button='right')
        pyautogui.keyUp('shift')
    else:
        # Небольшая задержка когда программа выключена, чтобы не нагружать процессор
        time.sleep(0.1)