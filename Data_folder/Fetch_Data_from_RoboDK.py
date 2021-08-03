from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
import re
RDK = Robolink()
robot = RDK.Item('GSK RMD08')      # retrieve the robot by name
file = open(r'D:\robo_data_TESTING(1).txt','w')
for i in range(104,171,2):
    for j in range(-40,91,2):
        for k in range(-90,69,2):
            robot.setJoints([i,j,k,0])
            stri = str(robot.Pose())
            ext=re.findall('Pose\((.*)\):',stri)[0]+', '+str(i)+', '+str(j)+', '+str(k)+'\n'
            print(ext)
            file.writelines(ext)
itemlist = RDK.ItemList()