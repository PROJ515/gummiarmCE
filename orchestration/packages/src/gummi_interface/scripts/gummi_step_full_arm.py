#!/usr/bin/env python

import rospy
import sys
import csv

from gummi_interface.gummi import Gummi

def main(args):

    pi = 3.1416
    print("Please enter path to folder where you want data file saved:")
    path =  raw_input()

    rospy.init_node('gummi', anonymous=True)
    r = rospy.Rate(60)  
    
    cocontractionsToTry = (0.0, 0.25, 0.5, 0.75, 1.0)

    rest = (-0.13, -0.3, 0.89, -0.26, -0.05, 0.69, 0.6)
    desired = (0.16, 0.56, 0.35, -0.56, 0.04, 0.40, -0.26)

    gummi = Gummi()

    gummi.setCocontraction(0.4, 0.4, 0.4, 0.4, 0.4)

    print('WARNING: Moving joints sequentially to equilibrium positions.')
    gummi.doGradualStartup()
    
    print('WARNING: Moving to resting pose, hold arm!')
    rospy.sleep(3)

    for i in range(0, 400):
        gummi.goRestingPose()
        r.sleep()

    print("GummiArm is live!")
     
    for cocont in cocontractionsToTry: 

        gummi.setCocontraction(cocont, cocont, cocont, cocont, cocont)
      
        for att in range (1,2):

            print("Moving arm into place.")
            for i in range (0,400):
                gummi.servoTo(rest)
                r.sleep()
            print("Test started, cocontraction: " + str(cocont) + ", attempt: " + str(att) + ".")
            
            fileName = path + '/step_test_full_arm_s_' + str(cocont) + '_a_' + str(att) + '.csv'
            with open(fileName, 'wb') as csvfile:
                #writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                #writer.writerow(['time','desired','angle', 'equilibrium', 'flexor', 'extensor'])
                
                time1 = rospy.Time.now()
                now = False
                for i in range (0,1000):

                    if i < 200:
                        command = rest
                    else:
                        if i < 600:
                            command = desired
                            now = False
                            if i == 200:
                                now = True
                        else:
                            command = rest
                            now = False
                            if i == 600:
                                now = True

                    gummi.goTo(command, now)

                    #angle = joint.getJointAngle() * 180/pi
                    #time2 = rospy.Time.now()
                    #duration = time2-time1
                    #delta = duration.to_sec()
                    #equilibrium = joint.getDesiredEquilibrium()
                    #cocontraction = joint.getCommandedCocontraction()
                    #flexor = joint.getFlexorAngle()
                    #extensor = joint.getExtensorAngle()

                    #writer.writerow([delta, command, angle, equilibrium, cocontraction, flexor, extensor])
                    r.sleep()
            
if __name__ == '__main__':
    main(sys.argv)
