from numpy import save
import rclpy
import os
from . import change_suffix
from rclpy.node import Node

from std_msgs.msg import String


save_objname = 'out'

def create_object(msg_data):
    obj_dir = os.getcwd() + '/src/object_communication/data/'
    f = open(obj_dir+save_objname+'.txt', 'w')
    f.write(msg_data)

    f.close()
    change_suffix.change_txt_obj(save_objname)


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        create_object(msg.data)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
