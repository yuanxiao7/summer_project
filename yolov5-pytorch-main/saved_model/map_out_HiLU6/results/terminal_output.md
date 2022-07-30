```python
Load model.
saved_model/best_epoch_weights.pth model, and classes loaded.
Configurations:
----------------------------------------------------------------------
|                     keys |                                   values|
----------------------------------------------------------------------
|               model_path |       saved_model/best_epoch_weights.pth|
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
100%|██████████| 2151/2151 [01:22<00:00, 26.00it/s]
  0%|          | 0/2151 [00:00<?, ?it/s]Get predict result done.
Get ground truth result.
100%|██████████| 2151/2151 [00:01<00:00, 1829.37it/s]
Get ground truth result done.
Get map.
94.16% = aeroplane AP 	||	score_threhold=0.5 : F1=0.60 ; Recall=43.33% ; Precision=100.00%
91.83% = bicycle AP 	||	score_threhold=0.5 : F1=0.67 ; Recall=50.70% ; Precision=98.63%
84.22% = bird AP 	||	score_threhold=0.5 : F1=0.61 ; Recall=44.51% ; Precision=98.65%
77.49% = boat AP 	||	score_threhold=0.5 : F1=0.27 ; Recall=15.60% ; Precision=100.00%
74.14% = bottle AP 	||	score_threhold=0.5 : F1=0.50 ; Recall=33.64% ; Precision=98.67%
91.15% = bus AP 	||	score_threhold=0.5 : F1=0.75 ; Recall=61.29% ; Precision=96.20%
89.73% = car AP 	||	score_threhold=0.5 : F1=0.75 ; Recall=60.27% ; Precision=98.16%
85.04% = cat AP 	||	score_threhold=0.5 : F1=0.35 ; Recall=21.86% ; Precision=93.02%
71.74% = chair AP 	||	score_threhold=0.5 : F1=0.43 ; Recall=27.74% ; Precision=96.61%
86.74% = cow AP 	||	score_threhold=0.5 : F1=0.69 ; Recall=53.16% ; Precision=100.00%
64.75% = diningtable AP 	||	score_threhold=0.5 : F1=0.11 ; Recall=5.56% ; Precision=100.00%
86.29% = dog AP 	||	score_threhold=0.5 : F1=0.49 ; Recall=33.22% ; Precision=97.00%
92.20% = horse AP 	||	score_threhold=0.5 : F1=0.62 ; Recall=45.11% ; Precision=96.77%
89.06% = motorbike AP 	||	score_threhold=0.5 : F1=0.54 ; Recall=37.21% ; Precision=100.00%
90.16% = person AP 	||	score_threhold=0.5 : F1=0.63 ; Recall=46.22% ; Precision=98.04%
65.16% = pottedplant AP 	||	score_threhold=0.5 : F1=0.34 ; Recall=20.77% ; Precision=95.00%
90.85% = sheep AP 	||	score_threhold=0.5 : F1=0.75 ; Recall=60.66% ; Precision=99.11%
70.02% = sofa AP 	||	score_threhold=0.5 : F1=0.38 ; Recall=23.53% ; Precision=100.00%
84.44% = train AP 	||	score_threhold=0.5 : F1=0.46 ; Recall=30.58% ; Precision=94.87%
88.86% = tvmonitor AP 	||	score_threhold=0.5 : F1=0.74 ; Recall=59.40% ; Precision=98.75%
mAP = 83.40%
F1 = 53.49%
recall = 38.72%
precision = 97.97%
Get map done.

```

