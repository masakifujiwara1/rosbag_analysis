#!/bin/bash

FILE_NAME=${1}

TOPIC_LIST=(
/tf
/tf_static
/amcl_pose
/map_for_costmap
/move_base/global_costmap/costmap
/move_base/global_costmap/costmap_updates
/move_base/local_costmap/costmap
)

TOPIC_FILTER=""
for TOPIC in ${TOPIC_LIST[@]}; do
  TOPIC_FILTER+=$TOPIC
  TOPIC_FILTER+=":=/tmp"
  TOPIC_FILTER+=$TOPIC
  TOPIC_FILTER+=" "
done
rosbag play $FILE_NAME --clock $TOPIC_FILTER