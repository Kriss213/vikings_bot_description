from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, PythonExpression


from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    vikings_bot_name_arg = DeclareLaunchArgument("vikings_bot_name",
                    default_value="vikings_bot_1",
                    description="Namespace of robot - [vikings_bot_1 or vikings_bot_2]")
    robot_file_arg = DeclareLaunchArgument("robot_file", default_value="vikings_bot.xacro")
    use_sim_arg = DeclareLaunchArgument("use_sim", default_value="true")

    vikings_bot_name = LaunchConfiguration("vikings_bot_name")
    use_sim = LaunchConfiguration("use_sim")
  
    # Robot state publisher
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name="robot_state_publisher",
        emulate_tty=True,
        namespace=vikings_bot_name,
        output='screen',
        parameters=[{
            'use_sim_time': use_sim,
            'frame_prefix': PythonExpression(["'",vikings_bot_name, "/'"]),
            'robot_description': Command([
                'xacro ',
                PathJoinSubstitution([
                    FindPackageShare('vikings_bot_description'),
                    'xacro',
                    'vikings_bot.xacro'
                ]),
                ' vikings_bot_name:=', vikings_bot_name,
                ' use_sim:=', use_sim
            ])
        }]
    )
    return LaunchDescription([
        vikings_bot_name_arg,
        robot_file_arg,
        use_sim_arg,
        robot_state_publisher_node,
        ])


