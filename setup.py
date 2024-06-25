from setuptools import find_packages, setup

package_name = 'ros_yolo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aspera',
    maintainer_email='aspera@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'capturer = ros_yolo.camera_capture_function:main',
            'detector = ros_yolo.target_detect_function:main',
        ],
    },
)
