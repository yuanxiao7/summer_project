

```python
Load model.
server_weights/baseline/best_epoch_weights.pth model, and classes loaded.
  0%|          | 0/2151 [00:00<?, ?it/s]Configurations:
----------------------------------------------------------------------
|                     keys |                                   values|
----------------------------------------------------------------------
|               model_path | server_weights/baseline/best_epoch_weights.pth|
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
100%|██████████| 2151/2151 [01:24<00:00, 25.41it/s]
  0%|          | 0/2151 [00:00<?, ?it/s]Get predict result done.
Get ground truth result.
100%|██████████| 2151/2151 [00:05<00:00, 367.26it/s]
Get ground truth result done.
Get map.
94.93% = aeroplane AP 	||	score_threhold=0.3 : F1=0.91 ; Recall=87.50% ; Precision=94.59%
89.48% = bicycle AP 	||	score_threhold=0.3 : F1=0.83 ; Recall=80.28% ; Precision=86.36%
83.72% = bird AP 	||	score_threhold=0.3 : F1=0.79 ; Recall=75.00% ; Precision=84.25%
81.88% = boat AP 	||	score_threhold=0.3 : F1=0.78 ; Recall=70.64% ; Precision=86.52%
74.46% = bottle AP 	||	score_threhold=0.3 : F1=0.71 ; Recall=67.73% ; Precision=74.13%
93.94% = bus AP 	||	score_threhold=0.3 : F1=0.87 ; Recall=86.29% ; Precision=88.43%
90.63% = car AP 	||	score_threhold=0.3 : F1=0.85 ; Recall=83.07% ; Precision=87.20%
84.44% = cat AP 	||	score_threhold=0.3 : F1=0.85 ; Recall=79.23% ; Precision=90.62%
70.91% = chair AP 	||	score_threhold=0.3 : F1=0.67 ; Recall=59.85% ; Precision=76.16%
80.03% = cow AP 	||	score_threhold=0.3 : F1=0.75 ; Recall=70.89% ; Precision=80.00%
63.50% = diningtable AP 	||	score_threhold=0.3 : F1=0.62 ; Recall=50.93% ; Precision=79.71%
85.98% = dog AP 	||	score_threhold=0.3 : F1=0.80 ; Recall=73.97% ; Precision=87.10%
89.86% = horse AP 	||	score_threhold=0.3 : F1=0.88 ; Recall=86.47% ; Precision=89.84%
89.36% = motorbike AP 	||	score_threhold=0.3 : F1=0.85 ; Recall=79.84% ; Precision=91.15%
90.91% = person AP 	||	score_threhold=0.3 : F1=0.86 ; Recall=83.09% ; Precision=90.06%
66.45% = pottedplant AP 	||	score_threhold=0.3 : F1=0.65 ; Recall=61.75% ; Precision=68.48%
90.23% = sheep AP 	||	score_threhold=0.3 : F1=0.85 ; Recall=83.06% ; Precision=86.86%
70.62% = sofa AP 	||	score_threhold=0.3 : F1=0.65 ; Recall=54.90% ; Precision=81.16%
81.05% = train AP 	||	score_threhold=0.3 : F1=0.82 ; Recall=75.21% ; Precision=90.10%
89.56% = tvmonitor AP 	||	score_threhold=0.3 : F1=0.82 ; Recall=79.70% ; Precision=84.80%
mAP = 83.10%
F1 = 79.13%
recall = 74.47%
precision = 84.88%
Get map done.

```

