from pynput import keyboard
import pickle
import cv2
from graph import Graph

GAME = "1"
ITER = "1"
FRAMES = 54120
VID_STRIDE=90

last_classification = 8


def label_classification(key) -> int:
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


cap = cv2.VideoCapture("videos/coop/game1.mp4")
ret, frame = cap.read()

listener = keyboard.Listener(
    on_press=label_classification,
)
listener.start()

with open(f"unlabeled_graphs/game{GAME}.pickle", "rb") as unlabeled:
    with open(f"labeled_graphs/game{GAME}_{ITER}.pickle", "wb") as labeled:
        for idx in range(1, FRAMES + 1):
            ret, frame = cap.read()
            cv2.imshow('frame',frame)

            if cv2.waitKey(1) & 0xFF == ord('q') or ret==False :
                cap.release()
                cv2.destroyAllWindows()
                break
            cv2.imshow('frame',frame)
                
            if idx % VID_STRIDE == 0:
                graph: Graph = pickle.load(unlabeled)
                graph.add_classification(last_classification)
                
                print(f"i: {idx}, {last_classification}, {graph.attacking_classification}")
                if last_classification == 'q':
                    break
                pickle.dump(graph, labeled)

listener.stop()
listener.join()
