<!--
{"title": "Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks", "url": "https://arxiv.org/abs/1506.01497", "topics": "2d-object-detection", "date": "2020-01-22", "estimated_minutes": "300"}
-->
### Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks

Read on: 2020-01-22  
Time spent: *300* minutes  
Link to pdf: https://arxiv.org/abs/1506.01497  
Topic(s): `2d-object-detection`

citation:
```
@article{Ren2017,
archivePrefix = {arXiv},
arxivId = {1506.01497},
author = {Ren, Shaoqing and He, Kaiming and Girshick, Ross and Sun, Jian},
doi = {10.1109/TPAMI.2016.2577031},
eprint = {1506.01497},
issn = {01628828},
journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
keywords = {Object detection,convolutional neural network,region proposal},
mendeley-groups = {2d obj det},
month = {jun},
number = {6},
pages = {1137--1149},
pmid = {27295650},
publisher = {IEEE Computer Society},
title = {{Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks}},
url = {https://arxiv.org/abs/1506.01497},
volume = {39},
year = {2017}
}

```

### Abstract

__*What questions are the authors addressing?*__

Can the object region proposal method be encoded by/in the neural network architecture?

__*What is the major finding or scientific contribution?*__

Using RPN in the object detection pipeline increases mAP and improves running time

__*What is the work's significance?*__

end-to-end learning for the whole 2d object pipeline, including object proposals

### Materials and Methods

__*What is their experimental methodology or developed system?*__

Image is encoded by a deep conv net such as vgg16

The resulting feature map is convolved by the RPN.
The RPN is a single 3x3 convolutional layer followed by 2 sibling 1x1 convolutional layers.
At each sliding window of the 3x3 conv layer, the goal is to predict k object proposals.
Thus one 1x1 convolutional layer sibling computes 2k binary "object classification scores", 1 positive and 1 negative for each proposal
The other 1x1 convolutional layer sibling computes 4k object regions (xmin, ymin, w, h)

The best region proposals by the RPN are selected based on non-max suppression on their class score with IoU > 0.7.

The resulting region proposals are taken from the feature map of the encoder and fed through the classification network (identical to Fast RCN)


### Conclusions/Discussion

__*What do the results mean?*__

The whole object detection pipeline can be modeled as a neural architecture

### Additional notes or thoughts

#### Future reading
