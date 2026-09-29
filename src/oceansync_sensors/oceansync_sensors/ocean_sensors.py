#!/usr/bin/env python3

import math

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64


class OceanSensors(Node):

    def __init__(self):
        super().__init__('ocean_sensors')

        # Publishers
        self.temperature_pub = self.create_publisher(
            Float64,
            '/oceansync/temperature',
            10
        )

        self.depth_pub = self.create_publisher(
            Float64,
            '/oceansync/depth',
            10
        )

        self.pressure_pub = self.create_publisher(
            Float64,
            '/oceansync/pressure',
            10
        )

        # Sensor update rate = 10 Hz
        self.timer = self.create_timer(
            0.1,
            self.update_sensors
        )

        # Ocean parameters
        self.surface_temperature = 25.0  # Celsius
        self.temperature_gradient = 0.02  # °C per meter

        self.water_density = 1025.0       # kg/m³
        self.gravity = 9.81               # m/s²
        self.atmospheric_pressure = 101325.0  # Pa

        self.get_logger().info(
            'OceanSync temperature/depth/pressure sensor node started'
        )

    def get_device_position(self):

        # TEMPORARY POSITION SOURCE
        #
        # For the first test we use a simulated movement.
        # Later this will be replaced by the actual floating
        # device position from Gazebo.

        time = self.get_clock().now().nanoseconds / 1e9

        x = 2.0 * math.sin(0.1 * time)
        y = 2.0 * math.cos(0.1 * time)

        # Floating device moves vertically with the waves
        z = 0.5 + 0.2 * math.sin(0.5 * time)

        return x, y, z

    def update_sensors(self):

        x, y, z = self.get_device_position()

        # Gazebo uses Z as vertical direction.
        #
        # Water surface = z = 0
        #
        # Therefore:
        #
        # depth = -z
        #
        # If the device is above the water,
        # depth should not become negative.

        depth = max(0.0, -z)

        # Temperature decreases with depth.
        temperature = (
            self.surface_temperature
            - self.temperature_gradient * depth
        )

        # Hydrostatic pressure.
        pressure = (
            self.atmospheric_pressure
            + self.water_density * self.gravity * depth
        )

        # Publish temperature
        temperature_msg = Float64()
        temperature_msg.data = temperature

        self.temperature_pub.publish(temperature_msg)

        # Publish depth
        depth_msg = Float64()
        depth_msg.data = depth

        self.depth_pub.publish(depth_msg)

        # Publish pressure
        pressure_msg = Float64()
        pressure_msg.data = pressure

        self.pressure_pub.publish(pressure_msg)

        # Terminal output
        self.get_logger().info(
            f'Position: ({x:.2f}, {y:.2f}, {z:.2f}) | '
            f'Depth: {depth:.2f} m | '
            f'Temperature: {temperature:.2f} °C | '
            f'Pressure: {pressure:.0f} Pa'
        )


def main(args=None):

    rclpy.init(args=args)

    node = OceanSensors()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
