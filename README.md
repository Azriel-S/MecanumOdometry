Math for mecanum wheel odometry

A web site explaing the general concept is:
https://docs.google.com/document/d/1hZyp0voiU3fu0_DVSJWG9b193BgK567rUs9VWVcOfyc/edit

This uses a swerve drive, but the vectors are a good
explanation.

The math comes from:
https://github.com/acmerobotics/road-runner/blob/master/doc/pdf/Mobile_Robot_Kinematics_for_FTC.pdf

Mecanum_kinematics gives us the velocity of the robot.  
This is multiplied by the change in time to get the 
change in position with respect to the robot. This is 
last equation in section 2.3.

MecanumOdometry takes the current global position and
the change in the position with respect to the robot
to come up with the position in the field.  This also 
called the global position.  This is the last
equation in seciont 3.1.

This needs to be calculated in a loop.  For each pass
through the loop, store the current time and the positions
of each encoder.  Also save the last position and time.  
The change in time is the current time - the previous time.
A good reference for this is: 
https://www.bridgefusion.com/blog/2019/5/22/robot-localization-driving-to-field-coordinates

The math is a little different in this article since 
the wheels are arranged differently.  That is why we
are using the math from the pdf file.