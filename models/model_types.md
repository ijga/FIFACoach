- yolo10b_1_coop.pt ->
  from fifacoach/co-op-cam-settings/9,
  4x6 tiling,
  5040 training images(),
  blur and noise augmentations,
  yolov10_balanced
  imgsz 640,
  100 epochs,
  batch 32,
  maybe its a yolov10x?

- yolo10b_2_coop.pt ->
  from fifacoach/co-op-cam-settings/7,
  2x3 tiling,
  1260 training images(),
  blur and noise augmentations,
  yolov10_balanced
  imgsz 640,
  100 epochs,
  batch -1 (60% CPU util),
  <!-- maybe its a yolov10x? -->

- best7_coop.pt ->
  from fifacoach/co-op-cam-settings/7,
  2x3 tiling,
  1260 training images(),
  blur and noise augmentations,
  yolov8 not sure which size,
  imgsz 640,
  not sure how many epochs,
  batch not sure,
