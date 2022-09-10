![image](https://user-images.githubusercontent.com/35918277/189467550-aa3b7c62-f38f-4c30-ad7c-602579e70435.png)
2022.7.19 ArXiv

目标：从统一的视角，在现实数据集上分析解决OOD问题的各个流派方法。<br>

本文的研究问题：<\br>
1. 当我们可以访问到一个数据集时，我们应该用什么指标来描述OOD robustness ?
2. 模型结构和微调策略会如何影响OOD robustness?
因此，本文做了大量实验。全都是在 ImageNet 上预训练模型。 这是一篇主要贡献为实验的文章。<br>

但实际上并没有太多东西，都是验证了一些直觉：<br>
- 随着 ID acc 的增长，OOD acc 可能不变，可能增长，可能无关，但是绝对不会下降。<br>
实验：计算随着一个domain acc的增长，另一个domain acc 的变化情况
![image](https://user-images.githubusercontent.com/35918277/189467696-6850d55d-bb34-4eab-a34d-5f46a797a45c.png)

- ID 是最好的指示OOD泛化性能的指标，其次是hold-out OOD acc.<br>
实验：计算各个指标与OOD acc的相关度分数
Adjusted: 计算各个指标与 “训练一个线性分类器，从ID acc预测OOD acc的准确度”之间的相关度分数![image](https://user-images.githubusercontent.com/35918277/189467742-5de73633-5676-4d77-8ca2-d4a19db125d9.png)
![image](https://user-images.githubusercontent.com/35918277/189467745-84d6a439-55eb-476a-8577-4be25c1d3749.png)

- 模型结构对OOD Robustness的影响 <br>
实验：计算不同模型结构下的分类 error

![image](https://user-images.githubusercontent.com/35918277/189467761-85591b6d-a777-4e9f-8459-61722fd11e3e.png)

