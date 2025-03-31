cmake_minimum_required(VERSION 3.5)

project(ros2_laser_scan_matcher)

# コンパイルオプション
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# 依存関係を見つける
find_package(ament_cmake REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(rclcpp REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)
find_package(rcutils REQUIRED)
find_package(PkgConfig)
find_package(Eigen3 REQUIRED)
find_package(Boost COMPONENTS thread REQUIRED)

# CSMのビルド設定
add_subdirectory(csm)

# レーザースキャンマッチャーの実行ファイル
add_executable(laser_scan_matcher src/laser_scan_matcher.cpp)

# インクルードディレクトリ
target_include_directories(laser_scan_matcher
  PRIVATE
  include
  ${EIGEN3_INCLUDE_DIRS}
  ${CMAKE_CURRENT_SOURCE_DIR}/csm/include
)

# 依存関係の設定
ament_target_dependencies(laser_scan_matcher
  rclcpp
  sensor_msgs
  rcutils
  Eigen3
  tf2_ros
  tf2
  tf2_geometry_msgs
  Boost
  nav_msgs
)

# CSMライブラリをリンク
target_link_libraries(laser_scan_matcher
  csm
)

# 実行ファイルをインストール
install(TARGETS laser_scan_matcher
  DESTINATION lib/${PROJECT_NAME}
)

# configとlaunchディレクトリをインストール
install(DIRECTORY config/
  DESTINATION share/${PROJECT_NAME}/config
)

install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

ament_package()