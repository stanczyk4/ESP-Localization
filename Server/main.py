import atexit
import time
import sys

#local libraries
import database
import server
import packet
import sensorClass
import trilat

databaseFilePath = 'database.db'
serverIP = "127.0.0.1"
serverPORT = 5006

#sensorData = []

def programExit(db,serv):
    db.closeDatabase()
    serv.closeSocket()
    sys.exit()


def main():
    #create database object db to handle all database functionality
    db = database.Database(databaseFilePath)
    #create server object serv to handle all server operations
    serv = server.Server(serverIP, serverPORT)

    #register an OnExit function to close the database and server in case the program exits
    atexit.register(programExit, db, serv)

    #start listening to packets in the background
    serv.listenForPackets()
    sensorData = sensorClass.SensorList()

    while True:
        #checks if we have a packet, if so, do something else loop again
        if not serv.queue.empty():
            newPacket = packet.Packet(serv.queue.get())
            newPacket.sortPacket()

            sensorData.getIndex(newPacket.MAC_Sensor)
            #Now index contains the correct sensor object

            # If we dont have a sensor data object for this sensor
            # Create a new one and append to the sensorData list
            sensorData.wasFound(newPacket.MAC_Sensor, db)

            # Clear out old data from beacons
            print "Cleaning expired data...\n"
            sensorData.list[sensorData.sensorIndex].clearOld()

            # Add the new values
            print "Adding new data values...\n"
            sensorData.list[sensorData.sensorIndex].replaceData(newPacket.MAC_Beacon,newPacket.Rssi,db.c)

            #print sensorData[sensorIndex].data_dict.items()
            print sensorData.list[sensorData.sensorIndex].data_dict.items()

            # Check if there are 3 or more beacons for this sensorData, if so, Trilaterate it
            if len(sensorData.list[sensorData.sensorIndex].data_dict.items()) > 2:
                loc = trilat.trilat2D(sensorData.list[sensorData.sensorIndex].data_dict)
                print "LOCATION:",loc


if __name__ == "__main__":
    main()
