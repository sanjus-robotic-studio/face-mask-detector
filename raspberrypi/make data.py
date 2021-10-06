import numpy as np
import cv2
import os
import pickle
import random

main_path='dataset'
subFolders=['with_mask','without_mask']


training_data = []
X = []
y = []

def create_training_data():
    for category in subFolders:  # do with_mask and without_mask

        path = os.path.join(main_path,category)  # create path to with_mask and without_mask
        class_num = subFolders.index(category)  # get the classification  (0 or a 1). 0=dog 1=cat

        for img in os.listdir(path):  # iterate over each image per dogs and cats
            try:
                img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
                new_array = cv2.resize(img_array, (150, 150))  # resize to normalize data size
                training_data.append([new_array, class_num])  # add this to our training_data
            except Exception as e:  # in the interest in keeping the output clean...
                pass
     

create_training_data()

print(f' length of data {len(training_data)}')

random.shuffle(training_data)

for features,label in training_data:
    X.append(features)
    y.append(label)


X = np.array(X).reshape(-1, 150, 150, 1)    
y=np.array(y)

pickle_out = open("raspberrypi/X.pickle","wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("raspberrypi/y.pickle","wb")
pickle.dump(y, pickle_out)
pickle_out.close()