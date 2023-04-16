# Python 3 code to rename multiple
# files in a directory or folder

# importing os module
import os

path = "C:/Users/khiem/OneDrive/Desktop/dataset/0.5_50/"
new_path = "C:/Users/khiem/OneDrive/Desktop/dataset/dataset/"
imgs_name = os.listdir(path)
count = 1120
for img_name in imgs_name:
    os.rename(path + img_name, new_path + str(count) + ".png")
    count += 1