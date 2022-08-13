

```python
Configurations:
----------------------------------------------------------------------
|                     keys |                                   values|
----------------------------------------------------------------------
|               model_path | D:\shuqikaohe\weights/last_epoch_weights.pth|
|             classes_path |               model_data/voc_classes.txt|
|             anchors_path |              model_data/yolo_anchors.txt|
|             anchors_mask |        [[6, 7, 8], [3, 4, 5], [0, 1, 2]]|
|              input_shape |                               [640, 640]|
|                      pad |                                        2|
|                 backbone |                               cspdarknet|
|                      phi |                                        s|
|               confidence |                                    0.001|
|                  nms_iou |                                      0.5|
|          letterbox_image |                                     True|
|                     cuda |                                     True|
----------------------------------------------------------------------
Load model done.
Get predict result.
100%|██████████| 2151/2151 [01:39<00:00, 21.63it/s]
  0%|          | 0/2151 [00:00<?, ?it/s]Get predict result done.
Get ground truth result.
100%|██████████| 2151/2151 [00:07<00:00, 277.97it/s]
Get ground truth result done.
Get map.
97.16% = aeroplane AP 	||	score_threhold=0.4 : F1=0.94 ; Recall=90.00% ; Precision=99.08%
93.04% = bicycle AP 	||	score_threhold=0.4 : F1=0.90 ; Recall=85.21% ; Precision=94.53%
92.60% = bird AP 	||	score_threhold=0.4 : F1=0.89 ; Recall=84.15% ; Precision=94.52%
88.25% = boat AP 	||	score_threhold=0.4 : F1=0.84 ; Recall=78.90% ; Precision=89.58%
78.91% = bottle AP 	||	score_threhold=0.4 : F1=0.76 ; Recall=70.45% ; Precision=82.45%
98.55% = bus AP 	||	score_threhold=0.4 : F1=0.93 ; Recall=90.32% ; Precision=96.55%
92.96% = car AP 	||	score_threhold=0.4 : F1=0.88 ; Recall=83.52% ; Precision=92.50%
93.20% = cat AP 	||	score_threhold=0.4 : F1=0.89 ; Recall=84.70% ; Precision=94.51%
79.05% = chair AP 	||	score_threhold=0.4 : F1=0.74 ; Recall=65.45% ; Precision=85.13%
90.11% = cow AP 	||	score_threhold=0.4 : F1=0.87 ; Recall=83.54% ; Precision=90.41%
67.72% = diningtable AP 	||	score_threhold=0.4 : F1=0.64 ; Recall=52.78% ; Precision=80.28%
94.08% = dog AP 	||	score_threhold=0.4 : F1=0.90 ; Recall=85.62% ; Precision=93.98%
95.95% = horse AP 	||	score_threhold=0.4 : F1=0.93 ; Recall=91.73% ; Precision=93.85%
92.51% = motorbike AP 	||	score_threhold=0.4 : F1=0.86 ; Recall=81.40% ; Precision=92.11%
92.72% = person AP 	||	score_threhold=0.4 : F1=0.88 ; Recall=82.75% ; Precision=93.66%
75.67% = pottedplant AP 	||	score_threhold=0.4 : F1=0.73 ; Recall=65.57% ; Precision=81.08%
93.36% = sheep AP 	||	score_threhold=0.4 : F1=0.87 ; Recall=84.70% ; Precision=90.12%
82.75% = sofa AP 	||	score_threhold=0.4 : F1=0.71 ; Recall=61.76% ; Precision=84.00%
90.35% = train AP 	||	score_threhold=0.4 : F1=0.86 ; Recall=79.34% ; Precision=94.12%
93.13% = tvmonitor AP 	||	score_threhold=0.4 : F1=0.87 ; Recall=87.97% ; Precision=86.67%
mAP = 89.10%
F1 = 84.45%
recall = 79.49%
precision = 90.46%
Get map done.
```

