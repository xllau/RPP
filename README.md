# RPP
using the ResNet 101 and the pyramid pooling way to detect the road on KITTI raod dataset.
It have achived the results as follow:

| Benchmark | MaxF | AP  | PRE  | REC | FPR | FNR |
| --------  | ---- | --- |------|---- |-----|-----|
| **UM_ROAD**| 96.04% | 89.77% | 95.61%  |96.48% | 2.02% | 3.52%|
| **UMM_ROAD**|  97.03% |92.36% |96.36%| 97.70% |4.06% |2.30%|
| **UU_ROAD**|  95.47% |88.74% |95.16 % |95.77% |1.59% |4.23%|

This is the link:
http://www.cvlibs.net/datasets/kitti/eval_road.php

The project name is RPP. It have the rank of 1st on um_road, 4th on umm_road and 1st on uu_road on the data of Dec 25, 2016.

The repository includes model file, deploy.prototxt, and some pics. 
You can download and run on justify the model result.

