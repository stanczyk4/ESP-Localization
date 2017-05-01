Code for the PSR Server

How to use:
  Download the source code and run main.py using python 2.7. 
  
  
  Required repositories: matplotlib, numpy, localization, shapely, sqlite3, itertools
  All can be installed via a - pip install *insert above repository name*
                            ex: pip install matplotlib
                            
What it does:
  Creates a local UDP Server to listen for incoming packets. Packets received must be in the format of SENSOR_MACADDRESS,NODE_MACADDRESS,RSSI
  When a packet comes in, will search in the database to get the x,y,z positon for the node. 
  Sorts through an array of sensor information to remove all data that is older than 2 seconds, replace data from nodes already existing
  
  After Sorting is complete, run the information through a localization method and return the predicted position.
  Graph the nodes and predicted position.
 
 
Known Issues:
If a packet comes in the wrong format, might crash program
If a packet comes in and values can't be found in database, program will crash
Matplotlib graph will appear to be frozen, but will continue to update. Can't interact with graph features though

                            
