# gummiarmCE
Superrepository for all the gummi arm CE packages.

This is the first bundle from all the current repositories from GummiArmCE and the latest version of dynamixel-motors from arebgun. 

**ATTENTION:** This bundle was not tested yet and should be used with caution, as errors in robotics software may cause damage to property and personnel. 

## Before you run it

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

## Running it for the first time

Each time you test new code or make considerable changes to source, it is recommended that you start the robot with another person on the look-out to turn the arm off as fast as possible. 
Specially if this is the first time that you are running the code on your newly assembled arm, you will need another person to turn off the robot really fast, hopefully before it does anything dangerous. Currently the design has no panic button, so doing this alone is rather tricky. Surely, the dynamixel motors are sturdy and you can always print new 3d parts, but nylon can have rough edges and to be on the safe side it is better to be careful. 

1. Run manager and controllers again. If there are no errors, you are almost ready to start the arm.
2. Grab a buddy.
   
  One of you will run the arm, the other will be ready to disconnect the power supply if the arm moves in a strange way. 
  
3. Run gummi.launch while your partner is ready to shut it down.

 Be on the look-out for how it is going to move. The current home position is having the arm with the shoulder close to the base, with the upper arm vertical, elbow in a 90 degree angle and the end effector positioned straight ahead. When running gummi, most if not all motors will turn so that this position can be achieved. This usually looks like a jerky, lateral shoulder elevation with elbow being brought to 90 degrees and some rotation of the end-effector forearm roll. 
 
 ***ATTENTION:*** Extreme movements that do not fall under this category should prompt immediate shut down and revision of software and hardware elements. 
 
 Since now you and your buddy are ready, run:
 
 ```$ roslaunch gummi_interface gummi.launch ```
 
 If everything went correctly the arm is now on its home position. You can test it further.
 
## HMI and Moveit

### HMI
To have direct access to the joint angles, a slider control interface can be run with :

`$ roslaunch gummi_interface hmi.launch`

Remember, this is direct access to joint angles, so it will bump into things if you make it so. The arm is compliant, but if joints are set to a high co-contraction level and maximum servo velocities were changed to high levels, this can cause accidents. 

### Moveit

Currently the latest moveit model for the handshake is under development, so the mesh files for it are not showing the right information and there will be a big error on end-effector position. With that being said, one should still be able to test path planning with moveit if gummi.yaml is correct. 

Run the moveit demo:

```$ roslaunch gummi_moveit demo.launch```

## Troubleshooting

If you had to turn off the arm because you thought it was moving weirdly, there are 2 possibilities here:
1. Either the arm is working correctly, only the movement is rather jerky and it would in the end work out or;
2. There is some configuration problems. 

### The tendons unspooled from some pulley(s) 

Wrong spooling tensioning or orientation (i. e. clockwise when it was supposed to be counter-clockwise). Check wiki for correct spooling intructions and orientations. 

### The arm started moving to a very weird position

If an encoder or a 3d piece is positioned with an 180 degree error, the controller will never get to the right start position, as it will try to move the joint in the opposite way, increasing the error. This will look like a movement that does not end and eventually reaches mechanical joint angle, either:

 - turning off the motor with overcurrent (or destroying the motor if this was turned off) or;
 - pulling a tendon or;
 - breaking a 3d printed part.
 
 Note that at this point the robotic arm does not have any concept of collision (it is just trying to position joint angles to its home position) so the arm may also smash anything (object or person) in its way, including itself. 
 
 We want to prevent this, so it is best to check that all assembly instructions were followed correctly. ***But before correcting anything, you need to make sure this is actually an assembly or software mistake!*** Check assembly instructions, check if the code is correct for the specific base you are using, check servo ROM and software parameters for the affected joints - specially if you introduced changes. If you are sure it is an assembly mistake, then, correct it. If you are unsure, open an issue so we can assist you better. 
 
 ### I've followed all the assembly instructions or I've bought this thing from you already assembled, supposedly correctly so!
 
 Make sure you have the correct clone type. Not all bases are exactly the same, with different joint angle limits and different standard orientations. Loading the wrong base definition may not instantly fail, but will cause unpredictable errors. Make sure this is not the case.

### Something else happened: Code failed with random error, just got stuck somewhere, or nothing happened

Open an issue and try to be as descriptive as possible (error messages or where applicable screenshots, photos, videos) highlighting relevant changes you implemented on your particular setup. 


## TO-DOs:

### Important testing, i.e., things that can break the robot and hurt people should include: ##
- Joint limits (minAngle, maxAngle), Servo offset values (servoOffset, servoRange), motor min and max parameters
- Dynamixel motor modes - check correct multiturn settings where applicable 
- Hardware assembly problems - e. g. 180 degree rotations of 3d printed parts and motor/encoders

### Additional testing and tunning necessary to make this release into a production one ##
- Complete ee_handshake urdf and srdf model with appropriate mesh files
- Fix or remove broken .launch files
- Implement fastswitch model
- Finish .yaml base and ee autogeneration
- Remove unnecessary files
- Test end-effector position in move-it
