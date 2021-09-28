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

#Ask user for a start date
user_date = input("Enter data to search for Sara: ")


#Create a variable pointing to the data file 
file_name = './data/raw/sara.txt'

#Create a file object from the file 
file_object = open(file_name, 'r')

#Read contents of file into a list 
line_list = file_object.readlines()

#Close the file 
file_object.close()

#Create two empty dictionaries 
date_dict = {}
coord_dict = {} 

#Iterate through all lines in the lineList
for lineString in line_list:
    if lineString[0] in ("#","u"): continue #membership rules. Looks at first character. If in this tuple, evaluate to true and trigger the continue 

    #Split the string into a list of data items 
    lineData = lineString.split()
    
    #Extract items in list into variables 
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    
    #Print the location of Sara
   # print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},long:{obs_lon} on {obs_date}")
    
   # if =1,2,3, 
       # date_dict[record_id] = obs_date #looks like a number but being pulled as a string first. Nominal value (unique code, better kept as a string)
       # coord_dict[record_id] = (obs_lat,obs_lon)
       
    if obs_lc in ("1","2","3"):
       # print(f"Record {record_id} indicated Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")
        date_dict[record_id] = obs_date
        coord_dict[record_id] = (obs_lat,obs_lon)
        
#Create empty list to hold matching keys 
matching_keys = []

#Loop through items in the date_dict, and collect keys for matching dates
for date_item in date_dict.items(): 
    #get the key and  date of the item 
    the_key, the_date = date_item
    #see if the date matches the user date 
    if the_date == user_date: 
        matching_keys.append(the_key)
        
#Reveal locations for each key in matching_keys
for matching_key in matching_keys: 
    the_coords = coord_dict[matching_key]
    obs_date = date_dict[matching_key]
    print(f"Record {matching_key} indicates Sara was seen at lat:{obs_lat},long:{obs_lon} on {obs_date}")