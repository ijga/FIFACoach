import time
from pynput import keyboard
    
def classification_label(key) -> int:
    global last_classification
    if key.char == '1':
        last_classification = 1
    elif key.char == '2':
        last_classification = 2
    elif key.char == '3':
        last_classification = 3
    elif key.char == '4':
        last_classification = 4
    elif key.char == '5':
        last_classification = 5
    elif key.char == '6':
        last_classification = 6
    elif key.char == '7':
        last_classification = 7
    elif key.char == '8':
        last_classification = 8
    elif key.char == 'q':
        last_classification = 'q'
    else:
        last_classification = '0'


last_classification = 8
for i in range (10000):

    listener = keyboard.Listener(
        on_press=classification_label,
    )
    listener.start()

    time.sleep(1)
    listener.stop()
    listener.join()
    print(f"i: {i}, {last_classification}")
    if last_classification == 'q':
        break

print('end program')