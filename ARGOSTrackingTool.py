#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Shana Shapiro (shana.shapiro@duke.edu)
# Date:   Fall 2021
#--------------------------------------------------------------

#Pretend we read one line of data from the file 
lineString = '20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0'

#Split the string into a list of data items 
lineData = lineString.split()

#Extract items in list into variables 
record_id = lineData[0]
obs_date = lineData[2]
obs_lc = lineData[4]
obs_lat = lineData[5]
obs_lon = lineData[6]

#Print the location of Sara
print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},long:{obs_lon} on {obs_date}")