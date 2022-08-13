

```python
D:\shuqikaohe\weights/last_epoch_weights.pth model, and classes loaded.
  0%|          | 0/2151 [00:00<?, ?it/s]Configurations:
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
100%|██████████| 2151/2151 [01:29<00:00, 23.95it/s]
  0%|          | 0/2151 [00:00<?, ?it/s]Get predict result done.
Get ground truth result.
100%|██████████| 2151/2151 [00:07<00:00, 285.44it/s]
Get ground truth result done.
Get map.
97.16% = aeroplane AP 	||	score_threhold=0.5 : F1=0.92 ; Recall=85.83% ; Precision=100.00%
93.04% = bicycle AP 	||	score_threhold=0.5 : F1=0.89 ; Recall=82.39% ; Precision=96.69%
92.60% = bird AP 	||	score_threhold=0.5 : F1=0.87 ; Recall=79.27% ; Precision=95.59%
88.25% = boat AP 	||	score_threhold=0.5 : F1=0.80 ; Recall=69.72% ; Precision=95.00%
78.91% = bottle AP 	||	score_threhold=0.5 : F1=0.74 ; Recall=64.55% ; Precision=87.65%
98.55% = bus AP 	||	score_threhold=0.5 : F1=0.90 ; Recall=83.87% ; Precision=96.30%
92.96% = car AP 	||	score_threhold=0.5 : F1=0.87 ; Recall=80.81% ; Precision=94.21%
93.20% = cat AP 	||	score_threhold=0.5 : F1=0.86 ; Recall=78.69% ; Precision=94.74%
79.05% = chair AP 	||	score_threhold=0.5 : F1=0.72 ; Recall=60.83% ; Precision=89.61%
90.11% = cow AP 	||	score_threhold=0.5 : F1=0.86 ; Recall=78.48% ; Precision=93.94%
67.72% = diningtable AP 	||	score_threhold=0.5 : F1=0.59 ; Recall=45.37% ; Precision=85.96%
94.08% = dog AP 	||	score_threhold=0.5 : F1=0.86 ; Recall=78.42% ; Precision=96.22%
95.95% = horse AP 	||	score_threhold=0.5 : F1=0.91 ; Recall=87.22% ; Precision=95.87%
92.51% = motorbike AP 	||	score_threhold=0.5 : F1=0.85 ; Recall=75.97% ; Precision=96.08%
92.72% = person AP 	||	score_threhold=0.5 : F1=0.85 ; Recall=76.69% ; Precision=95.61%
75.67% = pottedplant AP 	||	score_threhold=0.5 : F1=0.69 ; Recall=57.38% ; Precision=87.50%
93.36% = sheep AP 	||	score_threhold=0.5 : F1=0.89 ; Recall=83.06% ; Precision=95.00%
82.75% = sofa AP 	||	score_threhold=0.5 : F1=0.72 ; Recall=60.78% ; Precision=88.57%
90.35% = train AP 	||	score_threhold=0.5 : F1=0.87 ; Recall=78.51% ; Precision=96.94%
93.13% = tvmonitor AP 	||	score_threhold=0.5 : F1=0.85 ; Recall=81.95% ; Precision=88.62%
mAP = 89.10%
F1 = 82.62%
recall = 74.49%
precision = 93.50%
```

