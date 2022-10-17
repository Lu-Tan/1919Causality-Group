# CoOp：LearningtoPromptforVision-LanguageModels

将文本标签转化为离散的数字标签，丢失了封装在文本中的语义信息，使得识别系统被限制到闭集concept中。而使用vl模型可以通过prompt进行多种下游任务。但prompt需要tune非常耗时，微小的变动会造成性能很大的不同，并且需要对任务的先验知识。
## 方法
### VL预训练模型

Image encoder：resnet50、ViT

Text encoder：Transformer

word（tokens）-->byte pair encoding representation-->512d vector

### Zero-shot inference
- 用不同类别的prompt产生权重，再计算概率：

![image](https://user-images.githubusercontent.com/49772993/196181119-42136066-7d4f-4c61-9edf-03fd82ff70f1.png)

### Context Optimization (CoOp)
- 用连续向量对context words进行建模。有两种实现方式：

①unified context，每类用相同的context，但[CLASS]不同。

![image](https://user-images.githubusercontent.com/49772993/196181180-5a0d4d04-c8f1-4d11-9363-c8e1d09e3169.png)

也可以将[CLASS]放在中间增加灵活性（可以在后面的cell增加补充信息，或者用句号进行中断）

![image](https://user-images.githubusercontent.com/49772993/196181200-5aa49393-c57b-4a4a-bb88-1852b9afaafe.png)

②class-specific context，每个类别context不同，适用于一些细粒度分类任务。

![image](https://user-images.githubusercontent.com/49772993/196181212-8eeee4a9-536e-4700-ace2-44e044089f02.png)

训练方式：固定预训练参数，梯度随着text encoder传播来更新context向量，从而利用text encoder中的语义信息。
### 讨论
NLP中的prompt的不同：backbone结构不同，VL vs L，目标函数不同，对比学习vs自回归学习
## 实验
### Baseline
- zero-shot CLIP：使用常见的prompt：a photo of a [CLASS]等
- linear probe model：在CLIP特征之上加一层线性分类器
### few-shot实验
![image](https://user-images.githubusercontent.com/49772993/196181229-8231adfb-6b13-4828-96b6-a50f2f6e2a04.png)
### 域泛化实验
- CoOp提高了域泛化鲁棒性，并且更少的context token有更好的效果。（可能能防止过拟合）
![image](https://user-images.githubusercontent.com/49772993/196181292-3cb95de1-0ffc-4013-9b88-bc8809a15ae9.png)
![image](https://user-images.githubusercontent.com/49772993/196181338-ce1c7e92-aaa0-427c-8ed5-8e832f97e30a.png)

