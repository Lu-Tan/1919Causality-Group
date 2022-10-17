# CoCoOp：Conditional Prompt Learning for Vision-Language Models
- CoOp的一个关键问题：学习到的context不能泛化到unseen的类别，对base class产生了过拟合。因此提出了CoCoOp，为每一个image 产生input-conditional的向量，这种动态的prompt可以适应每一个instance，因此对class shift不那么敏感。
![image](https://user-images.githubusercontent.com/49772993/196183110-a00014a4-08d0-46f4-817e-f0907796c582.png)
## 方法
![image](https://user-images.githubusercontent.com/49772993/196183129-42f2ebf1-d9cc-424f-9823-76bfb3b94fc6.png)
![image](https://user-images.githubusercontent.com/49772993/196183153-db795446-5578-4baf-b650-ba0a4305123a.png)
![image](https://user-images.githubusercontent.com/49772993/196183172-80c5e462-d306-4052-a8e8-5016f889a69d.png)
- 新增一个meata-net，由Linear-ReLU-Linear组成，对每个image feature进行学习。
## 实验
- 用 ViT-B/16，context length = 4 ，pre-trained word embeddings = “a photo of a” 
### 从基类泛化到新类的实验
![image](https://user-images.githubusercontent.com/49772993/196183274-f00503ef-870a-4b34-850f-948713947b14.png)
- 虽然在base类CoOp很好，但是新类上较差，调和平均后与CLIP相当。但CoCoOp新类上表现较好。
- CoCoOp缩小了泛化gap。证明instance-conditional prompt更具有泛化性。
![image](https://user-images.githubusercontent.com/49772993/196183355-90c2ddd0-81f5-4aa0-9023-9eb8e8bba463.png)
- CoCoOp在泛化性能上的增益超过了在基类准确度上的损失
### 跨数据集迁移
![image](https://user-images.githubusercontent.com/49772993/196183373-aae8f656-a7cb-476e-8ede-60788ba7b6e5.png)
- 比CoOp好。
### 域泛化
![image](https://user-images.githubusercontent.com/49772993/196183437-1ec4dbe7-08f1-462f-a936-8e35b1949a66.png)
- 证明instance-conditional prompt更具有泛化性。
### 深入分析
- 用手工prompt初始化更好。
- 因为CoCoOp增加了参数，所以用更大的CoOp做了对比试验。
