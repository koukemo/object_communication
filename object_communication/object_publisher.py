import rclpy
from . import change_suffix
from time import sleep
import os
from std_msgs.msg import String


open_objname = 'test'

def change_text_string(file_name):
    obj_dir = os.getcwd() + '/src/object_communication/data/'
    change_suffix.change_obj_txt(file_name)
    f = open(obj_dir + file_name + '.txt', 'r', encoding='UTF-8')

    data = f.read()
    f.close()
    change_suffix.change_txt_obj(file_name)

    return data


def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('minimal_publisher')
    publisher = node.create_publisher(String, 'topic', 10)

    msg = String()
    senden = True
    i = 0
    while rclpy.ok():
        msg.data = change_text_string(open_objname)
        i += 1
        # node.get_logger().info('Publishing: "%s"' % msg.data)
        if senden:
            publisher.publish(msg)
            senden = False
        sleep(0.5)  # seconds

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
