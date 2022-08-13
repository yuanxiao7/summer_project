



```python
Load model.
server_weights/last_epoch_weights.pth model, and classes loaded.
Configurations:
----------------------------------------------------------------------
|                     keys |                                   values|
----------------------------------------------------------------------
|               model_path |    server_weights/last_epoch_weights.pth|
|             classes_path |               model_data/voc_classes.txt|
|             anchors_path |              model_data/yolo_anchors.txt|
|             anchors_mask |        [[6, 7, 8], [3, 4, 5], [0, 1, 2]]|
|              input_shape |                               [640, 640]|
|                      pad |                                        1|
|                 backbone |                               cspdarknet|
|                      phi |                                        s|
|               confidence |                                    0.001|
|                  nms_iou |                                      0.5|
|          letterbox_image |                                     True|
|                     cuda |                                     True|
----------------------------------------------------------------------
Load model done.
Get predict result.
100%|██████████| 2151/2151 [01:42<00:00, 20.95it/s]
Get predict result done.
Get ground truth result.
100%|██████████| 2151/2151 [00:16<00:00, 130.15it/s]
Get ground truth result done.
Get map.
96.26% = aeroplane AP 	||	score_threhold=0.5 : F1=0.87 ; Recall=79.17% ; Precision=96.94%
92.77% = bicycle AP 	||	score_threhold=0.5 : F1=0.89 ; Recall=83.10% ; Precision=95.16%
91.26% = bird AP 	||	score_threhold=0.5 : F1=0.87 ; Recall=79.27% ; Precision=97.01%
88.99% = boat AP 	||	score_threhold=0.5 : F1=0.82 ; Recall=71.56% ; Precision=96.30%
79.94% = bottle AP 	||	score_threhold=0.5 : F1=0.74 ; Recall=64.55% ; Precision=86.59%
97.38% = bus AP 	||	score_threhold=0.5 : F1=0.93 ; Recall=90.32% ; Precision=96.55%
93.44% = car AP 	||	score_threhold=0.5 : F1=0.88 ; Recall=81.04% ; Precision=95.99%
92.91% = cat AP 	||	score_threhold=0.5 : F1=0.87 ; Recall=78.69% ; Precision=96.64%
78.23% = chair AP 	||	score_threhold=0.5 : F1=0.70 ; Recall=57.91% ; Precision=88.81%
91.10% = cow AP 	||	score_threhold=0.5 : F1=0.84 ; Recall=75.95% ; Precision=93.75%
64.86% = diningtable AP 	||	score_threhold=0.5 : F1=0.54 ; Recall=39.81% ; Precision=86.00%
94.13% = dog AP 	||	score_threhold=0.5 : F1=0.86 ; Recall=78.08% ; Precision=96.20%
96.55% = horse AP 	||	score_threhold=0.5 : F1=0.91 ; Recall=86.47% ; Precision=96.64%
92.72% = motorbike AP 	||	score_threhold=0.5 : F1=0.88 ; Recall=80.62% ; Precision=97.20%
92.10% = person AP 	||	score_threhold=0.5 : F1=0.84 ; Recall=75.13% ; Precision=95.52%
71.56% = pottedplant AP 	||	score_threhold=0.5 : F1=0.64 ; Recall=52.46% ; Precision=82.76%
93.48% = sheep AP 	||	score_threhold=0.5 : F1=0.88 ; Recall=81.97% ; Precision=94.94%
80.02% = sofa AP 	||	score_threhold=0.5 : F1=0.68 ; Recall=54.90% ; Precision=88.89%
90.00% = train AP 	||	score_threhold=0.5 : F1=0.87 ; Recall=79.34% ; Precision=96.97%
93.63% = tvmonitor AP 	||	score_threhold=0.5 : F1=0.89 ; Recall=84.21% ; Precision=94.12%
mAP = 88.57%
F1 = 82.08%
recall = 73.73%
precision = 93.65%
Get map done.

```





```python
Get map.
96.26% = aeroplane AP 	||	score_threhold=0.4 : F1=0.91 ; Recall=86.67% ; Precision=95.41%
92.77% = bicycle AP 	||	score_threhold=0.4 : F1=0.88 ; Recall=85.92% ; Precision=91.04%
91.26% = bird AP 	||	score_threhold=0.4 : F1=0.89 ; Recall=85.37% ; Precision=93.96%
88.99% = boat AP 	||	score_threhold=0.4 : F1=0.83 ; Recall=77.98% ; Precision=88.54%
79.94% = bottle AP 	||	score_threhold=0.4 : F1=0.76 ; Recall=70.00% ; Precision=82.35%
97.38% = bus AP 	||	score_threhold=0.4 : F1=0.94 ; Recall=91.94% ; Precision=96.61%
93.44% = car AP 	||	score_threhold=0.4 : F1=0.89 ; Recall=85.10% ; Precision=93.32%
92.91% = cat AP 	||	score_threhold=0.4 : F1=0.89 ; Recall=83.61% ; Precision=95.62%
78.23% = chair AP 	||	score_threhold=0.4 : F1=0.75 ; Recall=66.42% ; Precision=85.31%
91.10% = cow AP 	||	score_threhold=0.4 : F1=0.90 ; Recall=87.34% ; Precision=93.24%
64.86% = diningtable AP 	||	score_threhold=0.4 : F1=0.60 ; Recall=49.07% ; Precision=77.94%
94.13% = dog AP 	||	score_threhold=0.4 : F1=0.90 ; Recall=85.96% ; Precision=94.72%
96.55% = horse AP 	||	score_threhold=0.4 : F1=0.91 ; Recall=88.72% ; Precision=93.65%
92.72% = motorbike AP 	||	score_threhold=0.4 : F1=0.90 ; Recall=82.95% ; Precision=97.27%
92.10% = person AP 	||	score_threhold=0.4 : F1=0.87 ; Recall=81.88% ; Precision=92.20%
71.56% = pottedplant AP 	||	score_threhold=0.4 : F1=0.68 ; Recall=62.30% ; Precision=74.51%
93.48% = sheep AP 	||	score_threhold=0.4 : F1=0.89 ; Recall=86.89% ; Precision=91.38%
80.02% = sofa AP 	||	score_threhold=0.4 : F1=0.72 ; Recall=62.75% ; Precision=84.21%
90.00% = train AP 	||	score_threhold=0.4 : F1=0.88 ; Recall=83.47% ; Precision=93.52%
93.63% = tvmonitor AP 	||	score_threhold=0.4 : F1=0.89 ; Recall=86.47% ; Precision=91.27%
mAP = 88.57%
F1 = 84.41%
recall = 79.54%
precision = 90.30%
Get map done.
```

