# Frustratingly Easy Transferability Estimation
ICML, 2022

任务：不用优化、不用训练，评估预训练模型的可迁移性。从而可以为下游任务选择预训练模型以及模型中的层。

难点：
1. Source task 与 target task 之间的相关性对于迁移结果的影响很大。
2. 哪怕是相同的 source data, target data, 模型结构对于迁移效果的影响也很大
![image](https://user-images.githubusercontent.com/35918277/189467320-e5fb79a5-db1a-4561-a9b3-3934235f5af2.png)

3. 最佳的迁移层也不好确定，需要一个平衡.<br>
   若在高层迁移，而高层通常带有更加抽象的信息，可能带有太多 source data 的信息，导致在 target data 上表现不好<br>
   若在低层迁移，需要耗费更长的时间来训练。<br>
 
## 本文提出的方法： TransRate
  思路：计算预训练模型提取出来的特征 与 标签 之间的互信息。<br>
  使用（标签）与（预训练模型的不同层所提取的特征）之间的互信息来衡量可迁移性。<br>
  创新点：使用编码率来替代熵。使得互信息的计算更加高效。<br>

## 实际计算方案
![image](https://user-images.githubusercontent.com/35918277/189467377-cc05d3fc-5af4-4d60-ba12-98e1c978d851.png)
![image](https://user-images.githubusercontent.com/35918277/189467378-6b89e97d-a236-4047-a7fc-f158ff2e97f4.png)
