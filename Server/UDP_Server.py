import sqlite3
import socket
import os.path
import time
import sys
import atexit
import math
import localization as lx

class SensorData(object):
    def __init__(self,MAC,ID):
        self.mac = MAC
        self.name = ID
        self.data_dict = {}
    def findCombo(self,MAC_Beacon):
        ret = 0
        for beacon in self.data_dict.items():
            # beacon = (mac, [rssi,timestamp])
            if beacon[0] == MAC_Beacon:
                ret = 1
                break
        return ret
    def replaceData(self,MAC,RSSI,db):
        # If we are replacing data, we should already know if the combo exists
        # or not
        db.execute('SELECT X FROM node WHERE MAC=?',(MAC,))
        X = db.fetchone()[0]
        db.execute('SELECT Y FROM node WHERE MAC=?',(MAC,))
        Y = db.fetchone()[0]
        db.execute('SELECT Z FROM node WHERE MAC=?',(MAC,))
        Z = db.fetchone()[0]

        est_dist = math.pow(math.e,(int(RSSI) + 42.849) / -10.693)

        self.data_dict[MAC] = [est_dist,time.time(),X,Y,Z]

    def clearOld(self):
        for beacon in self.data_dict.items():
            if time.time() - beacon[1][1] > 2:
                del self.data_dict[beacon[0]]
                
    def __str__(self):
        st = str(self.mac)+","+str(self.name)+"\n\n"
        for i in self.data_dict:
            st = st+i+"\n"

        return st

# SensorData object notes:
#
#   Dictionary?
#   {  BEACON_MAC : [RSSI, TimeStamp]  }
#
##############################################################
def trilat2D(nodes):
    mySolver = "LSE"
    P = lx.Project(mode='2D',solver=mySolver)

    for anchors in nodes.items():
        P.add_anchor(anchors[0],(anchors[1][2],anchors[1][3]))

    t, label = P.add_target()
    for anchors in nodes.items():
        t.add_measure(anchors[0],anchors[1][0])

    P.solve()
    center = t.loc

    return center

##############################################################

databaseFilePath = 'database.db'

###############################################################
################# SOCKET SETUP AND CONNECTION #################
UDP_IP = "127.0.0.1"
UDP_PORT = 5007

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

sock.bind((UDP_IP,UDP_PORT))

###############################################################
###############################################################
if(os.path.exists(databaseFilePath)):
    pass
else:
    input("Database Missing...")
    sys.exit()

conn = sqlite3.connect(databaseFilePath)
c = conn.cursor()
###############################################################

sensorData = []

while True:

    sensorIndex = 0
    found = False
    
    # Receive a packet of data over UDP. Buffer size set at 1024 bytes but 
    # can be decreased.
    data, addr = sock.recvfrom(1024)
    print "Received Message:", data

    # Each packet will be a series of comma-deliniated data. Split the data
    # to create a list of all important properties.
    splitData = data.split(',')
    #print splitData,"\n"

    MAC_Sensor = splitData[0]
    MAC_Beacon = splitData[1]
    Rssi = splitData[2]

    for i in range(len(sensorData)):
        if sensorData[i].mac == MAC_Sensor:
            # This is the sensor data object we want
            sensorIndex = i
            found = True
            break

    # Now index contains the correct sensor object

    # We don't have a sensor data object for this sensor
    # Create a new one and append to the sensorData list
    if not(found):
        c.execute('SELECT ID FROM sensor WHERE MAC=?',(MAC_Sensor,))

        sensorID = c.fetchone()
        newSensor = SensorData(MAC_Sensor,sensorID[0]) 

        sensorData.append(newSensor)
        sensorIndex = len(sensorData) - 1

    # Clear out old data from beacons
    print "Cleaning expired data...\n"
    sensorData[sensorIndex].clearOld()

    # Add the new values
    print "Adding new data values...\n"
    sensorData[sensorIndex].replaceData(MAC_Beacon,Rssi,c)

    print sensorData[sensorIndex].data_dict.items()

    # Check if there are 3 or more beacons for this sensorData
    if len(sensorData[sensorIndex].data_dict.items()) > 2:
        loc = trilat2D(sensorData[sensorIndex].data_dict)
        print "LOCATION:",loc

    # CONVERT TO DISTANCE
    # TRILAT
    # UPDATE POSITION DATABASE

input("Press any key to continue...")
socket.close()

