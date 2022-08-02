```python
Load model.
saved_model/last_epoch_weights.pth model, and classes loaded.
Configurations:
----------------------------------------------------------------------
|                     keys |                                   values|
----------------------------------------------------------------------
|               model_path |       saved_model/last_epoch_weights.pth|
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
100%|██████████| 2151/2151 [01:21<00:00, 26.36it/s]
Get predict result done.
Get ground truth result.
100%|██████████| 2151/2151 [00:01<00:00, 1107.01it/s]
Get ground truth result done.
Get map.
94.91% = aeroplane AP 	||	score_threhold=0.5 : F1=0.59 ; Recall=41.67% ; Precision=100.00%
91.50% = bicycle AP 	||	score_threhold=0.5 : F1=0.73 ; Recall=57.75% ; Precision=98.80%
86.02% = bird AP 	||	score_threhold=0.5 : F1=0.68 ; Recall=51.83% ; Precision=98.84%
82.35% = boat AP 	||	score_threhold=0.5 : F1=0.37 ; Recall=22.94% ; Precision=100.00%
73.14% = bottle AP 	||	score_threhold=0.5 : F1=0.59 ; Recall=42.73% ; Precision=95.92%
93.51% = bus AP 	||	score_threhold=0.5 : F1=0.79 ; Recall=66.13% ; Precision=98.80%
90.62% = car AP 	||	score_threhold=0.5 : F1=0.77 ; Recall=62.98% ; Precision=99.29%
86.56% = cat AP 	||	score_threhold=0.5 : F1=0.42 ; Recall=26.78% ; Precision=96.08%
72.39% = chair AP 	||	score_threhold=0.5 : F1=0.49 ; Recall=32.85% ; Precision=96.43%
86.16% = cow AP 	||	score_threhold=0.5 : F1=0.68 ; Recall=51.90% ; Precision=100.00%
67.90% = diningtable AP 	||	score_threhold=0.5 : F1=0.12 ; Recall=6.48% ; Precision=100.00%
87.66% = dog AP 	||	score_threhold=0.5 : F1=0.56 ; Recall=39.38% ; Precision=95.83%
91.04% = horse AP 	||	score_threhold=0.5 : F1=0.70 ; Recall=54.14% ; Precision=98.63%
90.46% = motorbike AP 	||	score_threhold=0.5 : F1=0.57 ; Recall=40.31% ; Precision=98.11%
90.33% = person AP 	||	score_threhold=0.5 : F1=0.65 ; Recall=49.34% ; Precision=97.16%
63.18% = pottedplant AP 	||	score_threhold=0.5 : F1=0.38 ; Recall=24.04% ; Precision=89.80%
91.97% = sheep AP 	||	score_threhold=0.5 : F1=0.78 ; Recall=64.48% ; Precision=100.00%
71.83% = sofa AP 	||	score_threhold=0.5 : F1=0.45 ; Recall=29.41% ; Precision=96.77%
85.63% = train AP 	||	score_threhold=0.5 : F1=0.50 ; Recall=33.88% ; Precision=95.35%
89.76% = tvmonitor AP 	||	score_threhold=0.5 : F1=0.73 ; Recall=60.15% ; Precision=94.12%
mAP = 84.35%
F1 = 57.85%
recall = 42.96%
precision = 97.50%
Get map done.
```

