<!--
{"title": "You Only Look Once: Unified, Real-Time Object Detection", "url": "https://arxiv.org/abs/1506.02640", "topics": "2d-object-detection", "date": "2020-01-20", "estimated_minutes": "180"}
-->
### You Only Look Once: Unified, Real-Time Object Detection

Read on: 2020-01-20  
Time spent: *180* minutes  
Link to pdf: https://arxiv.org/abs/1506.02640  
Topic(s): `2d-object-detection`

citation:
```

```

### Abstract

__*What questions are the authors addressing?*__

Can 2d object detection in neural network be performed in a single convolutional neural network, foregoing framing it as object classification?

__*What is the major finding or scientific contribution?*__

Propose a novel framework for object detection which has fewer components, is (a lot) faster but performs worse.

__*What is the work's significance?*__

Important for real-time object detection

### Materials and Methods

__*What is their experimental methodology or developed system?*__

A single convolutional network which outputs a 7x7x(B*5 + C) tensor.

Each image input image is rescaled to 448x448x3. The image is put on a 7x7 grid.
For each grid cell, B bounding boxes are computed as well as one of C class labels.

A bounding box B consist out of (x, y, w, h, confidence), hence B*5 in the tensor.

convolutional layers pretrained on ImageNet.

Loss function assign a bounding box to each grid, and only to one of the B predictors. Loss function is weighted so that predicting no bounding box is not dominating the loss signal.

__*If there are alternative approaches, how did they select this system?*__

The alternative methods use region proposal algorithms, which are a lot slower.

### Experiments

__*Which dataset(s) were used?*__

Pascal VOC 2006, Pascal VOC 2012

__*What experiments were conducted*__

Accuracy + Speed comparison on Pascal VOC 2007

Type of error in VOC 2007 compared to fast R-CNN

Accuracy on Pascal VOC 2007

### Results

__*What are the conclusions they draw from the experiments?*__

Yolo is fast but does not have good accuracy in comparison

Yolo makes a lot of errors with small objects but not with false-posities/background. It can therefore be used to increase accuracy of faster RCNN

Yolo generalizes outside of the training data


__*How do these results answer the greater question identified in the abstract?*__

Yes

__*Do the results lead to the final claims of the paper?*__

Yes

### Figures, Tables, and Data

__*Can you identify the results in the images/charts/graphs?*__

Yes

__*What are the controls in the experiments and have they presented them properly?*__

They have presented/compared to a wide variety of different network architecture/proposals. They have not performed any ablation.

### Conclusions/Discussion

__*What do the results mean?*__

Real-time performance and accuracy are a trade off

__*Can you think of other interpretations of their results?*__

A smaller network with less modeling power is not as accurate but quicker

### Additional notes or thoughts

#### Future reading

R-CNN, Fast R-CNN, Faster R-CNN, Overfeat, DPM, Deep Multibox
