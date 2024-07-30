game_object_classification_names = {
    0: 'ball',
    1: 'down',
    # 2: 'game-objects',
    2: 'left',
    3: 'left_goal',
    4: 'man_city',
    5: 'man_city_gk',
    6: 'man_utd',
    7: 'man_utd_gk',
    8: 'right',
    9: 'right_goal',
    10: 'tri',
    11: 'up',
    12: 'x',
}

# we may want to remap these if model treat numbers are continuous rather than discrete and independent

game_object_classification_ids = {name: id for id, name in game_object_classification_names.items()}

edge_classification_names = {
    0: "team",
    1: "opponent",
    2: "ball",
    3: "goal",
}

edge_classification_ids = {name: id for id, name in edge_classification_names.items()}
