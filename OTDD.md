# Geometric Dataset Distances via Optimal Transport 
NIPS 2020

主要应用：无需训练的情况下衡量两个数据集之间的差异

理论基础：最优传输距离—————将一个分布变换为另一个分布的最短路径（https://zhuanlan.zhihu.com/p/82424946）

难点：不同数据集之间标签可能不同，因此需要找到衡量标签之间距离的方式

主要方法：标签之间的距离=标签对应的特征之间的最优传输距离，也是Wasserstein Distance，为了方便求解假设数据为高斯分布，该问题有解析解；数据集之间的距离就是两个数据集分布的最优传输距离OTDD（Optimal Transport Dataset Distance）
