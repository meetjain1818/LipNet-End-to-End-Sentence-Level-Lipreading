import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppresses all but ERROR messages
import tensorflow as tf
import cv2
import dlib
import numpy as np
from platform import python_version

print("\n\n=======================Verifying Environment=======================")
print("TensorFlow Version:", tf.__version__)
print("GPU Available:", len(tf.config.list_physical_devices('GPU')) > 0)
print("OpenCV Version:", cv2.__version__)
print("DLib Version:", dlib.__version__)
print("NumPy Version:", np.__version__)
print("Python Version:", python_version())