# A Fine-Grained Analysis on Distribution Shift

ICLR 2022 oral

- 主要内容：各种域泛化方法在不同情况的分布偏移中的性能比较

- 3种类型的分布偏移：①spurious correlation(SC)；②low-data drift(LDD)；③unseen data shift(UDS)
![image](https://user-images.githubusercontent.com/46912520/190843403-654c5e37-e4c3-45f4-8009-cebf9b301753.png)

- 2个特殊情况：①标签中存在噪声；②数据集大小的限制

- 待评估模型的类型：①Architecture choice；②Heuristic data augmentation；③Learned data augmentation；④Domain generalization；⑤Adaptive approaches；⑥Representation learning 

- 部分实验结果：
![image](https://user-images.githubusercontent.com/46912520/190843569-a42edec5-3bda-4035-b30e-accc535cf5f4.png)
![image](https://user-images.githubusercontent.com/46912520/190843667-7d859b69-7602-4d65-9af6-432aa55bdb45.png)
![image](https://user-images.githubusercontent.com/46912520/190843656-7e5db7f7-c41d-4795-ac6c-69005c8b8d9b.png)

- Takeaways：
1. While we can improve over ERM, no one method always performs best. 
2. Pretraining is a powerful tool across different shifts and datasets. 
3. Heuristic augmentation improves generalization if the augmentation describes an attribute. 
4. Learned data augmentation is effective across different conditions and distribution shifts. 
5. Domain generalization algorithms offer limited performance improvement. 
6. The best algorithms may differ under the precise conditions. 
7. The precise attributes we consider directly impacts the results. 

- Tips：
1. If heuristic augmentations approximate part of the true underlying generative model, use them. 
2. If heuristic augmentations do not help, learn the augmentation. 
3. Use pretraining. 
4. More complex approaches lead to limited improvements. 
