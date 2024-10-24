#!/usr/bin/env python3

import rospy
import tf2_ros
import tf2_msgs.msg
from tf2_msgs.msg import TFMessage

class TFMapFilter:
    def __init__(self):
        # ノードの初期化
        rospy.init_node('tf_map_filter')

        # tfの購読者
        self.tf_sub = rospy.Subscriber('/tmp/tf', TFMessage, self.tf_callback)
        # tf_staticの購読者
        self.tf_static_sub = rospy.Subscriber('/tmp/tf_static', TFMessage, self.tf_static_callback)

        # tfのパブリッシャー
        self.tf_pub = rospy.Publisher('/tf', TFMessage, queue_size=10)
        # tf_staticのパブリッシャー
        self.tf_static_pub = rospy.Publisher('/tf_static', TFMessage, queue_size=10)

    def tf_callback(self, msg):
        # mapフレームをフィルタリング
        filtered_transforms = [t for t in msg.transforms if t.header.frame_id != 'map' and t.child_frame_id != 'map']
        if filtered_transforms:
            filtered_msg = TFMessage(transforms=filtered_transforms)
            self.tf_pub.publish(filtered_msg)

    def tf_static_callback(self, msg):
        # mapフレームをフィルタリング
        filtered_transforms = [t for t in msg.transforms if t.header.frame_id != 'map' and t.child_frame_id != 'map']
        if filtered_transforms:
            filtered_msg = TFMessage(transforms=filtered_transforms)
            self.tf_static_pub.publish(filtered_msg)

if __name__ == '__main__':
    try:
        # ノードの実行
        filter_node = TFMapFilter()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
