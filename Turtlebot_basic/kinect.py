#!/usr/bin/env python

'''
Copyright (c) 2015, Mark Silliman
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

#Code is inspired by http://wiki.ros.org/navigation/Tutorials/SendingSimpleGoals (written in C++).
#TurtleBot must have minimal.launch & amcl_demo.launch running prior to starting this script.

#!/usr/bin/env python
""" 
  Example code of how to convert ROS images to OpenCV's cv::Mat
  This is the solution to HW2, using Python.

  See also cv_bridge tutorials: 
    http://www.ros.org/wiki/cv_bridge
"""

import roslib
import rospy

import cv2
from cv_bridge import CvBridge, CvBridgeError

from std_msgs.msg import String
from sensor_msgs.msg import Image

class image_blur:

  def __init__(self):
    # initialize a node called 

    # create a window to display results in
    cv2.namedWindow("image_view", 1)
    self.bridge = CvBridge()

    # part 2.1 of hw2 -- subscribe to a topic called image
    self.image_sub = rospy.Subscriber("/camera/rgb/image_color",Image,self.callback,queue_size=1)

  def callback(self,data):
    """ This is a callback which recieves images and processes them. """
    # convert image into openCV format
    try:
      # bgr8 is the pixel encoding -- 8 bits per color, organized as blue/green/red
      image = self.bridge.imgmsg_to_cv2(data,"bgr8")
    except CvBridgeError, e:
      # all print statements should use a rospy.log_ form, don't print!
      rospy.loginfo("Conversion failed")

    # for now, we'll blur using a median blur
    #cv.Smooth(cv_image, cv_image, smoothtype=cv.CV_MEDIAN, param1=31, param2=0, param3=0, param4=0)

    # show the image
    cv_image = image[:,:,:];
    if(key == 99):


  def main(args):
      ic = image_conventer()
      rospy.init_node('image_converter', anonymous=True)
      try:
        rospy.spin()
    except CvBridgeError, e:
      # all print statements should use a rospy.log_ form, don't print!
      rospy.loginfo("Conversion failed")       
      cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.args)