import rclpy , time
from rclpy.node import Node
from turtlesim.msg import Pose
from std_msgs.msg import Float32  

class TurtleDistancePublisher(Node):
    def __init__(self):
        super().__init__('distance_pub')

        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10
        )

        self.publisher_ = self.create_publisher(Float32, '/turtle/distance_from_origin', 10)

    def pose_callback(self, msg):
        time.sleep(1)
        distance = (msg.x**2 + msg.y**2) ** 0.5
        distance_msg = Float32()
        distance_msg.data = distance
        self.publisher_.publish(distance_msg)
        self.get_logger().info(f"x = {msg.x} , y = {msg.y} , distance = {distance}")
def main(args=None):
    rclpy.init(args=args)
    turtle_distance_publisher = TurtleDistancePublisher()
    rclpy.spin(turtle_distance_publisher)
    turtle_distance_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
