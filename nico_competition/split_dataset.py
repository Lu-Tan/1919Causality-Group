import os
import shutil

train_dir = 'public_ood_0412_nodomainlabel/train/'
classes = os.listdir(train_dir)
classes_dirs = [train_dir+c for c in classes]
classes_nums = [len(os.listdir(d)) for d in classes_dirs]
classes_dict = dict(zip(classes,classes_nums))
print(classes_dict)
print("min:",min(zip(classes,classes_nums),key=lambda x:x[1]))
print("max:",max(zip(classes,classes_nums),key=lambda x:x[1]))
print("sum:",sum(classes_nums))

for c in classes:
    print(c)
    class_dir = train_dir+c
    class_files = os.listdir(class_dir)
    train_num = int(len(class_files)/5*4)
    train_list = class_files[:train_num]
    test_list = class_files[train_num:]
    for f in train_list:
        if not os.path.exists('dataset/train_split/'+c+'/'):
            os.mkdir('dataset/train_split/'+c+'/')
        shutil.copy(class_dir+'/'+f,'dataset/train_split/'+c+'/'+f)
    for f in test_list:
        if not os.path.exists('dataset/test_split/'+c+'/'):
            os.mkdir('dataset/test_split/'+c+'/')
        shutil.copy(class_dir+'/'+f,'dataset/test_split/'+c+'/'+f)
