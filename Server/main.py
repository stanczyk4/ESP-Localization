import atexit
import time

#local libraries
import database
import server
import packet #currently doing nothing, gnna put some code from main into this later
import sensorClass
import trilat

databaseFilePath = 'database.db'
serverIP = "127.0.0.1"
serverPORT = 5012

sensorData = []

def programExit(db,serv):
    db.closeDatabase()
    serv.closeSocket()

def main():
    #create database object db to handle all database functionality
    db = database.Database(databaseFilePath)
    #create server object serv to handle all server operations
    serv = server.Server(serverIP, serverPORT)

    #register an OnExit function to close the database and server in case the program exits
    atexit.register(programExit, db, serv)

    #start listening to packets in the background
    serv.listenForPackets()

    while True:
        #checks if we have a packet, if so, do something else loop again
        if not serv.queue.empty():
            #print serv.queue.get()
            splitData = serv.queue.get().split(',')
            MAC_Sensor = splitData[0]
            MAC_Beacon = splitData[1]
            Rssi = splitData[2]

            sensorIndex = 0
            found = False

            for i in range(len(sensorData)):
                if sensorData[i].mac == MAC_Sensor:
                    #this is the sensor data object we want
                    sensorIndex = i
                    found = True
                    break

            #Now index contains the correct sensor object

            # We dont have a sensor data object for this sensor
            # Create a new one and append to the sensorData list
            if not(found):
                sensorID = db.searchIDfromMACinSensor(MAC_Sensor)
                newSensor = sensorClass.SensorData(MAC_Sensor, sensorID[0])

                sensorData.append(newSensor)
                sensorIndex = len(sensorData) - 1

            # Clear out old data from beacons
            print "Cleaning expired data...\n"
            sensorData[sensorIndex].clearOld()

            # Add the new values
            print "Adding new data values...\n"
            sensorData[sensorIndex].replaceData(MAC_Beacon,Rssi,db.c)

            print sensorData[sensorIndex].data_dict.items()

            # Check if there are 3 or more beacons for this sensorData
            if len(sensorData[sensorIndex].data_dict.items()) > 2:
                loc = trilat.trilat2D(sensorData[sensorIndex].data_dict)
                print "LOCATION:",loc

            # CONVERT TO DISTANCE
            # TRILAT
            # UPDATE POSITION DATABASE

if __name__ == "__main__":
    main()
