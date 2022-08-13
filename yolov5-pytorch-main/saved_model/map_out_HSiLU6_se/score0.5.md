best_epoch_weights.pth

```python
saved_model\map_out_HSiLU6_SE\se_block/best_epoch_weights.pth model, and classes loaded.
  0%|          | 0/2151 [00:00<?, ?it/s]Configurations:
----------------------------------------------------------------------
|                     keys |                                   values|
----------------------------------------------------------------------
|               model_path | saved_model\map_out_HSiLU6_SE\se_block/best_epoch_weights.pth|
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
100%|██████████| 2151/2151 [01:29<00:00, 23.91it/s]
Get predict result done.
Get ground truth result.
100%|██████████| 2151/2151 [00:01<00:00, 1394.15it/s]
Get ground truth result done.
Get map.
94.29% = aeroplane AP 	||	score_threhold=0.5 : F1=0.81 ; Recall=69.17% ; Precision=98.81%
93.02% = bicycle AP 	||	score_threhold=0.5 : F1=0.84 ; Recall=73.24% ; Precision=99.05%
85.94% = bird AP 	||	score_threhold=0.5 : F1=0.78 ; Recall=65.24% ; Precision=95.54%
82.44% = boat AP 	||	score_threhold=0.5 : F1=0.67 ; Recall=50.46% ; Precision=98.21%
72.62% = bottle AP 	||	score_threhold=0.5 : F1=0.68 ; Recall=55.91% ; Precision=86.01%
93.84% = bus AP 	||	score_threhold=0.5 : F1=0.87 ; Recall=81.45% ; Precision=93.52%
90.62% = car AP 	||	score_threhold=0.5 : F1=0.85 ; Recall=77.20% ; Precision=94.21%
88.15% = cat AP 	||	score_threhold=0.5 : F1=0.71 ; Recall=56.28% ; Precision=97.17%
72.02% = chair AP 	||	score_threhold=0.5 : F1=0.63 ; Recall=48.91% ; Precision=88.94%
81.13% = cow AP 	||	score_threhold=0.5 : F1=0.81 ; Recall=69.62% ; Precision=96.49%
64.56% = diningtable AP 	||	score_threhold=0.5 : F1=0.45 ; Recall=29.63% ; Precision=94.12%
88.02% = dog AP 	||	score_threhold=0.5 : F1=0.72 ; Recall=57.53% ; Precision=94.92%
92.98% = horse AP 	||	score_threhold=0.5 : F1=0.80 ; Recall=69.92% ; Precision=93.00%
89.30% = motorbike AP 	||	score_threhold=0.5 : F1=0.79 ; Recall=66.67% ; Precision=95.56%
90.64% = person AP 	||	score_threhold=0.5 : F1=0.79 ; Recall=67.80% ; Precision=95.53%
64.03% = pottedplant AP 	||	score_threhold=0.5 : F1=0.57 ; Recall=44.26% ; Precision=80.20%
92.19% = sheep AP 	||	score_threhold=0.5 : F1=0.84 ; Recall=77.60% ; Precision=92.21%
72.57% = sofa AP 	||	score_threhold=0.5 : F1=0.62 ; Recall=47.06% ; Precision=92.31%
85.61% = train AP 	||	score_threhold=0.5 : F1=0.73 ; Recall=59.50% ; Precision=96.00%
90.24% = tvmonitor AP 	||	score_threhold=0.5 : F1=0.82 ; Recall=73.68% ; Precision=91.59%
mAP = 84.21%
F1 = 73.90%
recall = 62.06%
precision = 93.67%
Get map done.
```



last_epoch_weights.pth|

```python
Get map.
94.27% = aeroplane AP 	||	score_threhold=0.5 : F1=0.81 ; Recall=69.17% ; Precision=98.81%
93.56% = bicycle AP 	||	score_threhold=0.5 : F1=0.83 ; Recall=71.83% ; Precision=99.03%
87.23% = bird AP 	||	score_threhold=0.5 : F1=0.79 ; Recall=68.29% ; Precision=94.12%
84.93% = boat AP 	||	score_threhold=0.5 : F1=0.65 ; Recall=48.62% ; Precision=96.36%
75.17% = bottle AP 	||	score_threhold=0.5 : F1=0.71 ; Recall=60.45% ; Precision=84.71%
95.03% = bus AP 	||	score_threhold=0.5 : F1=0.87 ; Recall=81.45% ; Precision=94.39%
91.54% = car AP 	||	score_threhold=0.5 : F1=0.86 ; Recall=78.10% ; Precision=94.54%
88.18% = cat AP 	||	score_threhold=0.5 : F1=0.73 ; Recall=59.02% ; Precision=96.43%
73.80% = chair AP 	||	score_threhold=0.5 : F1=0.66 ; Recall=51.58% ; Precision=90.99%
82.33% = cow AP 	||	score_threhold=0.5 : F1=0.81 ; Recall=70.89% ; Precision=94.92%
69.52% = diningtable AP 	||	score_threhold=0.5 : F1=0.49 ; Recall=33.33% ; Precision=94.74%
89.25% = dog AP 	||	score_threhold=0.5 : F1=0.75 ; Recall=61.99% ; Precision=94.76%
94.88% = horse AP 	||	score_threhold=0.5 : F1=0.83 ; Recall=73.68% ; Precision=95.15%
90.67% = motorbike AP 	||	score_threhold=0.5 : F1=0.79 ; Recall=67.44% ; Precision=95.60%
91.09% = person AP 	||	score_threhold=0.5 : F1=0.80 ; Recall=69.42% ; Precision=95.63%
65.16% = pottedplant AP 	||	score_threhold=0.5 : F1=0.58 ; Recall=45.36% ; Precision=80.58%
92.63% = sheep AP 	||	score_threhold=0.5 : F1=0.85 ; Recall=79.78% ; Precision=91.25%
74.97% = sofa AP 	||	score_threhold=0.5 : F1=0.64 ; Recall=49.02% ; Precision=90.91%
86.28% = train AP 	||	score_threhold=0.5 : F1=0.74 ; Recall=60.33% ; Precision=96.05%
91.69% = tvmonitor AP 	||	score_threhold=0.5 : F1=0.82 ; Recall=74.44% ; Precision=91.67%
mAP = 85.61%
F1 = 75.11%
recall = 63.71%
precision = 93.53%
Get map done.

```

