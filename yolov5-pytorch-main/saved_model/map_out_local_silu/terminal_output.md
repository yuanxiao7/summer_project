```
Load model.
weights/best_epoch_weights.pth model, and classes loaded.
Configurations:
----------------------------------------------------------------------
|                     keys |                                   values|
----------------------------------------------------------------------
|               model_path |           weights/best_epoch_weights.pth|
|             classes_path |               model_data/voc_classes.txt|
|             anchors_path |              model_data/yolo_anchors.txt|
|             anchors_mask |        [[6, 7, 8], [3, 4, 5], [0, 1, 2]]|
|              input_shape |                               [640, 640]|
|                 backbone |                               cspdarknet|
|                      phi |                                        s|
|               confidence |                                      0.5|
|                  nms_iou |                                      0.4|
|          letterbox_image |                                     True|
|                     cuda |                                     True|
----------------------------------------------------------------------
Load model done.
Get predict result.
100%|██████████| 2151/2151 [01:25<00:00, 25.30it/s]
Get predict result done.
Get ground truth result.
100%|██████████| 2151/2151 [00:05<00:00, 407.66it/s]
Get ground truth result done.
Get map.
86.94% = aeroplane AP 	||	score_threhold=0.5 : F1=0.77 ; Recall=64.17% ; Precision=97.47%
83.85% = bicycle AP 	||	score_threhold=0.5 : F1=0.77 ; Recall=63.38% ; Precision=97.83%
72.32% = bird AP 	||	score_threhold=0.5 : F1=0.68 ; Recall=54.27% ; Precision=91.75%
61.73% = boat AP 	||	score_threhold=0.5 : F1=0.43 ; Recall=28.44% ; Precision=91.18%
56.19% = bottle AP 	||	score_threhold=0.5 : F1=0.56 ; Recall=42.27% ; Precision=84.55%
85.08% = bus AP 	||	score_threhold=0.5 : F1=0.81 ; Recall=72.58% ; Precision=90.91%
84.12% = car AP 	||	score_threhold=0.5 : F1=0.79 ; Recall=69.07% ; Precision=93.29%
76.72% = cat AP 	||	score_threhold=0.5 : F1=0.61 ; Recall=45.36% ; Precision=91.21%
54.95% = chair AP 	||	score_threhold=0.5 : F1=0.47 ; Recall=33.09% ; Precision=83.44%
66.03% = cow AP 	||	score_threhold=0.5 : F1=0.59 ; Recall=45.57% ; Precision=83.72%
51.93% = diningtable AP 	||	score_threhold=0.5 : F1=0.31 ; Recall=18.52% ; Precision=86.96%
71.24% = dog AP 	||	score_threhold=0.5 : F1=0.52 ; Recall=37.33% ; Precision=84.50%
75.81% = horse AP 	||	score_threhold=0.5 : F1=0.65 ; Recall=53.38% ; Precision=81.61%
74.31% = motorbike AP 	||	score_threhold=0.5 : F1=0.65 ; Recall=50.39% ; Precision=91.55%
85.50% = person AP 	||	score_threhold=0.5 : F1=0.73 ; Recall=59.61% ; Precision=92.73%
50.44% = pottedplant AP 	||	score_threhold=0.5 : F1=0.44 ; Recall=30.60% ; Precision=80.00%
78.27% = sheep AP 	||	score_threhold=0.5 : F1=0.76 ; Recall=66.67% ; Precision=89.05%
60.15% = sofa AP 	||	score_threhold=0.5 : F1=0.51 ; Recall=36.27% ; Precision=86.05%
72.57% = train AP 	||	score_threhold=0.5 : F1=0.64 ; Recall=48.76% ; Precision=92.19%
80.29% = tvmonitor AP 	||	score_threhold=0.5 : F1=0.71 ; Recall=57.89% ; Precision=92.77%
mAP = 71.42%
Get map done.
```

