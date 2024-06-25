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
from cv_bridge import CvBridge
import cv2
from ultralytics import YOLO

class TargetDetector(Node):

    def __init__(self):
        super().__init__('target_detector')
        self.subscription = self.create_subscription(
            Image,
            'image_topic',
            self.listener_callback,
            10)
        self.bridge = CvBridge()

    def listener_callback(self, data):
        # 将 ROS 2 的 Image 消息类型转换为 OpenCV 格式
        cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")

        # 加载预训练YOLO模型
        model = YOLO("yolov8n.pt")
        results = model(cv_image)
        for detection in results:
            boxes = detection.boxes

            for i in range(len(boxes)):
                [x1, y1, x2, y2] = boxes[i].xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # 转换为整数类型
                name = detection.names[i]

                # 在图像上绘制矩形框和标签文本
                cv2.rectangle(cv_image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # 绘制矩形框
                cv2.putText(cv_image, name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)  # 放置文本

        # 显示图片
        cv2.imshow('image', cv_image)
        cv2.waitKey(1)


def main(args=None):
    rclpy.init(args=args)

    target_detector = TargetDetector()

    rclpy.spin(target_detector)

    target_detector.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
