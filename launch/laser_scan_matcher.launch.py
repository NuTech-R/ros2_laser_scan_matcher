from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # パッケージのshareディレクトリを取得
    pkg_dir = get_package_share_directory('ros2_laser_scan_matcher')
    
    # 設定ファイルへのパス
    config_file = os.path.join(pkg_dir, 'config', 'laser_scan_matcher_params.yaml')
    
    # ノードの起動設定
    laser_scan_matcher_node = Node(
        package='ros2_laser_scan_matcher',
        executable='laser_scan_matcher',
        name='laser_scan_matcher',
        output='screen',
        parameters=[config_file]
    )
    
    return LaunchDescription([
        laser_scan_matcher_node
    ])