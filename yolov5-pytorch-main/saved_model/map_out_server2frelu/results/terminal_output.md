```python
Load model.
saved_model\map_out_server2frelu\frelu\best_epoch_weights.pth model, and classes loaded.
Configurations:
----------------------------------------------------------------------
|                     keys |                                   values|
----------------------------------------------------------------------
|               model_path | saved_model\map_out_server2frelu\frelu\best_epoch_weights.pth|
|             classes_path |               model_data/voc_classes.txt|
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
100%|██████████| 2151/2151 [01:47<00:00, 19.97it/s]
  0%|          | 0/2151 [00:00<?, ?it/s]Get predict result done.
Get ground truth result.
100%|██████████| 2151/2151 [00:17<00:00, 119.84it/s]
Get ground truth result done.
Get map.
96.79% = aeroplane AP 	||	score_threhold=0.5 : F1=0.90 ; Recall=81.67% ; Precision=100.00%
93.93% = bicycle AP 	||	score_threhold=0.5 : F1=0.89 ; Recall=80.99% ; Precision=98.29%
91.90% = bird AP 	||	score_threhold=0.5 : F1=0.89 ; Recall=81.10% ; Precision=97.79%
86.55% = boat AP 	||	score_threhold=0.5 : F1=0.78 ; Recall=66.06% ; Precision=94.74%
76.52% = bottle AP 	||	score_threhold=0.5 : F1=0.71 ; Recall=60.91% ; Precision=85.35%
96.92% = bus AP 	||	score_threhold=0.5 : F1=0.90 ; Recall=86.29% ; Precision=93.86%
92.31% = car AP 	||	score_threhold=0.5 : F1=0.87 ; Recall=80.81% ; Precision=94.71%
91.37% = cat AP 	||	score_threhold=0.5 : F1=0.83 ; Recall=73.22% ; Precision=95.04%
77.43% = chair AP 	||	score_threhold=0.5 : F1=0.69 ; Recall=55.96% ; Precision=91.27%
91.02% = cow AP 	||	score_threhold=0.5 : F1=0.88 ; Recall=79.75% ; Precision=96.92%
67.20% = diningtable AP 	||	score_threhold=0.5 : F1=0.53 ; Recall=39.81% ; Precision=81.13%
92.36% = dog AP 	||	score_threhold=0.5 : F1=0.82 ; Recall=72.95% ; Precision=93.83%
97.16% = horse AP 	||	score_threhold=0.5 : F1=0.90 ; Recall=83.46% ; Precision=96.52%
89.42% = motorbike AP 	||	score_threhold=0.5 : F1=0.85 ; Recall=75.19% ; Precision=97.98%
91.85% = person AP 	||	score_threhold=0.5 : F1=0.84 ; Recall=75.01% ; Precision=96.08%
73.43% = pottedplant AP 	||	score_threhold=0.5 : F1=0.66 ; Recall=52.46% ; Precision=90.57%
93.95% = sheep AP 	||	score_threhold=0.5 : F1=0.88 ; Recall=80.33% ; Precision=96.71%
78.48% = sofa AP 	||	score_threhold=0.5 : F1=0.70 ; Recall=56.86% ; Precision=92.06%
92.33% = train AP 	||	score_threhold=0.5 : F1=0.86 ; Recall=76.03% ; Precision=97.87%
90.31% = tvmonitor AP 	||	score_threhold=0.5 : F1=0.85 ; Recall=79.70% ; Precision=91.38%
mAP = 88.06%
F1 = 81.13%
recall = 71.93%
precision = 94.11%
Get map done.
```

