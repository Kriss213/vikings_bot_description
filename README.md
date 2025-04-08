# vikings_bot_description

<hr>

### Description
This package contains `vikings_bot` project robot description related files.

<hr>

### Installation

Download source and install dependencies:
```
rosdep update
rosdep install --ignore-src --default-yes --from-path src
```

Build package:
```
colcon build
source install/setup.bash
```


To launch robot state publisher:
```
ros2 launch vikings_bot_description robot_state_publisher.launch.py
```



