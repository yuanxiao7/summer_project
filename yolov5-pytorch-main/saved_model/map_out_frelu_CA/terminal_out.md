

score = 0.5

```python
Load model.
saved_model/1_2/best_epoch_weights.pth model, and classes loaded.
  0%|          | 0/2151 [00:00<?, ?it/s]Configurations:
----------------------------------------------------------------------
|                     keys |                                   values|
----------------------------------------------------------------------
|               model_path |   saved_model/1_2/best_epoch_weights.pth|
|             classes_path |               model_data/voc_classes.txt|
|             anchors_path |              model_data/yolo_anchors.txt|
|             anchors_mask |        [[6, 7, 8], [3, 4, 5], [0, 1, 2]]|
|              input_shape |                               [640, 640]|
|                      pad |                                        4|
|                 backbone |                               cspdarknet|
|                      phi |                                        s|
|               confidence |                                    0.001|
|                  nms_iou |                                      0.5|
|          letterbox_image |                                     True|
|                     cuda |                                     True|
----------------------------------------------------------------------
Load model done.
Get predict result.
100%|██████████| 2151/2151 [01:32<00:00, 23.30it/s]
  0%|          | 0/2151 [00:00<?, ?it/s]Get predict result done.
Get ground truth result.
100%|██████████| 2151/2151 [00:01<00:00, 1600.64it/s]
Get ground truth result done.
Get map.
95.69% = aeroplane AP 	||	score_threhold=0.5 : F1=0.90 ; Recall=81.67% ; Precision=100.00%
93.15% = bicycle AP 	||	score_threhold=0.5 : F1=0.87 ; Recall=78.87% ; Precision=97.39%
91.22% = bird AP 	||	score_threhold=0.5 : F1=0.86 ; Recall=76.83% ; Precision=97.67%
87.78% = boat AP 	||	score_threhold=0.5 : F1=0.79 ; Recall=66.06% ; Precision=98.63%
79.36% = bottle AP 	||	score_threhold=0.5 : F1=0.75 ; Recall=64.55% ; Precision=89.87%
95.90% = bus AP 	||	score_threhold=0.5 : F1=0.89 ; Recall=84.68% ; Precision=94.59%
92.21% = car AP 	||	score_threhold=0.5 : F1=0.88 ; Recall=80.81% ; Precision=97.02%
90.68% = cat AP 	||	score_threhold=0.5 : F1=0.84 ; Recall=76.50% ; Precision=93.33%
78.18% = chair AP 	||	score_threhold=0.5 : F1=0.71 ; Recall=58.15% ; Precision=91.57%
88.78% = cow AP 	||	score_threhold=0.5 : F1=0.85 ; Recall=74.68% ; Precision=98.33%
74.87% = diningtable AP 	||	score_threhold=0.5 : F1=0.61 ; Recall=44.44% ; Precision=96.00%
91.05% = dog AP 	||	score_threhold=0.5 : F1=0.82 ; Recall=73.29% ; Precision=94.27%
95.54% = horse AP 	||	score_threhold=0.5 : F1=0.89 ; Recall=83.46% ; Precision=95.69%
91.24% = motorbike AP 	||	score_threhold=0.5 : F1=0.84 ; Recall=75.19% ; Precision=96.04%
91.74% = person AP 	||	score_threhold=0.5 : F1=0.83 ; Recall=74.44% ; Precision=94.92%
73.54% = pottedplant AP 	||	score_threhold=0.5 : F1=0.66 ; Recall=53.01% ; Precision=88.18%
93.63% = sheep AP 	||	score_threhold=0.5 : F1=0.88 ; Recall=85.25% ; Precision=90.17%
77.76% = sofa AP 	||	score_threhold=0.5 : F1=0.69 ; Recall=55.88% ; Precision=89.06%
90.51% = train AP 	||	score_threhold=0.5 : F1=0.83 ; Recall=73.55% ; Precision=95.70%
92.87% = tvmonitor AP 	||	score_threhold=0.5 : F1=0.86 ; Recall=80.45% ; Precision=93.04%
mAP = 88.29%
F1 = 81.36%
recall = 72.09%
precision = 94.58%
Get map done.
```





