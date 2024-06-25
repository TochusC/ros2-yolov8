# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge  # 用于 OpenCV 和 ROS 之间的图像转换
import cv2

class CameraCapturer(Node):

    def __init__(self):
        super().__init__('camera_capturer')
        self.publisher_ = self.create_publisher(Image, 'image_topic', 10)
        timer_period = 1  # 图片发布周期，单位为秒
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.bridge = CvBridge()

    def timer_callback(self):
        # 打开默认摄像头。
        cap = cv2.VideoCapture(0)

        raw_image = cv2.imread('fallback.jpg')
        if  cap.isOpened():
            # 捕获一帧图像
            ret, frame = cap.read()
            if ret:
                raw_image = frame

        # 将图片转换为 ROS 2 的 Image 消息类型
        image_msg = self.bridge.cv2_to_imgmsg(raw_image, "bgr8")

        # 发布图片消息
        self.publisher_.publish(image_msg)
        self.get_logger().info('Publishing image')



def main(args=None):
    rclpy.init(args=args)

    camera_capturer = CameraCapturer()

    rclpy.spin(camera_capturer)

    camera_capturer.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
