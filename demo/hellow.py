import cv2
import tensorflow as tf

print("Hello Python");
print("Hello OpenCV")

hello = tf.constant("Hello Tensorflow");
session = tf.Session();
print(session.run(hello));