score = 0.4

```python
saved_model\map_out_relu_ECA\ECA/best_epoch_weights.pth model, and classes loaded.
Configurations:
----------------------------------------------------------------------
|                     keys |                                   values|
----------------------------------------------------------------------
|               model_path | saved_model\map_out_frelu_ECA\ECA/best_epoch_weights.pth|
|             classes_path |               model_data/voc_classes.txt|
|             anchors_path |              model_data/yolo_anchors.txt|
|             anchors_mask |        [[6, 7, 8], [3, 4, 5], [0, 1, 2]]|
|              input_shape |                               [640, 640]|
|                      pad |                                        4|
|                 backbone |                               cspdarknet|
|                      phi |                                        s|
|               confidence |                                    0.001|
|                  nms_iou |                                      0.5|
|          letterbox_image |                                     True|
|                     cuda |                                     True|
----------------------------------------------------------------------
Load model done.
Get predict result.
100%|██████████| 2151/2151 [01:47<00:00, 19.93it/s]
  0%|          | 0/2151 [00:00<?, ?it/s]Get predict result done.
Get ground truth result.
100%|██████████| 2151/2151 [00:06<00:00, 328.36it/s]
Get ground truth result done.
Get map.
95.69% = aeroplane AP 	||	score_threhold=0.4 : F1=0.94 ; Recall=88.33% ; Precision=100.00%
93.15% = bicycle AP 	||	score_threhold=0.4 : F1=0.89 ; Recall=84.51% ; Precision=93.75%
91.22% = bird AP 	||	score_threhold=0.4 : F1=0.89 ; Recall=82.93% ; Precision=95.10%
87.78% = boat AP 	||	score_threhold=0.4 : F1=0.83 ; Recall=74.31% ; Precision=94.19%
79.36% = bottle AP 	||	score_threhold=0.4 : F1=0.78 ; Recall=71.36% ; Precision=86.26%
95.90% = bus AP 	||	score_threhold=0.4 : F1=0.91 ; Recall=90.32% ; Precision=91.80%
92.21% = car AP 	||	score_threhold=0.4 : F1=0.89 ; Recall=85.78% ; Precision=92.68%
90.68% = cat AP 	||	score_threhold=0.4 : F1=0.88 ; Recall=84.15% ; Precision=92.77%
78.18% = chair AP 	||	score_threhold=0.4 : F1=0.74 ; Recall=64.72% ; Precision=86.08%
88.78% = cow AP 	||	score_threhold=0.4 : F1=0.86 ; Recall=79.75% ; Precision=92.65%
74.87% = diningtable AP 	||	score_threhold=0.4 : F1=0.69 ; Recall=55.56% ; Precision=89.55%
91.05% = dog AP 	||	score_threhold=0.4 : F1=0.84 ; Recall=78.08% ; Precision=91.94%
95.54% = horse AP 	||	score_threhold=0.4 : F1=0.91 ; Recall=88.72% ; Precision=92.91%
91.24% = motorbike AP 	||	score_threhold=0.4 : F1=0.88 ; Recall=82.17% ; Precision=95.50%
91.74% = person AP 	||	score_threhold=0.4 : F1=0.87 ; Recall=82.00% ; Precision=92.69%
73.54% = pottedplant AP 	||	score_threhold=0.4 : F1=0.70 ; Recall=61.20% ; Precision=82.35%
93.63% = sheep AP 	||	score_threhold=0.4 : F1=0.87 ; Recall=87.43% ; Precision=86.96%
77.76% = sofa AP 	||	score_threhold=0.4 : F1=0.70 ; Recall=60.78% ; Precision=83.78%
90.51% = train AP 	||	score_threhold=0.4 : F1=0.86 ; Recall=79.34% ; Precision=93.20%
92.87% = tvmonitor AP 	||	score_threhold=0.4 : F1=0.88 ; Recall=86.47% ; Precision=90.55%
mAP = 88.29%
F1 = 84.08%
recall = 78.40%
precision = 91.24%
Get map done.

```

