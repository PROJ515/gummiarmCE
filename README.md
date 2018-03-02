# gummiarmCE
Superrepository for all the gummi arm CE packages.

This is the first bundle from all the current repositories from GummiArmCE and the latest version of dynamixel-motors from arebgun. 

**ATTENTION:** This bundle was not tested yet and should be used with caution, as errors in robotics software may cause damage to property and personnel. 

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

# Necessary steps to get it running

1. 
