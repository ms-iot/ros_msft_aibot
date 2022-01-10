import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
    aibot_node = Node(
        package='ros_msft_aibot', 
        executable='ros_msft_aibot', 
        name='ros_msft_aibot')
    return LaunchDescription([
        aibot_node
    ])
