import unittest
from joint_model import JointModel

#TODO: Integrate with Rostest
 
class TestJointModel(unittest.TestCase):
 
    def test_initialize_joint_model_for_elbow(self):
        jm = JointModel("test")
        self.assertIsNotNone(jm)

    def test_load_calibration_agonist(self):
        jm = JointModel("test")
        self.assertIsNotNone(jm.fAgonist)

    def test_load_calibration_antagonist(self):
        jm = JointModel("test")
        self.assertIsNotNone(jm.fAntagonist)

    def test_interpolation_agonist(self):
        jm = JointModel("test")
        jm.calculateCommands(0.0,0.0)
        angle = jm.getAgonist()
        self.assertEqual(angle, 0.0) #TODO: Create test dataset

    def test_interpolation_antagonist(self):
        jm = JointModel("test")
        jm.calculateCommands(0.0,0.0)
        angle = jm.getAntagonist()
        self.assertEqual(angle, 0.0) #TODO: Create test dataset
        
if __name__ == '__main__':
    unittest.main()
