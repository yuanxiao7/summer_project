



score = 0.5

```python
Load model.
server_weights/best_epoch_weights.pth model, and classes loaded.
  0%|          | 0/2151 [00:00<?, ?it/s]Configurations:
----------------------------------------------------------------------
|                     keys |                                   values|
----------------------------------------------------------------------
|               model_path |    server_weights/best_epoch_weights.pth|
|             classes_path |               model_data/voc_classes.txt|
|             anchors_path |              model_data/yolo_anchors.txt|
|             anchors_mask |        [[6, 7, 8], [3, 4, 5], [0, 1, 2]]|
|              input_shape |                               [640, 640]|
|                      pad |                                        3|
|                 backbone |                               cspdarknet|
|                      phi |                                        s|
|               confidence |                                    0.001|
|                  nms_iou |                                      0.5|
|          letterbox_image |                                     True|
|                     cuda |                                     True|
----------------------------------------------------------------------
Load model done.
Get predict result.
100%|██████████| 2151/2151 [01:30<00:00, 23.69it/s]
Get predict result done.
Get ground truth result.
100%|██████████| 2151/2151 [00:01<00:00, 1491.53it/s]
Get ground truth result done.
Get map.
95.27% = aeroplane AP 	||	score_threhold=0.5 : F1=0.89 ; Recall=81.67% ; Precision=98.00%
93.50% = bicycle AP 	||	score_threhold=0.5 : F1=0.88 ; Recall=79.58% ; Precision=98.26%
90.62% = bird AP 	||	score_threhold=0.5 : F1=0.86 ; Recall=78.05% ; Precision=96.97%
88.40% = boat AP 	||	score_threhold=0.5 : F1=0.80 ; Recall=66.97% ; Precision=98.65%
77.41% = bottle AP 	||	score_threhold=0.5 : F1=0.71 ; Recall=60.45% ; Precision=84.71%
95.79% = bus AP 	||	score_threhold=0.5 : F1=0.90 ; Recall=87.90% ; Precision=93.16%
91.88% = car AP 	||	score_threhold=0.5 : F1=0.87 ; Recall=81.26% ; Precision=94.74%
91.63% = cat AP 	||	score_threhold=0.5 : F1=0.84 ; Recall=74.32% ; Precision=95.77%
76.41% = chair AP 	||	score_threhold=0.5 : F1=0.69 ; Recall=56.69% ; Precision=88.59%
91.39% = cow AP 	||	score_threhold=0.5 : F1=0.86 ; Recall=75.95% ; Precision=100.00%
67.34% = diningtable AP 	||	score_threhold=0.5 : F1=0.56 ; Recall=40.74% ; Precision=89.80%
91.37% = dog AP 	||	score_threhold=0.5 : F1=0.83 ; Recall=74.32% ; Precision=93.13%
94.91% = horse AP 	||	score_threhold=0.5 : F1=0.90 ; Recall=84.96% ; Precision=95.76%
90.73% = motorbike AP 	||	score_threhold=0.5 : F1=0.86 ; Recall=78.29% ; Precision=95.28%
92.15% = person AP 	||	score_threhold=0.5 : F1=0.84 ; Recall=74.78% ; Precision=95.50%
71.73% = pottedplant AP 	||	score_threhold=0.5 : F1=0.62 ; Recall=48.63% ; Precision=83.96%
93.83% = sheep AP 	||	score_threhold=0.5 : F1=0.88 ; Recall=81.97% ; Precision=95.54%
76.80% = sofa AP 	||	score_threhold=0.5 : F1=0.64 ; Recall=51.96% ; Precision=82.81%
91.19% = train AP 	||	score_threhold=0.5 : F1=0.82 ; Recall=71.90% ; Precision=95.60%
90.52% = tvmonitor AP 	||	score_threhold=0.5 : F1=0.83 ; Recall=75.19% ; Precision=93.46%
mAP = 87.64%
F1 = 80.43%
recall = 71.28%
precision = 93.49%
Get map done.

```



score = 0.4

```python
Get map.
95.27% = aeroplane AP 	||	score_threhold=0.4 : F1=0.92 ; Recall=87.50% ; Precision=96.33%
93.50% = bicycle AP 	||	score_threhold=0.4 : F1=0.89 ; Recall=83.10% ; Precision=96.72%
90.62% = bird AP 	||	score_threhold=0.4 : F1=0.88 ; Recall=81.71% ; Precision=94.37%
88.40% = boat AP 	||	score_threhold=0.4 : F1=0.86 ; Recall=76.15% ; Precision=97.65%
77.41% = bottle AP 	||	score_threhold=0.4 : F1=0.73 ; Recall=66.82% ; Precision=81.67%
95.79% = bus AP 	||	score_threhold=0.4 : F1=0.91 ; Recall=89.52% ; Precision=92.50%
91.88% = car AP 	||	score_threhold=0.4 : F1=0.88 ; Recall=84.20% ; Precision=92.33%
91.63% = cat AP 	||	score_threhold=0.4 : F1=0.88 ; Recall=82.51% ; Precision=94.38%
76.41% = chair AP 	||	score_threhold=0.4 : F1=0.72 ; Recall=62.29% ; Precision=84.49%
91.39% = cow AP 	||	score_threhold=0.4 : F1=0.88 ; Recall=81.01% ; Precision=96.97%
67.34% = diningtable AP 	||	score_threhold=0.4 : F1=0.63 ; Recall=50.93% ; Precision=83.33%
91.37% = dog AP 	||	score_threhold=0.4 : F1=0.86 ; Recall=81.16% ; Precision=91.15%
94.91% = horse AP 	||	score_threhold=0.4 : F1=0.90 ; Recall=87.22% ; Precision=93.55%
90.73% = motorbike AP 	||	score_threhold=0.4 : F1=0.88 ; Recall=82.17% ; Precision=93.81%
92.15% = person AP 	||	score_threhold=0.4 : F1=0.86 ; Recall=81.19% ; Precision=92.50%
71.73% = pottedplant AP 	||	score_threhold=0.4 : F1=0.67 ; Recall=58.47% ; Precision=78.10%
93.83% = sheep AP 	||	score_threhold=0.4 : F1=0.89 ; Recall=86.89% ; Precision=91.38%
76.80% = sofa AP 	||	score_threhold=0.4 : F1=0.66 ; Recall=56.86% ; Precision=79.45%
91.19% = train AP 	||	score_threhold=0.4 : F1=0.87 ; Recall=80.17% ; Precision=96.04%
90.52% = tvmonitor AP 	||	score_threhold=0.4 : F1=0.86 ; Recall=79.70% ; Precision=92.98%
mAP = 87.64%
F1 = 83.19%
recall = 76.98%
precision = 90.98%
Get map done.

```

