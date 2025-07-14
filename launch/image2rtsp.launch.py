import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    default_config_path = os.path.join(
        get_package_share_directory("image2rtsp"), "config", "parameters.yaml"
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            "image2rtsp_config",
            default_value=default_config_path,
            description="Path to the image2rtsp config file"
        ),

        Node(
            package="image2rtsp",
            executable="image2rtsp",
            name="image2rtsp",
            parameters=[LaunchConfiguration("image2rtsp_config")]
        )
    ])
