```python
Load model.
model_data/yolov5_s.pth model, and classes loaded.
  0%|          | 0/2151 [00:00<?, ?it/s]Configurations:
----------------------------------------------------------------------
|                     keys |                                   values|
----------------------------------------------------------------------
|               model_path |                  model_data/yolov5_s.pth|
|             classes_path |              model_data/coco_classes.txt|
|             anchors_path |              model_data/yolo_anchors.txt|
|             anchors_mask |        [[6, 7, 8], [3, 4, 5], [0, 1, 2]]|
|              input_shape |                               [640, 640]|
|                 backbone |                               cspdarknet|
|                      phi |                                        s|
|               confidence |                                    0.001|
|                  nms_iou |                                      0.5|
|          letterbox_image |                                     True|
|                     cuda |                                     True|
----------------------------------------------------------------------
Load model done.
Get predict result.
100%|██████████| 2151/2151 [01:24<00:00, 25.42it/s]
Get predict result done.
Get ground truth result.
100%|██████████| 2151/2151 [00:00<00:00, 3020.64it/s]
Get ground truth result done.
Get map.
90.62% = aeroplane AP 	||	score_threhold=0.3 : F1=0.88 ; Recall=85.00% ; Precision=91.07%
83.12% = bicycle AP 	||	score_threhold=0.3 : F1=0.77 ; Recall=73.94% ; Precision=80.15%
82.91% = bird AP 	||	score_threhold=0.3 : F1=0.80 ; Recall=78.05% ; Precision=82.58%
57.17% = boat AP 	||	score_threhold=0.3 : F1=0.56 ; Recall=54.13% ; Precision=59.00%
64.17% = bottle AP 	||	score_threhold=0.3 : F1=0.64 ; Recall=65.00% ; Precision=63.00%
89.39% = bus AP 	||	score_threhold=0.3 : F1=0.88 ; Recall=86.29% ; Precision=89.17%
81.62% = car AP 	||	score_threhold=0.3 : F1=0.77 ; Recall=79.68% ; Precision=74.32%
82.74% = cat AP 	||	score_threhold=0.3 : F1=0.78 ; Recall=73.22% ; Precision=83.75%
62.77% = chair AP 	||	score_threhold=0.3 : F1=0.57 ; Recall=63.50% ; Precision=51.38%
86.34% = cow AP 	||	score_threhold=0.3 : F1=0.80 ; Recall=87.34% ; Precision=74.19%
43.89% = diningtable AP 	||	score_threhold=0.3 : F1=0.51 ; Recall=45.37% ; Precision=58.33%
79.67% = dog AP 	||	score_threhold=0.3 : F1=0.76 ; Recall=68.49% ; Precision=84.75%
90.86% = horse AP 	||	score_threhold=0.3 : F1=0.86 ; Recall=89.47% ; Precision=82.64%
81.33% = motorbike AP 	||	score_threhold=0.3 : F1=0.80 ; Recall=81.40% ; Precision=77.78%
88.52% = person AP 	||	score_threhold=0.3 : F1=0.82 ; Recall=88.23% ; Precision=75.96%
51.75% = pottedplant AP 	||	score_threhold=0.3 : F1=0.53 ; Recall=55.74% ; Precision=50.50%
86.95% = sheep AP 	||	score_threhold=0.3 : F1=0.81 ; Recall=83.61% ; Precision=78.46%
69.15% = sofa AP 	||	score_threhold=0.3 : F1=0.64 ; Recall=66.67% ; Precision=60.71%
86.12% = train AP 	||	score_threhold=0.3 : F1=0.84 ; Recall=83.47% ; Precision=84.87%
82.59% = tvmonitor AP 	||	score_threhold=0.3 : F1=0.82 ; Recall=78.95% ; Precision=85.37%
mAP = 77.08%
F1 = 74.15%
recall = 74.38%
precision = 74.40%
Get map done.

```

