import cv2
import glob
import numpy as np
import pickle   
x_train = []
y_train = []

for filename in glob.glob("./data/CaBaSa/*.bmp"):
    img = cv2.resize(cv2.imread(filename), (150,150))
    x_train.append(img)
    y_train.append(0)

for filename in glob.glob("./data/CaBop/*.bmp"):
    img = cv2.resize(cv2.imread(filename), (150,150))
    x_train.append(img)
    y_train.append(1)

for filename in glob.glob("./data/CaChepDo/*.bmp"):
    img = cv2.resize(cv2.imread(filename), (150,150))
    x_train.append(img)
    y_train.append(2)

for filename in glob.glob("./data/CaChim/*.bmp"):
    img = cv2.resize(cv2.imread(filename), (150,150))
    x_train.append(img)
    y_train.append(3)


x_train = np.array(x_train)
y_train = np.array(y_train)
print(x_train.shape)
print(y_train.shape)
with open("data.ca", "wb") as f:
        pickle.dump((x_train, y_train),f)
