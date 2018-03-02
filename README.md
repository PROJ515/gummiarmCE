# gummiarmCE
Superrepository for all the gummi arm CE packages.

This is the first bundle from all the current repositories from GummiArmCE and the latest version of dynamixel-motors from arebgun. 

**ATTENTION:** This bundle was not tested yet and should be used with caution, as errors in robotics software may cause damage to property and personnel. 

# Before you run it

1. Change the USB ids in src/gummi_base_template/manager.launch

 The way I do it is, I unplug all but one and see what is listed in /dev/serial/by-id. There is a link there. Copy paste that into the appropriate port_name in manager.launch (under either gummi_d, gummi_ae or gummi_se). Repeat the process for the other USB serial devices. Hopefully this will be done via a configuration script in the future, but for now, do it like this.  
 
2. Run catkin_make
3. Set up environment variables for ROS
 
 `$ source devel/setup.bash` _remeber to run this on each new terminal before trying to use ros commands._

4. Run manager and controllers:
 
 ```$ roslaunch gummi_base_template manager.launch```
  
 On another terminal run:
 
 ```$ roslaunch gummi_base_template controllers.launch```
 
5. Check for errors

 And change where appropriate the ids for the motors or the buses in which they are connected.

6. Run manager and controllers again to see if everything works out well

# Running it

1. Run manager and controllers. If there are no errors, you are almost ready to start the arm.
2. Grab a buddy.

  If this is the first time that you are running the code on your newly assembled arm, you will need another person to be on the lookout and turn off the robot really fast, hopefully before it does anything dangerous. Currently the design has no panic button: the dynamixel motors are sturdy and you can always print new 3d parts, but nylon can have rough edges and to be on the safe side it is better to be careful. 
  
  One of you will run the arm, the other will be ready to disconnect the power supply if the arm moves in a strange way. 
  
3. Run gummi.launch while your partner is ready to shut it down.

 Be on the look-out for how it is going to move. The current home position is having the arm with the shoulder close to the base, with the upper arm vertical, elbow in a 90 degree angle and the end effector positioned straight ahead. When running gummi, most if not all motors will turn so that this position can be achieved. This usually looks like a jerky, lateral shoulder elevation with elbow being brought to 90 degrees and some rotation of the end-effector forearm roll. 
 
 ***ATTENTION:*** Extreme movements that do not fall under this category should prompt immediate shut down and revision of software and hardware elements. 
 
 Since now you and your buddy are ready, run:
 
 ```$ roslaunch gummi_interface gummi.launch ```
 
 If everything went correctly the arm is now on its home position. You can test it further
 
# HMI and Moveit

## HMI
To have direct access to the joint angles, a slider control interface can be run with :

`$ roslaunch gummi_interface hmi.launch`

Remember, this is direct access to joint angles, so it will bump into things if you make it so. The arm is compliant, but if joints are set to a high co-contraction level and maximum servo velocities were changed to high levels, this can cause accidents. 

## Moveit

Currently the latest moveit model for the handshake is under development, so the mesh files for it are not showing the right information and there will be a big error on end-effector position. With that being said, one should still be able to test path planning with moveit if gummi.yaml is correct. 

Run the moveit demo:
```$ roslaunch gummi_moveit demo.launch```

# TO-DOs:

## Important testing, i.e., things that can break the robot and hurt people should include: ##
- Joint limits (minAngle, maxAngle), Servo offset values (servoOffset, servoRange), motor min and max parameters
- Dynamixel motor modes - check correct multiturn settings where applicable 
- Hardware assembly problems - e. g. 180 degree rotations of 3d printed parts and motor 

## Additional testing and tunning necessary to make this release into a production one ##
- Complete ee_handshake urdf and srdf model with appropriate mesh files
- Fix or remove broken .launch files
- Implement fastswitch model
- Finish .yaml base and ee autogeneration
- Remove unnecessary files
- Test end-effector position in move-it
