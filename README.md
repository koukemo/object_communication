# Object Communication
![Object Communication](https://img.shields.io/badge/object-communication-blue)

Sending and receiving obj files in ROS2


## Installing

---

- ROS2

## Developing

---

### Setting up Dev

```
cd ~/ros2_ws/src
git clone git@github.com:koukemo/object_communication.git
```

### Building

```
cd ~/ros2_ws
colcon build --packages-select object_communication
```

## Tests

---

Receive `test.obj` in [data/](data) as `out.obj` .

<br>

Before executing, please do the following : <br>
(*You will need to do this for each new terminal you open!)

```
. install/setup.bash
```

<br>

Publisher(terminal1) : 
```
ros2 run object_communication 3dobject_publish
```

Subscriber(terminal2) :
```
ros2 run object_communication 3dobject_subscribe
```
