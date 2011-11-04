#!/usr/bin/env python

import roslib; 
roslib.load_manifest('srs_grasping')
import sys
import openravepy
import grasping_functions

package_path = roslib.packages.get_pkg_dir('srs_grasping')
##################################################################################	
class SCRIPT():###################################################################
##################################################################################	

	# ------------------------------------------------------------------------------------
	# ------------------------------------------------------------------------------------
	def __init__(self):

		self.robotName = 'robots/care-o-bot3.zae'
		#self.robotName = 'robots/barrett-hand.zae'


		if (len(sys.argv)<=1):
			self.targetName = 'Milk'
			self.object_path = package_path+"/DB/obj/"+self.targetName+'.xml'


		else:
			self.targetName = sys.argv[1]

			if self.targetName[len(self.targetName)-3:len(self.targetName)] == ".iv":
				self.object_path = package_path+'/DB/obj/'+self.targetName;
			else:
				self.object_path = package_path+'/DB/obj/'+self.targetName+'.xml'

		print "Loaded values: (%s, %s)" %(self.robotName, self.object_path)



	# ------------------------------------------------------------------------------------
	# ------------------------------------------------------------------------------------
	def run(self):
	
		env = openravepy.Environment()
    		robot = env.ReadRobotXMLFile(self.robotName)
		env.AddRobot(robot)
		target = env.ReadKinBodyXMLFile(self.object_path)
		env.AddKinBody(target)

		robot.SetActiveManipulator("arm")		#care-o-bot
		#robot.SetActiveManipulator("hand")		#barretthand
		gmodel = openravepy.databases.grasping.GraspingModel(robot=robot,target=target)
		if not gmodel.load():
		    print "GENERATING GRASPS..."
		    gmodel.autogenerate()
		    print "GENERATING GRASPS HAS FINISHED."



		grasping_functions.generateFile(targetName=self.targetName, gmodel=gmodel, env=env)

		raw_input("Press ENTER to finish.")
		


##########################################################################
if __name__ == "__main__":################################################
##########################################################################
	s = SCRIPT()
    	s.run()
