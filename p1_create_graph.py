from ultralytics import YOLO
import numpy as np
import cv2
from graph import Graph, Player, Edge, Ball, Goal
from classes import class_names
import pickle

GAME = "1"

def run():
   
    model = YOLO('models/best7_coop.pt')
    np.set_printoptions(threshold = np.inf)

    results = model(source=f"videos/coop/game{GAME}.mp4", imgsz=1920, show=True, stream=True, vid_stride=90)

    # 1080
    Hs = np.array([[ 5.94007434e-01,  1.18369697e+00,  3.77156029e+02],
                [-1.29464862e-15,  2.22727388e+00, -1.82615885e+02],
                [-7.25486452e-19,  1.24457088e-03,  1.00000000e+00]])

    with open(f"unlabeled_graphs/game{'5'}.pickle", "wb") as file:
        for idx, result in enumerate(results):

            confidence = result.boxes.conf.numpy()
            classes = result.boxes.cls.numpy()

            boxes = result.boxes.xywh.numpy()[:, :2] 
            boxes[:, 1] += (result.boxes.xywh.numpy()[:, 3] * 0.5)
            points = boxes.reshape(1, -1, 2)
            
            transformed_points = np.array([])
            try:
                transformed_points = cv2.perspectiveTransform(points, Hs)
                if len(transformed_points) > 0: # error thrown if null
                    pass
            except:
                transformed_points = np.array([])

            img = np.ones((1080, 1920, 3), dtype=np.uint8)  # 1080p
            img = 200 * img # make it gray

            graph = Graph()
            if len(transformed_points) > 0:
                idx = 0
                for type, point in zip(classes, transformed_points[0, :, :]):
                    type = int(type)
                    
                    if class_names[type] == 'man_city' or class_names[type] == 'man_utd':
                        graph.add_player(Player(idx, class_names[type], point[0], point[1]))
                    elif class_names[type] == 'man_city_gk' or class_names[type] == 'man_utd_gk':
                        graph.add_gk(Player(idx, class_names[type], point[0], point[1]))
                    elif class_names[type] == 'ball':
                        graph.add_ball(Ball(idx, point[0], point[1]))
                    elif class_names[type] == 'left_goal' or class_names[type] == 'right_goal':
                        graph.add_goal(Goal(idx, type, point[0], point[1]))

                    if type == 4: # man_city
                        cv2.circle(img, (int(point[0]), int(point[1])), 3, (255, 0, 0), -1)  # Draw a blue circle at each point
                    elif type == 6: # man_utd
                        cv2.circle(img, (int(point[0]), int(point[1])), 3, (0, 0, 255), -1)  # Draw a red circle at each point
                    elif type == 0: # ball orange
                        cv2.circle(img, (int(point[0]), int(point[1])), 3, (0, 140, 255), -1)  # Draw a orange circle at each point
                    else: # anything else
                        cv2.circle(img, (int(point[0]), int(point[1])), 3, (0, 255, 0), -1)  # Draw a green circle at each point
                    
                    idx += 1
                
            if len(transformed_points) > 0:
                # graph.add_edges(4)
                # graph.visualize_graph()
                cv2.imshow('game items', img)

            # write graph and image to pkl file
            pickle.dump(graph, file)
            

    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()