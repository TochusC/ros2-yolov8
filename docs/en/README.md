<div align="center">

<img src="/docs/img/img.png" style="margin-bottom: 0; height: 64%; width: 64%;">

<h1 style="margin-top: 0">ROS2-based Object Detection via Communication</h1>

### Introduction to Intelligent Computing Systems

[![ros2](https://img.shields.io/badge/ROS2-foxy-blue)](https://index.ros.org/doc/ros2/)
[![python](https://img.shields.io/badge/Python-3.10.12-blue)](https://www.python.org/)
![license](https://img.shields.io/badge/License-MIT-green)

[![madewithlove](https://img.shields.io/badge/made_with-%E2%9D%A4-red?style=for-the-badge&labelColor=orange)](https://github.com/TochusC)

[**简体中文**](/README.md) | [**English**](/docs/en/README.md) 
</div>

---

## Project Structure📁
```angular2html
docs  # README-related files
├── img
resources # Resource files
ros_yolo # Implementation code
├── src
│   ├── init.py # Node initialization
│   ├── camera_capture_function.py # Camera capture function
│   ├── target_detect_function.py # Target detection function
test # Test files
package.xml # ROS2 package description file
setup.cfg # Configuration file
setup.py # Installation file
```

## Implementation Details🔍
Using ROS2 for communication, sending node captures images from the camera, receiving node processes image data using YOLOv8 for object detection, and displays the detection results.

## How to Run❓

1. Clone the project to the ROS2 workspace, such as `~/ros2_ws/src/`
2. Navigate into the workspace, build the project with `colcon build`
3. Set up the environment for running with source `~/ros2_ws/install/setup.bash`
4. Start the capture node with `ros2 run ros_yolo capturer`
5. Start the detection node with `ros2 run ros_yolo detector`
6. Enjoy the results😉!

## Running Effect🌟
<div align="center">

    ![Running Effect](docs/img/result.png)](docs/img/result.png)

</div>
