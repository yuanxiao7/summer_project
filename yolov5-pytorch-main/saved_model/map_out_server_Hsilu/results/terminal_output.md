```python
Load model.
server_weights/hsilu/best_epoch_weights.pth model, and classes loaded.
  0%|          | 0/2151 [00:00<?, ?it/s]Configurations:
----------------------------------------------------------------------
|                     keys |                                   values|
----------------------------------------------------------------------
|               model_path | server_weights/hsilu/best_epoch_weights.pth|
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
100%|██████████| 2151/2151 [01:18<00:00, 27.56it/s]
Get predict result done.
Get ground truth result.
100%|██████████| 2151/2151 [00:00<00:00, 3257.56it/s]
Get ground truth result done.
Get map.
94.00% = aeroplane AP 	||	score_threhold=0.5 : F1=0.53 ; Recall=35.83% ; Precision=100.00%
90.64% = bicycle AP 	||	score_threhold=0.5 : F1=0.70 ; Recall=54.23% ; Precision=98.72%
85.42% = bird AP 	||	score_threhold=0.5 : F1=0.65 ; Recall=48.17% ; Precision=98.75%
78.86% = boat AP 	||	score_threhold=0.5 : F1=0.34 ; Recall=20.18% ; Precision=100.00%
73.39% = bottle AP 	||	score_threhold=0.5 : F1=0.49 ; Recall=33.18% ; Precision=96.05%
94.15% = bus AP 	||	score_threhold=0.5 : F1=0.76 ; Recall=62.10% ; Precision=98.72%
89.87% = car AP 	||	score_threhold=0.5 : F1=0.77 ; Recall=63.21% ; Precision=97.56%
86.22% = cat AP 	||	score_threhold=0.5 : F1=0.38 ; Recall=24.04% ; Precision=93.62%
71.44% = chair AP 	||	score_threhold=0.5 : F1=0.44 ; Recall=28.22% ; Precision=95.87%
89.06% = cow AP 	||	score_threhold=0.5 : F1=0.70 ; Recall=54.43% ; Precision=100.00%
65.48% = diningtable AP 	||	score_threhold=0.5 : F1=0.07 ; Recall=3.70% ; Precision=100.00%
86.56% = dog AP 	||	score_threhold=0.5 : F1=0.51 ; Recall=34.93% ; Precision=96.23%
90.29% = horse AP 	||	score_threhold=0.5 : F1=0.64 ; Recall=47.37% ; Precision=96.92%
90.26% = motorbike AP 	||	score_threhold=0.5 : F1=0.53 ; Recall=35.66% ; Precision=100.00%
89.79% = person AP 	||	score_threhold=0.5 : F1=0.63 ; Recall=46.51% ; Precision=97.70%
62.98% = pottedplant AP 	||	score_threhold=0.5 : F1=0.34 ; Recall=21.31% ; Precision=88.64%
91.23% = sheep AP 	||	score_threhold=0.5 : F1=0.76 ; Recall=60.66% ; Precision=100.00%
72.24% = sofa AP 	||	score_threhold=0.5 : F1=0.37 ; Recall=22.55% ; Precision=100.00%
85.28% = train AP 	||	score_threhold=0.5 : F1=0.44 ; Recall=28.93% ; Precision=94.59%
88.89% = tvmonitor AP 	||	score_threhold=0.5 : F1=0.72 ; Recall=57.89% ; Precision=95.06%
mAP = 83.80%
F1 = 53.82%
recall = 39.16%
precison = 97.42%
Get map done.

```

