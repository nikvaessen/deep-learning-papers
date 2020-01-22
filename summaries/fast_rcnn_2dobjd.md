<!--
{"title": "Fast R-CNN", "url": "https://arxiv.org/abs/1504.08083", "topics": "2d-object-detection", "date": "2020-01-22", "estimated_minutes": "180"}
-->
### Fast R-CNN

Read on: 2020-01-22  
Time spent: *180* minutes  
Link to pdf: https://arxiv.org/abs/1504.08083  
Topic(s): `2d-object-detection`

citation:
```
@inproceedings{Girshick2015,
archivePrefix = {arXiv},
arxivId = {1504.08083},
author = {Girshick, Ross},
booktitle = {Proceedings of the IEEE International Conference on Computer Vision},
doi = {10.1109/ICCV.2015.169},
eprint = {1504.08083},
isbn = {9781467383912},
issn = {15505499},
mendeley-groups = {2d obj det},
pages = {1440--1448},
title = {{Fast R-CNN}},
url = {https://github.com/rbgirshick/ https://arxiv.org/abs/1504.08083},
volume = {2015 Inter},
year = {2015}
}
```

### Abstract

__*What questions are the authors addressing?*__

Can the framework described in the R-CNN paper be improved both speed and accuracy wise?

__*What is the major finding or scientific contribution?*__

improve the speed of R-CNN by a factor of 213 while also improving mAP.

__*What is the work's significance?*__

Improve the region-proposal based framework of 2d object detection

### Materials and Methods

__*What is their experimental methodology or developed system?*__

Input to the network: image + a set of region proposals

Image is encoded into a feature map by conv network (AlexNet, vgg16)  
The region proposals locations can be translated on the downscaled feature map  
For each region proposal in the set, the region is max-pooled into a static size (7x7) feature vector by the RoI pooling layer
The feature vector is put through 2 fc layers, and then branched to 2 other fc layers, where one of them does object classification and the other bounding box regression fine-tuning

The conv network is pre-trained on imagenet and then fine-tuned on the training data. For training, a batch size of 128 is used. Each sample is a single region of interest. For each batch, the region of interests are sampled from 2 images, with 64 regions from each image. Each of those 64 includes 16 regions which have an IoU of > 0.5 with the ground truth bounding box, and 48 regions with a IoU of the bounding box between [1, 0.5) with the ground truth bounding box.

The network optimizes a weighted multi-task loss between the classification error of one branch of the network and the localization loss of the other part of the network. Instead of using a simple mean square error between the regression, they use a smoothed L1 distance measure instead.


### Experiments

__*Which dataset(s) were used?*__

VOC 2007, 2012, COCO (a bit)

__*What experiments were conducted*__
* benchmark evaluation on VOC

speed and accuracy are improved

* verifying multitask learning is beneficial

it is shown to imrpove performance to learn multiple tasks

* checking whether convolutional neural networks can learn scale invariance  

They bigger the network, the more it can deal with invariance. Smaller network + feature pyramid input (so multiple scales) performs worse than a bigger network with only 1 size as input

* checking if more training data improves accuracy
More data improves mAP

* do the fc layer + softmax perform better than SVM for classification?

yes, fc + softmax outperforms training SVM's for classification

* are more/less region proposals impactful?

There's a sweet spot. Too many region proposals are harmfull for the accuracy.

### Conclusions/Discussion

__*What do the results mean?*__

A simpler framework where more tasks are done by the neural network is shown to perform better and is also more computationally efficient. Backpropagation is a flexible tool and allows training through max-pool layers.

__*Are there any other implications based on this work?*__

Deep CNN can learn scale invariance, pre-training on ImageNet is very helpful, but first layer can be frozen.
