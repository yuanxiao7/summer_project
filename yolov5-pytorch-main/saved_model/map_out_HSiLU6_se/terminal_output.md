best_epoch_weights.pth

```python
Get map.
94.29% = aeroplane AP 	||	score_threhold=0.4 : F1=0.90 ; Recall=82.50% ; Precision=98.02%
93.02% = bicycle AP 	||	score_threhold=0.4 : F1=0.87 ; Recall=78.17% ; Precision=99.11%
85.94% = bird AP 	||	score_threhold=0.4 : F1=0.80 ; Recall=70.73% ; Precision=92.06%
82.44% = boat AP 	||	score_threhold=0.4 : F1=0.72 ; Recall=59.63% ; Precision=91.55%
72.62% = bottle AP 	||	score_threhold=0.4 : F1=0.70 ; Recall=63.18% ; Precision=78.98%
93.84% = bus AP 	||	score_threhold=0.4 : F1=0.88 ; Recall=85.48% ; Precision=90.60%
90.62% = car AP 	||	score_threhold=0.4 : F1=0.86 ; Recall=81.04% ; Precision=91.35%
88.15% = cat AP 	||	score_threhold=0.4 : F1=0.80 ; Recall=69.40% ; Precision=95.49%
72.02% = chair AP 	||	score_threhold=0.4 : F1=0.67 ; Recall=55.72% ; Precision=85.13%
81.13% = cow AP 	||	score_threhold=0.4 : F1=0.81 ; Recall=73.42% ; Precision=90.62%
64.56% = diningtable AP 	||	score_threhold=0.4 : F1=0.55 ; Recall=40.74% ; Precision=86.27%
88.02% = dog AP 	||	score_threhold=0.4 : F1=0.77 ; Recall=66.10% ; Precision=92.34%
92.98% = horse AP 	||	score_threhold=0.4 : F1=0.87 ; Recall=82.71% ; Precision=90.91%
89.30% = motorbike AP 	||	score_threhold=0.4 : F1=0.84 ; Recall=75.97% ; Precision=93.33%
90.64% = person AP 	||	score_threhold=0.4 : F1=0.84 ; Recall=76.98% ; Precision=93.16%
64.03% = pottedplant AP 	||	score_threhold=0.4 : F1=0.62 ; Recall=53.01% ; Precision=74.62%
92.19% = sheep AP 	||	score_threhold=0.4 : F1=0.86 ; Recall=82.51% ; Precision=88.82%
72.57% = sofa AP 	||	score_threhold=0.4 : F1=0.66 ; Recall=52.94% ; Precision=88.52%
85.61% = train AP 	||	score_threhold=0.4 : F1=0.81 ; Recall=70.25% ; Precision=95.51%
90.24% = tvmonitor AP 	||	score_threhold=0.4 : F1=0.84 ; Recall=78.95% ; Precision=89.74%
mAP = 84.21%
F1 = 78.40%
recall = 69.97%
precision = 90.31%
Get map done.
```

last_epoch_weights.pth

```python
Load model.
saved_model\map_out_HSiLU6_SE\se_block/last_epoch_weights.pth model, and classes loaded.
  0%|          | 0/2151 [00:00<?, ?it/s]Configurations:
----------------------------------------------------------------------
|                     keys |                                   values|
----------------------------------------------------------------------
|               model_path | saved_model\map_out_HSiLU6_SE\se_block/last_epoch_weights.pth|
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
100%|██████████| 2151/2151 [01:24<00:00, 25.59it/s]
Get predict result done.
Get ground truth result.
100%|██████████| 2151/2151 [00:00<00:00, 3034.06it/s]
Get ground truth result done.
Get map.
94.27% = aeroplane AP 	||	score_threhold=0.4 : F1=0.87 ; Recall=80.83% ; Precision=95.10%
93.56% = bicycle AP 	||	score_threhold=0.4 : F1=0.87 ; Recall=78.87% ; Precision=96.55%
87.23% = bird AP 	||	score_threhold=0.4 : F1=0.82 ; Recall=75.61% ; Precision=89.86%
84.93% = boat AP 	||	score_threhold=0.4 : F1=0.75 ; Recall=64.22% ; Precision=90.91%
75.17% = bottle AP 	||	score_threhold=0.4 : F1=0.73 ; Recall=65.45% ; Precision=81.36%
95.03% = bus AP 	||	score_threhold=0.4 : F1=0.89 ; Recall=86.29% ; Precision=92.24%
91.54% = car AP 	||	score_threhold=0.4 : F1=0.87 ; Recall=82.17% ; Precision=92.15%
88.18% = cat AP 	||	score_threhold=0.4 : F1=0.83 ; Recall=72.68% ; Precision=95.68%
73.80% = chair AP 	||	score_threhold=0.4 : F1=0.70 ; Recall=58.64% ; Precision=86.69%
82.33% = cow AP 	||	score_threhold=0.4 : F1=0.80 ; Recall=72.15% ; Precision=90.48%
69.52% = diningtable AP 	||	score_threhold=0.4 : F1=0.62 ; Recall=47.22% ; Precision=91.07%
89.25% = dog AP 	||	score_threhold=0.4 : F1=0.80 ; Recall=70.21% ; Precision=93.18%
94.88% = horse AP 	||	score_threhold=0.4 : F1=0.87 ; Recall=82.71% ; Precision=91.67%
90.67% = motorbike AP 	||	score_threhold=0.4 : F1=0.86 ; Recall=78.29% ; Precision=94.39%
91.09% = person AP 	||	score_threhold=0.4 : F1=0.85 ; Recall=78.30% ; Precision=93.72%
65.16% = pottedplant AP 	||	score_threhold=0.4 : F1=0.61 ; Recall=54.10% ; Precision=71.22%
92.63% = sheep AP 	||	score_threhold=0.4 : F1=0.86 ; Recall=83.61% ; Precision=88.44%
74.97% = sofa AP 	||	score_threhold=0.4 : F1=0.72 ; Recall=58.82% ; Precision=92.31%
86.28% = train AP 	||	score_threhold=0.4 : F1=0.82 ; Recall=71.90% ; Precision=95.60%
91.69% = tvmonitor AP 	||	score_threhold=0.4 : F1=0.85 ; Recall=80.45% ; Precision=89.92%
mAP = 85.61%
F1 = 79.97%
recall = 72.13%
precision = 90.63%
Get map done.
```

