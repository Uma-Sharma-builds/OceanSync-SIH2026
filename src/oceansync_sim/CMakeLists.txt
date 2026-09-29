cmake_minimum_required(VERSION 3.8)
project(oceansync_sim)

find_package(ament_cmake REQUIRED)

install(DIRECTORY
  worlds
  models
  urdf
  config
  launch
  rviz
  DESTINATION share/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/depth_node.py
  scripts/sensor_monitor.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
