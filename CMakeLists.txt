## For full information http://wiki.ros.org/catkin/CMakeLists.txt 

#############################################################################
## Set minimum required version of cmake, project name and compile options ##
#############################################################################
cmake_minimum_required(VERSION 2.8.3)
project(intermittent_monitoring)

###########################################################################
## Find catkin packages and libraries for catkin and system dependencies ##
###########################################################################
find_package(catkin REQUIRED COMPONENTS
  rospy
  geometry_msgs
  actionlib_msgs
  message_generation
)

##########################################
## Setup for python modules and scripts ##
##########################################
catkin_python_setup()

################################################
## Declare ROS messages, services and actions ##
################################################
add_service_files(
    FILES
        flevel.srv
        location.srv
        battery_level.srv
        area_assignment.srv
        assignment_notice.srv
        bid_area.srv
        robot_availability.srv
)

# No new message declared.
add_action_files(
    FILES
        visit.action
        monitor.action
        charge_battery.action
)

generate_messages(
    DEPENDENCIES actionlib_msgs std_msgs
)

################################################
## Declare ROS dynamic reconfigure parameters ##
################################################
# No new parameters declared.

###################################
## catkin specific configuration ##
###################################
catkin_package(
  CATKIN_DEPENDS
    rospy
    geometry_msgs
    std_msgs
    actionlib_msgs
  DEPENDS message_runtime
)

###########
## Build ##
###########
include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

#############
## Install ##
#############

# all install targets should use catkin DESTINATION variables
# See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html

catkin_install_python(
    PROGRAMS
        nodes/motion
        nodes/fmeasure
        nodes/decision_making
        nodes/charging_station
        nodes/monitor_battery
        nodes/area1
        nodes/area2
        nodes/area3
        nodes/monitor_fmeasure1
        nodes/monitor_fmeasure2
        nodes/monitor_fmeasure3
        nodes/auctioneer
        nodes/robot1
        nodes/robot2
        nodes/monitor_battery1
        nodes/monitor_battery2
        src/intermittent_monitoring/cost_fcns.py
        src/intermittent_monitoring/loss_fcns.py
        src/intermittent_monitoring/area.py
        src/intermittent_monitoring/monitor_fmeasure.py
        src/intermittent_monitoring/monitor_battery.py
        src/intermittent_monitoring/robot.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch
	DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

#############
## Testing ##
#############
# No unit test performed.
