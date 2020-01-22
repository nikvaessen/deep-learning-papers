<!--
{"title": "Rich feature hierarchies for accurate object detection and semantic segmentation", "url": "https://arxiv.org/abs/1311.2524", "topics": "2d-object-detection", "date": "2020-01-21", "estimated_minutes": "300"}
-->
### Rich feature hierarchies for accurate object detection and semantic segmentation

Read on: 2020-01-21  
Time spent: *300* minutes  
Link to pdf: https://arxiv.org/abs/1311.2524  
Topic(s): `2d-object-detection`

citation:
```
@inproceedings{Girshick2014,
archivePrefix = {arXiv},
arxivId = {1311.2524},
author = {Girshick, Ross and Donahue, Jeff and Darrell, Trevor and Malik, Jitendra},
booktitle = {Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition},
doi = {10.1109/CVPR.2014.81},
eprint = {1311.2524},
isbn = {9781479951178},
issn = {10636919},
mendeley-groups = {2d obj det},
month = {sep},
pages = {580--587},
publisher = {IEEE Computer Society},
title = {{Rich feature hierarchies for accurate object detection and semantic segmentation}},
year = {2014}
}

```

### Abstract

__*What questions are the authors addressing?*__

Can a CNN replace the "tradiotional" low level feature engineering methods for 2d object detection?

How can deep neural networks be used in a problem setting with scarce data?

__*What is the major finding or scientific contribution?*__

Present the region-proposal framework of 2d object detection

__*What is the work's significance?*__

Present a system which improves on the SOTA results of VOC 2012 by 30%

### Materials and Methods

__*What is their experimental methodology or developed system?*__

Their system is made up out of 3 modules:

1. Region proposal generation
2. Feature encoder
3. classification and detection predictor

The region proposal generation is done using selective search. However, this could be replaced for another method (it's agnostic to what method performs region proposal). At test time, each image has ~2000 region proposals.

A 4096-length feature vector is created by using AlexNet for each region proposal. The proposed regions are warped into the required 227x277 resolution.  

For each class, a separate SVM (trained on that class) scores all the feature vector of the proposed regions. Independently for each class, non-max suppression is run, which will reject a proposal if it overlaps (more than x%) with another region which has a higher confidence score by the SVM. The threshold x is learned.    

Training:

The CNN was pre-trained on Imagenet classification with slightly worse performance than reported by the AlexNet paper. After pretraining, the last 1000-classes fc layer is replaced by a random N+1 layer instead. (N=20 for VOC, N=200 for ILSVRC2013). The proposed regions for each class for each image are sampled
at random in a batch of 128, where the batch contains 32 positive and 96 background proposals. A proposal is positive if the IoU with the ground truth >= 0.5. With these batches training on the CNN is continued.

For training the SVM for each class, they generate positive and negative samples in a similar way as fine-tuning the CNN but the threshold was 0.3 instead. They use hard-negative mining as well.

Only explained in the appendix: They train a linear regression model which fine-tunes the bounding boxes of a region proposal as a final step. They evaluate the model with and without this final step.  

__*If there are alternative approaches, how did they select this system?*__

They looked for a method which can scale to a lot more object classes. traditional methods cannot scale, but CNN's can. They selected selective search for region proposals for comparison with other recent work.

### Experiments

__*Which dataset(s) were used?*__

ImageNet (ILSVRC2012) for pre-training  
VOC 2007 for validation design decisions/hyperparameters

VOC 2010, VOC 2012 for testing  
ILSVRC2013 for testing

__*What experiments were conducted*__  
Evaluation:

mAP of 53.7% on VOC 2010 (from 35.1%)  
mAP of 53.3% on VOC 2012  
mAP of 31.4% on ILSVRC2013 (from 24.3%)


### Conclusions/Discussion

__*What do the results mean?*__

Using a CNN in a detection pipeline has a significant performance impact on both accuracy and running time.

### Additional notes or thoughts

#### Future reading
