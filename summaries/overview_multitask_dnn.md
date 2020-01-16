<!--
{"title": "An Overview of Multi-Task Learning in Deep Neural Networks", "url": "https://arxiv.org/abs/1706.05098", "topics": "multi-task", "date": "2020-01-16", "estimated_minutes": "180"}
-->
### An Overview of Multi-Task Learning in Deep Neural Networks

Read on: 2020-01-16  
Time spent: *180* minutes  
Link to pdf: https://arxiv.org/abs/1706.05098  
Topic(s): `multi-task`

citation:
```
@techreport{Ruder2017,
arxivId = {1706.05098v1},
author = {Ruder, Sebastian},
eprint = {1706.05098v1},
institution = {Insight Centre for Data Analytics, NUI Galway},
mendeley-groups = {multi-task learning},
title = {{An Overview of Multi-Task Learning in Deep Neural Networks}},
url = {http://sebastianruder.com/multi-task/index.},
year = {2017}
}

```

### Abstract

__*What questions are the authors addressing?*__

What is the current (2017) status of Multi-Task learning?  

__*What is the major finding or scientific contribution*__

Distilling the current knowledge about multi-task learning into a single source

__*What is the work's significance?*__

It gives an overview of the current techniques and literature around the topic of
multi-task learning in machine learning.

### Motivation of MTL

Biologically, you use related information to learn new tasks.  
Pedagogically, you first learn fundamental tasks before complex tasks.   
From a machine learning perspective, learning multiple tasks adds a bias for
finding solutions which can explain more than one task    

### Methods of MTL

There are 2 ways of doing MTL:
 1. **hard parameter sharing**: a set of shared layers after which the networks branches with small subnetworks for each task
 2. **soft parameter sharing**: distinct network for each task but a set of layers in each network are constrained to be similar

### Why does MTL work?

1. Implicit data augmentation: By learning multiple tasks there is a reduced
change of overfitting by due to averaging the noisy patterns in both datasets
2. Attention focusing: multiple tasks can provide more evidence that certain
features are relevant and thus the model can only focus on those features
3. eavesdropping: some patterns might be obvious in task B while very hard to
detect in task A
4. representation bias: features which are good for both tasks have a bias
5. inductive bias: more than 1 task needs to be explained

### Techniques in ANN for MTL

Most common technique is to do hard-parameter sharing on convolutional layers
and then have some FC layers for each tasks

Some papers which introduce "better" mechanisms:

1. Deep Relationship networks: FC layers after hard-shared parameters have
matrix priors
2. Fully-adaptive feature sharing: a model is iteratively grown which creates
groups of shared parameters for each tasks
3. Cross-stitching: A soft-parameter sharing set up where models learn a linear combination of
each layer of each networks
4. Low supervision: some tasks should be supervised at lower layers
5. Joint many-task model: (pre-determined) hierarchy of different models for each task
6. weighting losses with uncertainty: The loss function takes into account the
uncertainty of each task
7. Tensor factorization: The model parameters are split into shared and task-specific
8. Sluice network: A model which learns what layers and subspaces should be shared

### Auxiliary tasks

You can also consider the scenario where you're only interested in performing
a single task but add "helper" tasks to get the "benefits" of MTL models, which
can lead to higher accuracies.

Some examples of this setting are:

1. related task: Try to predict things which are in the same domain (e.g detect road signs for the primary task of determining steering commands)
2. Adversarial: Create the opposite task and train and try to maximize this loss
3. hints: try to predict a broader setting which has some resemblance (e.g predict whether there is a road when trying to detect holes in a road)
4. Focusing attention: add a "bias" by forcing the model to learn a certain feature. For example, predict road markings when trying to predict steering
commands
5. Quantization smoothing: If problem is discrete, try to have different levels of discretization as each task  
6. predicting inputs: for some features, turn the feature into something which
also needs to be predicted (turn input feature into output feature) if it's not
seen as a valuable feature
7. Representation learning: Have one task be an auto encoder



### Additional notes or thoughts

It would be interesting to see concrete evidence for the claims "why does MTL work"

It's fairly straightforward to initially attempt hard parameter sharing when
facing a MTL problem. Somehow learning what to share and not to share might have
benefits, however.

#### Future reading

All the papers mentioned in section 6.
