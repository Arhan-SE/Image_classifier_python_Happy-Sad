import tensorflow as tf
import os
import cv2

import numpy
from matplotlib import pylot as plt


data_dr = 'Data'
image_exts=['jpeg','jpg','png','bmp']


# for image_class in os.listdir(data_dr):
#     for image in os.listdir(os.path.join(data_dr,image_class)):
#         image_path = os.path.join(data_dr,image_class,image)
#         try:
#             img=cv2.imread(image_path)
#             tip = imghdr.what(image_path)
#             if tip not in image_exts:
#                 print("Image not in ext list {}".format(image_path))
#                 os.remove(image_path)
#         except Exception as e:
#             print("Issue with image {}".format(image_path))

data=tf.keras.utils.image_dataset_from_directory('data')