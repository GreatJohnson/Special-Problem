#!/usr/bin/env python
    #from __future__ import print_function
import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import math;
import cv2;
import matplotlib.pyplot as plt;
import sys;
import caffe;
import socket;

class image_converter:

  def __init__(self):
    cv2.namedWindow("Image window", 1)
    print 'start bridge and subscribe'
    self.bridge = CvBridge()
    self.depth_sub = rospy.Subscriber("/camera/depth_registered/image_raw",Image,self.callback2,queue_size=1)
    self.image_sub = rospy.Subscriber("/camera/rgb/image_color",Image,self.callback,queue_size=1)


  def callback2(self,data):
    try:
      depth_image_raw = self.bridge.imgmsg_to_cv2(data, "passthrough")
      depth_image = depth_image_raw.astype(np.uint8)
      cv2.imshow("Depth window", depth_image)
      key = cv2.waitKey(3)
      if (key == 99): # 'c'
          except CvBridgeError, e:
      rospy.loginfo("Conversion failed")


  def callback(self,data):

    try:
      image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError, e:
      print e
    cv_image = image[:,:,:];
    if (key == 99): # 'c'
       # Use the depth data and get the corresponding points in the color image

  def main(args):
    ic = image_converter()
    rospy.init_node('image_converter', anonymous=True)
    try:
      rospy.spin()
    except KeyboardInterrupt:
      print "Shutting down"
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)